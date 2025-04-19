# veFaaS Sandbox MCP Server

## Introduction

A basic implementation of a veFaaS Sandbox MCP Server

## Architecture

```
Client --> MCP Server --> Sandbox MCP Service --> K8s Pod (veFaaS SandboxFusion)
                                                     |
                                                     |-- veFaaS: request & Pod 管理
```

## Prerequisites

Python >= 3.10

## Quick Start With 5ire Client

1. Download 5ire locally
2. Configure the service provider API information in the settings
3. Create a new tool and set this Sandbox MCP server Python script startup command
4. Start a conversation, enter a keyword, and the tool will automatically call the sandbox MCP server