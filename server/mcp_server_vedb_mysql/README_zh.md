# veDB MySQL MCP Server

这个MCP服务器提供了一个工具，用于与火山引擎（VolcEngine）的veDB MySQL服务进行交互，允许您从您的数据集中搜索和检索知识。

## 功能

- list_vedb_mysql_instances
> 用于获取用户的veDB MySQL实例列表，包括实例ID，以及实例的基本信息
- describe_vedb_mysql_detail
> 用于获取指定实例的实例详情
- list_vedb_mysql_instance_databases
> 用于获取指定实例中数据库列表，包括数据库的权限信息
- list_vedb_mysql_instance_accounts
> 用于获取指定实例中账号信息，包括账号的权限详情
- modify_vedb_mysql_instance_alias
> 用于更新指定实例的别名

## 安装部署

### 系统依赖

- Python 3.10 or higher
- API credentials (AK/SK)

### 安装

1. Install the package:

```bash
pip install -e .
```

Or with uv (recommended):

```bash
uv pip install -e .
```

### 配置

MCP server 依赖的环境变量:

- `VOLC_ACCESSKEY`: Your VolcEngine access key
- `VOLC_SECRETKEY`: Your VolcEngine secret key
- `REGION`: Your VolcEngine region (e.g., "cn-beijing")

可选的环境变量:

- `PORT`: Port for the FastMCP server (default: 8000)

## 使用

### 运行 MCP Server

```bash
python -m mcp_server_vedb_mysql.server --transport stdio
```

Or:

```bash
python -m mcp_server_vedb_mysql.server --transport sse
```

## MCP 集成配置

要将此服务器添加到您的MCP配置中，并将以下内容添加到您的MCP配置文件中:

```json
{
   "mcpServers": {
      "vedb_mysql": {
         "command": "uvx",
         "args": [
            "--from",
            "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_vedb_mysql",
            "mcp-server-vedb-mysql"
         ],
         "env": {
            "VOLC_ACCESSKEY": "your-access-key",
            "VOLC_SECRETKEY": "your-secret-key",
            "REGION": "<REGION>",
            "PORT": "<PORT>",
            "ENDPOINT": "<ENDPOINT>"
         }
      }
   }
}
```

## 问题排除

### 常见问题

1. **鉴权错误**
   - 请确认 AK/SK 的准确性 
   - 请确认您有权限访问相关的数据

2. **连接超时**
   - 请确认您可以正常访问 VolcEngine API
   - 请确认 host configuration 的正确性

3. **输出为空**
   - 请确认输入参数是否正确
   - 您可以扩大查询范围或者减少过滤条件

### 日志

该服务器默认使用 Python 的日志记录模块，日志级别为 INFO。在运行服务器时，您可以在 “/tmp/mcp.vedbmysql.log” 文件中查看详细的日志信息


## License

[MIT](https://github.com/volcengine/mcp-server/blob/main/LICENSE)
