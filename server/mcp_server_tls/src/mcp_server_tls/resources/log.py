import logging

from typing import Optional
from mcp_server_tls.resources.tls import TlsResource
from volcengine.tls.tls_exception import TLSException
from volcengine.tls.tls_requests import SearchLogsRequest
from volcengine.tls.tls_responses import SearchLogsResponse

logger = logging.getLogger(__name__)

class TlsLogResource(TlsResource):
    """
        火山引擎日志管理资源类
    """

    def search_logs_v2(self, topic_id: str, query: str, start_time: int, end_time: int,
                       limit: Optional[int] = None, context: Optional[str] = None, sort: str = "desc") -> SearchLogsResponse:
        """
        调用 SearchLogs 接口检索日志。
        api: https://www.volcengine.com/docs/6470/112195
        """
        request = SearchLogsRequest(topic_id, query, start_time, end_time, limit, context, sort)

        return self.client.search_logs_v2(request)


# 实例化资源
log_resource = TlsLogResource()

async def search_logs_v2_resource(topic_id: str, query: str, start_time: int, end_time: int, limit: int) -> dict:
    try:
        response = log_resource.search_logs_v2(topic_id, query, start_time, end_time, limit)
        search_result = response.get_search_result()
        search_result.analysis_result = vars(search_result.analysis_result)
        result =  vars(search_result)
        # 去掉无用字段
        result.pop("HitCount", None)
        return result
    except TLSException as e:
        logger.error(f"Search logs error: {e}")
        raise e

