import volcenginesdkecs
from volcenginesdkecs.models import *
from mcp_server_ecs.common.client import get_volc_ecs_client
from mcp_server_ecs.common.errors import handle_error
from mcp_server_ecs.common.logs import LOG, log_params
from mcp_server_ecs.tools.instance_prompts import *
from mcp_server_ecs.tools.server import MCP

tools_name = ToolsName()
tools_description = ToolsDescription()


@MCP.tool(tools_name.DescribeInstances, tools_description.DescribeInstances)
@log_params
async def describe_instances(params: DescribeInstancesParams):
    try:
        volc_client = get_volc_ecs_client()
        total_results = []
        next_token = None

        while True:
            response = volc_client.describe_instances(
                volcenginesdkecs.DescribeInstancesRequest(
                    dedicated_host_cluster_id=params.DedicatedHostClusterId,
                    dedicated_host_id=params.DedicatedHostId,
                    deployment_set_group_numbers=params.DeploymentSetGroupNumbers,
                    deployment_set_ids=params.DeploymentSetIds,
                    eip_addresses=params.EipAddresses,
                    hpc_cluster_id=params.HpcClusterId,
                    instance_charge_type=params.InstanceChargeType,
                    instance_ids=params.InstanceIds,
                    instance_name=params.InstanceName,
                    instance_type_families=params.InstanceTypeFamilies,
                    instance_types=params.InstanceTypeIds,
                    ipv6_addresses=params.Ipv6Addresses,
                    key_pair_name=params.KeyPairName,
                    max_results=params.MaxResults,
                    primary_ip_address=params.PrimaryIpAddress,
                    project_name=params.ProjectName,
                    scheduled_instance_id=params.ScheduledInstanceId,
                    status=params.Status,
                    tag_filters=params.TagFilters,
                    vpc_id=params.VpcId,
                    zone_id=params.ZoneId,
                    next_token=next_token,
                )
            )

            if not response or not getattr(response, "instances", None):
                return handle_error(tools_name.DescribeInstances)

            total_results.extend(response.instances)

            if len(total_results) >= params.NeedNum or not response.next_token:
                total_results = total_results[: params.NeedNum]
                break

            next_token = response.next_token

        LOG.info("Total instances found: %d", len(total_results))
        return {"response": {"instances": total_results}}

    except Exception as e:
        return handle_error(tools_name.DescribeInstances, e)


@MCP.tool(tools_name.DescribeImages, tools_description.DescribeImages)
@log_params
async def describe_images(params: DescribeImagesParams):
    try:
        volc_client = get_volc_ecs_client()
        total_results = []
        next_token = None

        while True:
            response = volc_client.describe_images(
                volcenginesdkecs.DescribeImagesRequest(
                    image_ids=params.ImageIds,
                    image_name=params.ImageName,
                    instance_type_id=params.InstanceTypeId,
                    is_lts=params.IsLTS,
                    is_support_cloud_init=params.IsSupportCloudInit,
                    os_type=params.OsType,
                    platform=params.Platform,
                    project_name=params.ProjectName,
                    status=params.Status,
                    tag_filters=params.TagFilters,
                    visibility=params.Visibility,
                    next_token=next_token,
                    max_results=params.MaxResults,
                )
            )

            if not response or not getattr(response, "images", None):
                return handle_error(tools_name.DescribeImages)

            total_results.extend(response.images)

            if len(total_results) >= params.NeedNum or not response.next_token:
                total_results = total_results[: params.NeedNum]
                break

            next_token = response.next_token

        LOG.info("Total images found: %d", len(total_results))
        return {"response": {"images": total_results}}

    except Exception as e:
        return handle_error(tools_name.DescribeImages, e)


@MCP.tool(tools_name.DescribeInstanceTypes, tools_description.DescribeInstanceTypes)
@log_params
async def describe_instance_types(params: DescribeInstanceTypesParams):
    try:
        volc_client = get_volc_ecs_client()
        total_results = []
        next_token = None

        while True:
            response = volc_client.describe_instance_types(
                volcenginesdkecs.DescribeInstanceTypesRequest(
                    image_id=params.ImageId,
                    instance_type_ids=params.InstanceTypeIds,
                    next_token=next_token,
                    max_results=params.MaxResults,
                )
            )

            if not response or not getattr(response, "instance_types", None):
                return handle_error(tools_name.DescribeInstanceTypes)

            total_results.extend(response.instance_types)

            if len(total_results) >= params.NeedNum or not response.next_token:
                total_results = total_results[: params.NeedNum]
                break

            next_token = response.next_token

        LOG.info("Total instance types found: %d", len(total_results))
        return {"response": {"instance_types": total_results}}

    except Exception as e:
        return handle_error(tools_name.DescribeInstanceTypes, e)


@MCP.tool(
    tools_name.DescribeAvailableResource, tools_description.DescribeAvailableResource
)
@log_params
async def describe_available_resource(params: DescribeAvailableResourceParams):
    try:
        volc_client = get_volc_ecs_client()
        total_results = []

        response = volc_client.describe_available_resource(
            volcenginesdkecs.DescribeAvailableResourceRequest(
                destination_resource=params.DestinationResource,
                elastic_scheduled_instance_type=params.ElasticScheduledInstanceType,
                instance_charge_type=params.InstanceChargeType,
                instance_type_id=params.InstanceTypeId,
                spot_strategy=params.SpotStrategy,
                volume_type=params.VolumeType,
                zone_id=params.ZoneId,
            )
        )

        if not response or not getattr(response, "available_zones", None):
            return handle_error(tools_name.DescribeAvailableResource)

        total_results.extend(response.available_zones)

        LOG.info("Total available zones found: %d", len(total_results))
        return {"response": {"available_zones": total_results}}

    except Exception as e:
        return handle_error(tools_name.DescribeAvailableResource, e)
