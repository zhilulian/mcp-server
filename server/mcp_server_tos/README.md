# MCP Server 产品名称： mcp-server-tos

![产品Logo](./static/image/TOS.svg)

## 版本信息

V0.1.0

## 产品描述

### 短描述

基于 MCP 管理 TOS 资源，智能化探索数据

### 长描述

TOS 官方推出的 MCP Server 提供强大的查询能力，支持通过自然语言便捷地探索和检索 TOS 中存储的内容，提升了数据访问的直观性与效率。可以与火山引擎云产品 MCP 组合，助力构建更智能的业务应用场景。

## 分类

云基础-存储

## 标签

搜索，视频，图片，文本, 对象存储

## Tools

本 MCP Server 产品提供以下 Tools (工具/能力):

### Tool 1: list_buckets

#### 类型

SaaS

#### 详细描述

该工具允许您便捷查看火山引擎TOS的存储桶列表。

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": [],
    "properties": {}
  },
  "name": "list_buckets",
  "description": "查询您账号下拥有的所有存储桶的列表。"
}

```

输出：
    - [参考文档](https://www.volcengine.com/docs/6349/74850)

#### 最容易被唤起的 Prompt示例

使用list_buckets tool工具帮我查询TOS桶列表

### Tool 2: list_objects

#### 类型

SaaS

#### 详细描述

该工具允许您便捷查看火山引擎TOS桶下的对象列表，每次请求都会返回存储桶中的部分或全部对象（最多 1000 个）。您可以使用请求参数作为选择条件，返回存储桶中对象的子集。

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": ["bucket"],
    "properties": {
      "bucket": {
        "type": "string",
        "description": "用户指定的存储桶名称"
      },
      "prefix": {
        "type": "string",
        "description": "可选的对象前缀"
      },
      "start_after": {
        "type": "string",
        "description": "列举对象的起始位置。您可以通过指定对象的起始位置分页列举对象"
      },
      "continuation_token": {
        "type": "string",
        "description": "指定列举操作从该 Token 开始，通常从上次请求返回的 NextContinuationToken 中获取此 Token"
      }
    }
  },
  "name": "list_objects",
  "description": "查询您指定存储桶的对象列表"
}

```

输出：
    - [参考文档](https://www.volcengine.com/docs/6349/357812)


#### 最容易被唤起的 Prompt示例

使用list_objects tool工具帮我查询example桶下的对象列表

### Tool 3: get_object tool

#### 类型

SaaS

#### 详细描述

从 TOS 检索对象，需要指定桶名和对象的完整路径。对于文本内容的对象，比如文本文件、CSV 文件等，该工具返回的是其内容。对于图片、视频等二进制对象，该工具返回的是Base64编码的内容。

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": [
      "bucket",
      "key"
    ],
    "properties": {
      "bucket": {
        "type": "string",
        "description": "用户指定的存储桶名称"
      },
      "key": {
        "type": "string",
        "description": "用户需要读取的对象名，需要指定完整的对象名"
      }
    }
  },
  "name": "get_object",
  "description": "获取指定对象的内容，对于文本内容的对象，比如文本文件、CSV 文件等，该工具返回的是其内容。对于图片、视频等二进制对象，该工具返回的是Base64编码的内容。"
}
```

输出：
    - [参考文档](https://www.volcengine.com/docs/6349/74856)

#### 最容易被唤起的 Prompt示例

使用get_object tool工具帮我读取example桶下的example.txt的文件内容

## 可适配平台
方舟

## 服务开通链接 (整体产品)

[开通tos服务](https://console.volcengine.com/tos), 未开通的用户会自动重定向到开通页. 如果已经开通,则会跳转首页

## 鉴权方式

API Key

### 操作步骤

```
mv .env_example .env
```

请在.env文件中设置相关环境变量

## 安装部署

### Run Locally

#### Option1

```json
{
  "mcpServers": {
    "tos-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/src/mcp_server_tos",
        "run",
        "mcp-server-tos"
      ]
    }
  }
}
```

#### Option2

```json
{
    "mcpServers": {
        "tos": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/volcengine/ai-app-lab#subdirectory=mcp/server/mcp_server_tos",
                "mcp-server-tos"
            ],
            "env": {
                "VOLC_ACCESSKEY": "your ak",
                "VOLC_SECRETKEY": "your sk",
                "REGION": "tos region",
                "TOS_ENDPOINT": "tos endpoint",
                "SECURITY_TOKEN": "your security token",
                "TOS_BUCKET": "your specific bucket"
            }
        }
    }
}
```

##在不同平台的配置

### 方舟

#### 体验中心

[示例如下]
1. 查看MCP Server 详情
在大模型生态广场，选择合适的MCP Server，并查看详情
2. 选择MCP Server即将运行的平台
检查当前MCP Server 已适配的平台，并选择合适的平台
3. 查看并对比可用的Tools
仔细查看可用的Tools的功能描述与所需的输入参数，并尝试运行对应的功能。
4. 获取专属的URL或代码示例
检查账号登录状态与服务开通情况，生成唯一URL
5. 去对应的Client的平台进行使用
点击快捷跳转按钮，前往方舟平台的体验中心进行对应MCP Server的体验

## License

see LICENSE


