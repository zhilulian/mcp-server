"""
MCP ECS Server.

This server provides MCP tools to interact with ECS OpenAPI.
"""

import argparse
from mcp_server_ecs.tools.server import MCP
from mcp_server_ecs.tools import instance, region, event
from mcp_server_ecs.common.logs import LOG


def main():
    parser = argparse.ArgumentParser(description="Run the ECS MCP Server")
    parser.add_argument(
        "--transport",
        "-t",
        choices=["sse", "stdio"],
        default="stdio",
        help="Transport protocol to use (sse or stdio)",
    )

    args = parser.parse_args()

    # Run the MCP server
    LOG.info("Starting ECS MCP Server with %s transport", args.transport)

    MCP.run(transport=args.transport)


if __name__ == "__main__":
    main()
