from mcp_server_tls.config import TLS_CONFIG
from typing import Optional, Any
from mcp_server_tls.resources.text_analysis import (
    create_app_instance_resource,
    describe_app_instances_resource,
    create_app_scene_meta_resource,
    describe_session_answer_resource,
)

async def text2sql(question: str, topic_id: Optional[str] = None, session_id: Optional[Any] = None) -> dict:
    """Converts user-entered natural language into TLS-compliant SQL statements

    Args:
        question: Question of user input, description of the TLS standard SQL statement user want to obtain
        topic_id: Optional topic ID. If not provided, uses the globally configured topic.
        session_id: Optional session ID. if not provided, it will be created. else it will continue to communicate

    Returns:
        answer: response of tls copilot, Includes reasoning process
        Suggestions: Suggestions of tls copilit for user input
        session_id: The session_id of the user's conversation with tls copilot

    Examples:
        # get sql by question
        text2sql("I want get count number of error log by `__content__` field")

        # get sql by question and specify topic_id
        text2sql("I want get count number of error log by `__content__` field", "specify the topic_id")

        # get sql by question and specify topic_id and exist session_id"
        text2sql("I want get count number of error log by `__content__` field", "specify the topic_id", "exist session_id")
    """
    # 转下session类型,解决json.loads类型问题
    session_id = str(session_id) if session_id is not None else None

    topic_id = TLS_CONFIG.topic_id or topic_id
    if not topic_id:
        raise ValueError("topic id is required")

    instance_name = TLS_CONFIG.account_id
    if not instance_name:
        raise ValueError("account_id of your env variable should be set")

    instance_type = "ai_assistant"
    app_meta_type = "tls.app.ai_assistant.session"

    try:
        app_instance = await describe_app_instances_resource(instance_name, instance_type)
        instance_list = app_instance.get("InstanceInfo", [])
        if len(instance_list) == 0:
            create_app_instance_response = await create_app_instance_resource(
                instance_name=instance_name,
                instance_type=instance_type
            )
            instance_id = create_app_instance_response.get("InstanceID", "")
        else:
            instance_id = instance_list[0].get("InstanceId", "")

        if not session_id:
            # 创建ai会话
            create_app_scene_meta_response = await create_app_scene_meta_resource(
                instance_id=instance_id,
                app_meta_type=app_meta_type,
                topic_id=topic_id,
            )
            session_id = create_app_scene_meta_response.get("Id", "")

        # 读取返回的会话信息,解析sql
        answer = await describe_session_answer_resource(
            instance_id=instance_id,
            topic_id=topic_id,
            question=question,
            session_id=session_id,
        )

        return answer

    except Exception as e:
        return {"error": str(e)}
