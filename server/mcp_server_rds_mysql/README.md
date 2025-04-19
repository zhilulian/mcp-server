# MCP Server 产品名称：火山引擎 RDS MySQL MCP
[![产品Logo](./static/image/RDSMySQL.png)

## 版本信息
v1.0.0

## 产品描述
### 短描述
火山引擎RDS MySQL版即开即用、稳定可靠的关系型数据库服务

### 长描述
火山引擎RDS MySQL版是由火山引擎提供的完全兼容开源MySQL的关系型数据库服务，支持实例管理、账号管理、数据库管理、备份恢复、白名单、透明数据加密、数据迁移、数据同步、读写分离、安全审计、高可用、版本升级、备份恢复等关键特性。

## 分类
数据库

## 标签
MySQL, RDS, 关系型数据库, 数据库

## Tools
本 MCP Server 产品提供以下 Tools:

### Tool 1: list_rds_mysql_instances
#### 详细描述
查看用户的 RDS MySQL 实例列表，支持分页查询

#### 最容易被唤起的 Prompt示例
"列出我的RDS MySQL实例"

### Tool 2: describe_rds_mysql_detail
#### 详细描述
根据指定RDS MySQL 实例ID查看实例详情

#### 最容易被唤起的 Prompt示例
"查看实例ID为mysql-123456的详细信息"

### Tool 3: list_rds_mysql_instance_engine_minor_versions
#### 详细描述
查询指定RDS MySQL实例可升级的内核小版本

#### 最容易被唤起的 Prompt示例
"查看实例mysql-123456可升级的内核版本"

### Tool 4: list_rds_mysql_instance_accounts

#### 详细描述
查看指定RDS MySQL实例的数据库账号列表，支持分页查询

#### 最容易被唤起的 Prompt示例
"列出实例mysql-123456的所有数据库账号"

### Tool 5: list_rds_mysql_instance_databases


#### 详细描述
查看指定RDS MySQL实例的数据库列表，支持分页查询

#### 最容易被唤起的 Prompt示例
"列出实例mysql-123456的所有数据库"

### Tool 6: list_rds_mysql_instance_parameters
#### 详细描述
查询指定RDS MySQL实例的参数配置


#### 最容易被唤起的 Prompt示例
"查看实例mysql-123456的参数配置"

### Tool 7: list_rds_mysql_parameter_templates

#### 详细描述
查询MySQL实例的参数模板列表，支持分页查询


#### 最容易被唤起的 Prompt示例
"列出可用的MySQL参数模板"

### Tool 8: describe_rds_mysql_parameter_template

#### 详细描述
根据参数模版ID查询指定的参数模板详情



#### 最容易被唤起的 Prompt示例
"查看参数模板mysql-template-123的详细信息"

### Tool 9: modify_rds_mysql_instance_alias


#### 详细描述
修改RDS MySQL实例名称



#### 最容易被唤起的 Prompt示例
"将实例mysql-123456的名称改为生产数据库"

### Tool 10: modify_rds_mysql_account_description
#### 详细描述
修改RDS MySQL实例的数据库账号的描述信息


#### 最容易被唤起的 Prompt示例
"将账号admin的描述改为管理员账号"

## 可适配平台
方舟，Cursor，Python


## 鉴权方式
API Key鉴权，需要在配置文件中设置access_key_id和access_key_secret

## 安装部署
### Using uv (recommended)
```bash
uv --directory /path/to/mcp-server-rds-mysql run server.py
```

### Using PIP
```bash
pip install volcenginesdkrdsmysqlv2
python -m mcp_server_rds_mysql
```


## 在不同平台的配置
### 方舟
#### 体验中心
1. 在MCP生态广场选择"RDS MySQL MCP"
2. 选择运行平台(方舟/Cursor/Python)
3. 查看可用的Tools功能描述与输入参数
4. 获取专属URL或代码示例
5. 前往方舟平台体验中心进行体验



## 部署
### UVX
```json
{
  "mcpServers": {
    "rds_mysql": {
      "command": "uv",
      "args": [
        "--directory",
        "/<path to mcp-servers>/mcp/server/mcp_server_rds_mysql/src/mcp_server_rds_mysql",
        "run",
        "server.py"
      ],
      "transportType": "stdio",
      "env": {
        "ENDPOINT": "<ENDPOINT>",
        "REGION": "<REGION>",
        "VOLC_ACCESSKEY": "<VOLC_ACCESSKEY>",
        "VOLC_SECRETKEY": "<VOLC_SECRETKEY>",
        "PORT": "<PORT>"
      }
    }
  }
}
```

## License
MIT
