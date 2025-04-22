# MCP Server CloudSearch
| 版本 | v1                                          |
|:---|:--------------------------------------------|
| 描述 | 云搜索服务（Cloud Search）是火山引擎提供的全托管一站式信息检索和分析平台  |
| 分类 | 数据库                                         |
| 标签 | ES，Elasticsearch，OpenSearch，搜索              |

## Tools
本 MCP Server 产品提供以下 Tools (工具/能力):
### 1. cloudsearch_describe_zones
查询云搜索服务在指定区域下的可用区列表
- 参数:
  - `region_id`: 地域 id

### 2. cloudsearch_describe_instance
查询云搜索服务在指定区域下的实例详细信息
- 参数:
  - `region_id`: 地域 id
  - `instance_id`: 实例 id

### 3. cloudsearch_describe_instances
查询云搜索服务在指定区域下的实例列表
- 参数:
  - `region_id`: 地域 id
  - `zone_id`: 可用区 id, 支持模糊查询
  - `instance_id`: 实例 id, 支持模糊查询
  - `instance_name`: 实例名称, 支持模糊查询
  - `status`: 实例状态
  - `version`: 实例版本
  - `charge_type`: 计费类型
  - `project_name`: 项目名称
  - `page_number`: 分页页码
  - `page_size`: 分页大小

### 4. cloudsearch_describe_instance_nodes
查询云搜索服务在指定区域下的实例节点列表
- 参数:
  - `region_id`: 地域 id
  - `instance_id`: 实例 id

### 5. cloudsearch_describe_instance_plugins
查询云搜索服务在指定区域下的实例的插件列表
- 参数:
  - `region_id`: 地域 id
  - `instance_id`: 实例 id

## 可适配平台  
方舟，python，cursor

## 服务开通链接 (整体产品)
https://console.volcengine.com/es/region:es+cn-beijing/v2/create?projectName=default

## 安装部署  
从 [volcengine](https://www.volcengine.com/docs/6291/65568) 获取 ak/sk, 然后将 ak/sk 添加到 mcp server 配置中, 或者在工作目录下的 `.env` 文件中配置, 格式如下:
```shell
VOLC_ACCESSKEY=your_volcengine_ak
VOLC_SECRETKEY=your_volcengine_sk
```

## 使用 uv
添加以下配置到你的 mcp settings 文件中
```json
{
  "mcpServers": {
    "mcp-server-cloudsearch": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server.git#subdirectory=server/mcp_server_cloudsearch",
        "mcp-server-cloudsearch"
      ],
      "env": {
        "VOLC_ACCESSKEY": "your_volcengine_ak",
        "VOLC_SECRETKEY": "your_volcengine_sk"
      }
    }
  }
}
```
或者克隆仓库到本地, 从本地代码仓库中启动
```json
{
  "mcpServers": {
    "mcp-server-cloudsearch": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/src/mcp_server_cloudsearch",
        "run",
        "server.py"
      ],
      "env": {
        "VOLC_ACCESSKEY": "your_volcengine_ak",
        "VOLC_SECRETKEY": "your_volcengine_sk"
      }
    }
  }
}
```

## License
[MIT](https://github.com/volcengine/mcp-server/blob/main/LICENSE)