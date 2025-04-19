from mcp_server_tls.config import TLS_CONFIG
from typing import Any, Dict, Optional
from mcp_server_tls.resources.project import describe_project, describe_projects

async def describe_project_tool(project_id: Optional[str] = None) -> Dict[str, str]:
    """
    通过火山引擎 TLS 获取当前权限下指定项目信息。
    """
    project_id = project_id or TLS_CONFIG.project_id
    if not project_id:
        raise ValueError("project id is required")

    try:
        return await describe_project(project_id)
    except Exception as e:
        return {"error": str(e)}

async def describe_projects_tool() -> Dict[str, Any]:
    """
    通过火山引擎 TLS 获取当前权限下的多个项目信息(限制10个)。
    """
    try:
        return await describe_projects()
    except Exception as e:
        return {"error": str(e)}
