# MCP Server 产品名称： mcp-server-tls

![产品Logo](./static/image/logo.svg)

## 版本信息

V0.1.0

## 产品描述

### 短描述

自然语言驱动日志分析新体验

### 长描述

日志服务官方推出的 MCP Server，可以将自然语言精准转化为日志分析语句，高效分析日志。操作便捷，上手快，适用于运维排查、数据分析等场景，为你轻松解锁日志服务的无限可能

## 分类

云基础-存储

## 标签

日志，可观测，数据飞轮

## Tools

本 MCP Server 产品提供以下 Tools (工具/能力):

### Tool 1: search_logs_v2_tool

#### 类型

SaaS

#### 详细描述

该工具允许您使用多种查询类型搜索日志，包括全文检索、键值搜索和SQL查询。它提供灵活的时间范围过滤和限制选项来定制搜索结果,默认时间为15分钟。

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": ["query"],
    "properties": {
      "query": {
        "type": "string",
        "description": "日志查询语句"
      },
      "topic_id": {
        "type": "string",
        "description": "可选的日志主题ID, 默认为环境变量中设置的topic_id,如果没有设置,则必传"
      },
      "start_time": {
        "type": "integer",
        "description": "查询起始时间，Unix 时间戳（秒/毫秒）"
      },
      "end_time": {
        "type": "integer",
        "description": "查询结束时间，Unix 时间戳（秒/毫秒）"
      },
      "limit": {
        "type": "integer",
        "description": "返回的最大日志条数，默认值为 10"
      }
    }
  },
  "name": "search_logs_v2",
  "description": "根据日志查询语句，在指定日志主题和时间范围内查询日志"
}

```

输出：
    - [参考文档](https://www.volcengine.com/docs/6470/112195)

#### 最容易被唤起的 Prompt示例

使用search_logs_v2_tool工具帮我查询下query为"__content__: error"的前十条日志

### Tool 2: text2sql

#### 类型

SaaS

#### 详细描述

将用户输入的查询语言转为TLS定义的SQL查询语句,如果查询语言比较模糊,可能会有询问.

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": ["question"],
    "properties": {
      "question": {
        "type": "string",
        "description": "用户输入的查询语言"
      },
      "topic_id": {
        "type": "string",
        "description": "可选的日志主题ID, 默认为环境变量中设置的topic_id,如果没有设置,则必传"
      },
      "session_id": {
        "type": "string",
        "description": "可选的tls copilot的会话id"
      },
    }
  },
  "name": "text2sql",
  "description": "将用户输入的查询语言转为TLS定义的SQL查询语句"
}

```

输出：

```json
{
    "answer": "ai给出的返回结果,包含推理过程",
    "Suggestions": ["ai返回的建议,比如查询字段不明确时,可能给出询问"],
    "session_id": "服务端返回的当前与tls copilot会话id"
}
```

#### 最容易被唤起的 Prompt示例

使用text2sql工具生成一个sql,用于查询__content__字段中包含error的日志数量

### Tool 3: describe_project_tool

#### 类型

SaaS

#### 详细描述

获取当前权限下指定项目id下的项目信息

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": [],
    "properties": {
      "project_id": {
        "type": "string",
        "description": "可选的日志项目ID, 默认为环境变量中设置的project_id,如果没有设置,则必传"
      },
    }
  },
  "name": "describe_project_tool",
  "description": "获取当前权限下指定项目id下的项目信息"
}
```

输出：
    - [参考文档](https://www.volcengine.com/docs/6470/112178)

#### 最容易被唤起的 Prompt示例

使用describe_project_tool工具帮我查下project_id为xxx的项目名是什么

### Tool 4: describe_projects_tool

#### 类型

SaaS

#### 详细描述

获取当前权限下的多个项目信息(限制10个)

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": [],
    "properties": {}
  },
  "name": "describe_projects_tool",
  "description": "获取当前权限下的多个项目信息(限制10个)"
}
```

输出：
    - [参考文档](https://www.volcengine.com/docs/6470/112179)

#### 最容易被唤起的 Prompt示例

使用describe_projects_tool工具帮我查下前十个项目名是什么

### Tool 5: describe_topic_tool

#### 类型

SaaS

#### 详细描述

获取当前权限下指定主题id的主题信息

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": [],
    "properties": {
      "topic_id": {
        "type": "string",
        "description": "可选的日志主题ID, 默认为环境变量中设置的topic_id,如果没有设置,则必传"
      },
    }
  },
  "name": "describe_topic_tool",
  "description": "获取当前权限下指定主题id的主题信息"
}
```

输出：
    - [参考文档](https://www.volcengine.com/docs/6470/112184)

#### 最容易被唤起的 Prompt示例

使用describe_topic_tool工具帮我查下当前主题的分片数量

### Tool 6: describe_topics_tool

#### 类型

SaaS

#### 详细描述

获取当前权限下指定项目ID的主题信息

#### 调试所需的输入参数:

输入：

```json
{
  "inputSchema": {
    "type": "object",
    "required": [],
    "properties": {
      "project_id": {
        "type": "string",
        "description": "可选的日志项目ID, 默认为环境变量中设置的project_id,如果没有设置,则必传"
      },
    }
  },
  "name": "describe_topics_tool",
  "description": "获取当前权限下指定project_id下的多个主题信息(限制10个)"
}
```

输出：
    - [参考文档](https://www.volcengine.com/docs/6470/112185)

#### 最容易被唤起的 Prompt示例

使用describe_topics_tool工具帮我查下当前项目下前10个项目的分区数量.

## 可适配平台
方舟

## 服务开通链接 (整体产品)

[开通tls服务](https://console.volcengine.com/tls), 未开通的用户会自动重定向到开通也. 如果已经开通,则会跳转首页

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
        "tls": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/src/mcp_server_tls",
                "run",
                "main.py"
            ]
        }
    }
}
```

#### Option2

```json
{
    "mcpServers": {
        "tls": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://git-repository#subdirectory=mcp/server/mcp_server_tls",
                "mcp-server-tls"
            ],
            "env": {
                "AK": "your ak",
                "SK": "your sk",
                "REGION": "your region",
                "ENDPOINT": "your endpoint",
                "ACCOUNT_ID": "your account id",
                "PROJECT_ID": "your project id",
                "TOPIC_ID": "your topic id"
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


