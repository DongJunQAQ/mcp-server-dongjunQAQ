from mcp.server.fastmcp import FastMCP

import tools

mcp = FastMCP("mcp-server-DongJunQAQ")  # 创建MCP Server并命名
mcp.add_tool(tools.get_platform_info)  # 注册工具
mcp.add_tool(tools.get_env)


def main() -> None:
    mcp.run(transport="stdio")  # 使用stdio的方式运行该MCP Server
