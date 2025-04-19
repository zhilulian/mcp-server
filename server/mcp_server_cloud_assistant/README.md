#MCP Server 产品名称：[云助手 MCP Server]

## 版本信息
v0.1.0

## 产品描述
自然语言驱动向云服务器实例发送和执行自定义命令

### 长描述（建议50字，不超过100字）
云助手的 MCP Server 实现，可以自然语言驱动向云服务器实例发送和执行自定义命令，适用于ECS带内运维、故障排查、环境检测、软件管理等场景。支持Linux 和 Windows 操作系统。


## 分类
计算

## 标签
命令执行、带内运维

## Tools
本 MCP Server 产品提供以下 Tools (工具/能力):
### Tool 1: RunCommand

#### 类型
saas

#### 详细描述
向目标实例发送命令，生成一条执行记录，等待执行完成，然后检索并返回执行结果。
**_RunCommand工具提供命令执行的通道，执行模型生成的命令_**。

#### 调试所需的输入参数:
- 输入：
  - instance: 实例名称
  - region: 实例所在地域，默认cn-beijing，支持cn-shanghai、cn-guangzhou、ap-southeast-1等
  - command_content: 执行命令内容
- 输出：
  - 命令的执行输出结果
#### 最容易被唤起的 Prompt示例
1. 查询cn-beijing地域下实例i-ydtoqt4pogh9l3bp82xx的操作系统信息
2. 查看实例i-ydtoqt4pogh9l3bp82xx的CPU使用情况

## 可适配平台  
方舟、cursor、claude

## 服务开通链接 (整体产品)  
服务类产品，无需开通

## 鉴权方式  
[请在此处说明该 MCP Server 产品使用的鉴权方式。例如：API Key，OAuth 2.0，Token 等，并简要说明如何获取和使用凭证。]  
暂定

## 安装部署  
[示例如下]
### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *mcp-server-git*.

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
[示例如下]
### UV
```json
{
  "mcpServers": {
    "mcp_server_cloud_assistant": {
      "command": "uv",
      "env": {
        "VOLC_ENDPOINT":"Volcengine OpenApi Endpoint",
        "VOLC_ACCESSKEY":"Your Volcengine access key",
        "VOLC_SECRETKEY":"Your Volcengine secret key"
      },
      "args": [
        "--directory",
        "/<path to mcp-servers>/mcp-servers/src/mcp_server_cloud_assistant",
        "run",
        "mcp-server-cloud-assistant"
      ]
    }
  }
}
```
### UVX
```json
{
  "mcpServers": {
    "mcp_server_cloud_assistant": {
      "command": "uvx",
      "env": {
        "VOLC_ENDPOINT":"Volcengine OpenApi Endpoint",
        "VOLC_ACCESSKEY":"Your Volcengine access key",
        "VOLC_SECRETKEY":"Your Volcengine secret key"
      },
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server.git@feat/cloud_assistant#subdirectory=server/mcp_server_cloud_assistant",
        "mcp-server-cloud-assistant"
      ]
    }
  }
}
```

## License
MIT