import volcenginesdkecs
from volcenginesdkecs.models import *
from mcp_server_ecs.common.client import get_volc_ecs_client
from mcp_server_ecs.common.errors import handle_error
from mcp_server_ecs.common.logs import LOG, log_params
from mcp_server_ecs.tools.event_prompts import *
from mcp_server_ecs.tools.server import MCP

tools_name = ToolsName()
tools_description = ToolsDescription()


@MCP.tool(tools_name.DescribeSystemEvents, tools_description.DescribeSystemEvents)
@log_params
async def describe_system_events(params: DescribeSystemEventsParams):
    try:
        volc_client = get_volc_ecs_client()
        total_results = []
        next_token = None

        while True:
            response = volc_client.describe_system_events(
                volcenginesdkecs.DescribeSystemEventsRequest(
                    category=params.Category,
                    created_at_start=params.CreatedAtStart,
                    created_at_end=params.CreatedAtEnd,
                    event_ids=params.EventIds,
                    resource_ids=params.ResourceIds,
                    types=params.Types,
                    next_token=next_token,
                    max_results=params.MaxResults,
                )
            )

            if not response or not getattr(response, "system_events", None):
                return handle_error(tools_name.DescribeSystemEvents)

            total_results.extend(response.system_events)

            if len(total_results) >= params.NeedNum or not response.next_token:
                total_results = total_results[: params.NeedNum]
                break

            next_token = response.next_token

        LOG.info("Total system events found: %d", len(total_results))
        return {"response": {"system_events": total_results}}

    except Exception as e:
        return handle_error(tools_name.DescribeSystemEvents, e)
