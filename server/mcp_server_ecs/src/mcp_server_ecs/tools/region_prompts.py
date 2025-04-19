from pydantic import BaseModel, Field


class ToolsName(BaseModel):
    """
    Name for tool.
    """

    DescribeRegions: str = "describe_regions"

    DescribeZones: str = "describe_zones"


class ToolsDescription(BaseModel):
    """
    Description for tool.
    """

    DescribeRegions: str = "查询地域列表"

    DescribeZones: str = "查询可用区列表"


class DescribeRegionsParams(BaseModel):
    RegionIds: list[str] = Field(
        default=None,
        description="地域ID，最多支持20个ID",
    )

    MaxResults: int = Field(
        default=20,
        description="分页查询时设置的每页行数，需要根据用户的意图来设置",
        ge=0,
        le=100,
    )

    NeedNum: int = Field(
        default=20,
        description="用户需要查询的事件总数，需要根据用户的意图来设置",
    )


class DescribeZonesParams(BaseModel):
    ZoneIds: list[str] = Field(
        default=None,
        description="可用区ID，最多支持20个。",
    )
