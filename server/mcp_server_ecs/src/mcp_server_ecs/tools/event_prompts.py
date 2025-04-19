from pydantic import BaseModel, Field


class ToolsName(BaseModel):
    """
    Name for tool.
    """

    DescribeSystemEvents: str = "describe_system_events"


class ToolsDescription(BaseModel):
    """
    Description for tool.
    """

    DescribeSystemEvents: str = "查询系统事件列表"


class DescribeSystemEventsParams(BaseModel):
    Category: str = Field(
        default=None,
        description="系统事件类别。取值：ResourceEvent：资源事件;TaskEvent：任务事件",
    )

    CreatedAtStart: str = Field(
        default=None,
        description="以CreatedAtStart为起点，筛选创建时间在其之后的事件。默认值为CreatedAtEnd前24小时（参考请求参数CreatedAtEnd），格式为RCF3339",
    )

    CreatedAtEnd: str = Field(
        default=None,
        description="以CreatedAtEnd为终点，筛选创建时间在其之前的事件。默认值为现在，格式为RCF3339",
    )

    EventIds: list[str] = Field(
        default=None,
        description="事件ID，最多支持100个ID。您可以通过事件通知或调用本接口查询获取。参数 - N：表示事件的序号。多个事件ID之间用&分隔",
    )

    ResourceIds: list[str] = Field(
        default=None,
        description="资源ID，最多支持100个ID。您可以调用DescribeInstances接口，查询获取实例ID。参数 - N：表示资源的序号。多个资源ID之间用&分隔",
    )

    Status: list[str] = Field(
        default=None,
        description="""
                    系统事件的状态，最多支持10个。
                    取值：
                    UnknownStatus：未知状态
                    Executing：执行中
                    Succeeded：执行成功
                    Failed：执行失败
                    Inquiring：待响应
                    Scheduled：计划执行
                    Rejected：用户拒绝执行
                    Canceled：已取消
                    Pending：已暂停
                    Recovered：已恢复
                """,
    )

    Types: list[str] = Field(
        default=None,
        description="""
                    系统事件的类型，最多支持100个。
                    参数 - N：表示事件类型的序号。
                    多个事件类型之间用&分隔。
                    取值：
                    SystemFailure_Stop：因系统故障实例停止。
                    SystemFailure_Reboot：因系统故障实例重启。
                    DiskError_Redeploy：因硬盘异常实例重新部署。
                    GpuError_Redeploy：GPU异常，导致实例重新部署。
                    SystemMaintenance_Redeploy：因系统维护实例重新部署。
                    SystemMaintenance_StopAndRepair：实例停止，系统维修。
                    SystemFailure_Redeploy：因系统故障实例重新部署。
                    SystemFailure_Repair：系统故障，进行维修。
                    CreateInstance：创建实例。
                    RunInstance：启动实例。
                    StopInstance：停止实例。
                    DeleteInstance：删除实例。
                    SpotInstanceInterruption_Delete：抢占型实例中断，实例释放。
                    AccountUnbalanced_Stop：账户欠费，实例停止。
                    AccountUnbalanced_Delete：账户欠费，实例释放。
                    InstanceChargeType_Change：实例计费类型改变。
                    InstanceConfiguration_Change：实例配置变更。
                    FileSystemReadOnly_Change：文件系统变为只读状态。
                    RebootInstance：实例重启。
                    InstanceFailure：因操作系统错误实例异常。
                    ApplicationFailure：应用异常。
                    DeploymentSet_Modify：修改实例部署集。
                    ServerMigrationTask：服务器迁移任务。
                    ServerMigration_FirstSync：服务器迁移，全量数据同步。
                    ServerMigration_AdditionalSync：服务器迁移，增量数据同步。
                    GpuRiskDetected：GPU运行存在风险。
                    ElasticScheduledInstance_Create：弹性预约单创建。
                    ElasticScheduledInstance_Cancel：弹性预约单取消。
                    ElasticScheduledInstance_Deliver：弹性预约单交付。
                    ElasticScheduledInstance_AutoRelease：弹性预约实例自动释放。
                    ElasticScheduledInstance_Invalid：弹性预约单失效。
                    InfrastructureUpgrade_Redeploy：因基础设施升级实例重新部署。
                    DiskErrorDetected：硬盘异常。
                    DiskError_ReplaceDisk：因硬盘异常更换硬盘。
                    InstanceOOM：实例内存OOM。
                    MemoryRiskDetected：内存运行存在风险。
                    InstanceFileSystemFailure_StopAndRepair：因文件系统异常实例停机修复。
                """,
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
