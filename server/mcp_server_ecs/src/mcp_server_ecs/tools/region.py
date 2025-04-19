import volcenginesdkecs
from volcenginesdkecs.models import *
from mcp_server_ecs.common.logs import LOG, log_params
from mcp_server_ecs.common.errors import handle_error
from mcp_server_ecs.common.client import get_volc_ecs_client
from mcp_server_ecs.tools.region_prompts import *
from mcp_server_ecs.tools.server import MCP

tools_name = ToolsName()
tools_description = ToolsDescription()


@MCP.tool(tools_name.DescribeRegions, tools_description.DescribeRegions)
@log_params
async def describe_regions(params: DescribeRegionsParams):
    try:
        volc_client = get_volc_ecs_client()
        total_results = []
        next_token = None

        while True:
            response = volc_client.describe_regions(
                volcenginesdkecs.DescribeRegionsRequest(
                    region_ids=params.RegionIds,
                    max_results=params.MaxResults,
                    next_token=next_token,
                )
            )

            if not response or not getattr(response, "regions", None):
                return handle_error(tools_name.DescribeRegions)

            total_results.extend(response.regions)

            if len(total_results) >= params.NeedNum or not response.next_token:
                total_results = total_results[: params.NeedNum]
                break

            next_token = response.next_token

        LOG.info("Total regions found: %d", len(total_results))
        return {"response": {"regions": total_results}}

    except Exception as e:
        return handle_error(tools_name.DescribeRegions, e)


@MCP.tool(tools_name.DescribeZones, tools_description.DescribeZones)
@log_params
async def describe_zones(params: DescribeZonesParams):
    try:
        volc_client = get_volc_ecs_client()
        response = volc_client.describe_zones(
            volcenginesdkecs.DescribeZonesRequest(
                zone_ids=params.ZoneIds,
            )
        )

        if not response or not getattr(response, "zones", None):
            return handle_error(tools_name.DescribeZones)

        return {"response": {"zones": response.zones}}

    except Exception as e:
        return handle_error(tools_name.DescribeZones, e)
