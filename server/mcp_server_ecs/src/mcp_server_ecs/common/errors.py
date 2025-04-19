from mcp_server_ecs.common.logs import LOG


# 处理空响应错误
def _handle_empty_response(action_name):
    LOG.error("%s returned empty response", action_name)
    return {"error": "Empty response from server"}


# 处理异常错误
def _handle_exception(action_name, error):
    LOG.error("Exception when calling %s: %s", action_name, str(error))
    return {"error": str(error)}


def handle_error(action_name, error=None):
    """统一处理API错误响应

    Args:
        action_name: API动作名称
        error: 异常对象(可选)

    Returns:
        统一格式的错误响应字典
    """
    # 创建处理函数映射表
    handlers = {
        True: lambda: _handle_exception(action_name, error),
        False: lambda: _handle_empty_response(action_name),
    }

    return handlers[error is not None]()
