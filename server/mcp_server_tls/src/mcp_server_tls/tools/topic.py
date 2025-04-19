from typing import Any, Dict, Optional
from mcp_server_tls.config import TLS_CONFIG
from mcp_server_tls.resources.topic import describe_topic, describe_topics

async def describe_topic_tool(topic_id: Optional[str] = None) -> Dict[str, str]:
    """
    通过火山引擎 TLS 获取当前权限下指定主题信息。
    """
    topic_id = topic_id or TLS_CONFIG.topic_id
    if not topic_id:
        raise ValueError("topic id is required")

    try:
        return await describe_topic(topic_id)
    except Exception as e:
        return {"error": str(e)}

async def describe_topics_tool(project_id: Optional[str] = None) -> Dict[str, Any]:
    """
    通过火山引擎 TLS 获取当前权限下指定project_id下的多个主题信息(限制10个)。
    """
    project_id = project_id or TLS_CONFIG.project_id
    if not project_id:
        raise ValueError("project id is required")

    try:
        return await describe_topics(project_id)
    except Exception as e:
        return {"error": str(e)}