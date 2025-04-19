# Volcengine ECS Model Context Protocol Server

The MCP server implementation for Product information from ECS.

## Version
v0.1.0

## Structure

The structure is as followed:
```
mcp_server_ecs/
├── src/
│   ├── common/                 # common utils
│   ├── conf/                   # config file
│   └── tools/                  # mcp tools + prompts
│       ├── __init__.py
│       ├── server.py           # init mcp server
│       ├── instance.py         
│       ├── instance_prompts.py 
│       ├── reigon.py           
│       ├── reigon_prompts.py   
│       ├── event.py            
│       └── event_prompts.py    
├── pyproject.toml              # dependencies
├── README.md                   # readme
└── uv.lock                     # lock file
```

## Configuration

### Run with uvx

```json
{
    "mcpServers": {
        "mcp-server-ecs": {
            "command": "uvx",
            "args": [
            "--from",
            "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_ecs",
            "mcp-server-ecs"
          ],
            "env": {
                "VOLC_ACCESSKEY": "YOUR_VOLC_ACCESSKEY",
                "VOLC_SECRETKEY": "YOUR_VOLC_SECRETKEY",
                "VOLC_REGION": "YOUR_VOLC_REGION",
                "FASTMCP_PORT": "YOUR_MCP_SERVER_PORT"
            }
        }
    }
}
```

## Tool Description
| Tool Name                   | Description                 |
|-----------------------------|---------------------------- |
| DescribeInstances           | 查询实例列表                  |
| DescribeImages              | 查询镜像列表                  |
| DescribeInstanceTypes       | 查询实例规格列表               |
| DescribeAvailableResource   | 查询可用资源列表               |
| DescribeRegions             | 查询地域列表                  |
| DescribeZones               | 查询可用区列表                |
| DescribeSystemEvents        | 查询系统事件列表               |

