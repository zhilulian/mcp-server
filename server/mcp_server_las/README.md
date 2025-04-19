#MCP Server 产品名称：AI数据湖服务LAS
[![产品Logo](las-logo.svg)]

## 版本信息

v1

## 产品描述

###短描述（建议20个字）
[LAS提供多模态数据集管理及清洗能力。]

### 长描述（建议50字，不超过100字）

[AI多模态数据湖服务LAS，提供多模态数据集的创建、预览、查询分析、编辑和清洗加工能力。]

## 分类

[大数据-数据中台]

## 标签

[多模态数据，数据集，数据湖，数据清洗]

## Tools

本 MCP Server 产品提供以下 Tools (工具/能力):

### Tool 1: 获取数据集详情

#### 类型

saas

#### 详细描述

获取数据集详细信息，包括大小，总行数，表结构schema等信息

#### 调试所需的输入参数:

输入：

```json
{
    "inputSchema": {
      "type": "object",
      "required": ["dataset_id"],
      "properties": {
        "dataset_id": {
          "description": "数据集id",
          "type": "string"
        }
      }
    },
    "name": "get_dataset_info",
    "description": "获取数据集详细信息，包括大小，总行数，表结构schema等信息"
}
```

输出：

- 输出结果描述
- 当前数据集id对应的数据集信息

#### 最容易被唤起的 Prompt示例

LAS中这是一个什么数据集

### Tool 2: 查询数据集

#### 类型

saas

#### 详细描述

检索数据集，通过query，检索匹配名称的数据集

#### 调试所需的输入参数:

输入：

```json
{
    "inputSchema": {
      "type": "object",
      "required": ["query"],
      "properties": {
        "query": {
          "description": "检索内容",
          "type": "string"
        }
      }
    },
    "name": "search_dataset",
    "description": "检索数据集，通过query，检索匹配名称的数据集"
}
```

输出：

- 输出结果描述
- 匹配query的数据集基本信息list

#### 最容易被唤起的 Prompt示例

LAS中，有哪些关于 image 的数据集

### Tool 3: 检索数据集数据项

#### 类型

saas

#### 详细描述

通过query，检索特定数据集中的内容，将数据项检索出来

#### 调试所需的输入参数:

输入：

```json
{
    "inputSchema": {
      "type": "object",
      "required": ["query"],
      "properties": {
        "query": {
          "description": "检索内容",
          "type": "string"
        }
      }
    },
    "name": "search_dataset_item",
    "description": "通过query，检索特定数据集中的内容，将数据项检索出来"
}
```

输出：

- 输出结果描述
- 匹配query的数据集数据内容数据项list

#### 最容易被唤起的 Prompt示例

LAS中，数据集中关于 RAY 相关的内容有哪些

## 可适配平台

方舟，python，cursor， Claude Desktop

## 服务开通链接 (整体产品)

[请在此处填写该 MCP Server 产品的整体服务开通链接]

## 鉴权方式

火山引擎AKSK鉴权体系

## 安装部署

[请在此处提供详细的安装和部署说明，根据您的产品特性选择合适的描述方式。]
[示例如下]

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *mcp-server-las*.

### Using PIP

Alternatively you can install `mcp-server-git` via pip:

```
pip install mcp-server-las
```

After installation, you can run it as a script using:

```
python -m mcp_server_las
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

## 资源列表 - optional

## 商业化 - optional

## 产品截图/视频 - optional

### Cursor

## 部署

[常见的部署方式，例如docker和uvx]
[示例如下]

### UVX

```json
{
    "mcpServers": {
        "las-dataset-mcp": {
            "command": "uvx",
            "args": [
            "--from",
            "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_las",
            "mcp-server-las"
          ],
            "env": {
                "VOLC_ACCESSKEY": "your-access-key-id",
                "VOLC_SECRETKEY": "your-access-key-secret",
                "LAS_DATASET_ID": "your-dataset-id"
            }
        }
    }
}
```

## License

MIT
