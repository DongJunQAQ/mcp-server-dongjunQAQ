from mcp.server.fastmcp import FastMCP

my_mcp = FastMCP("mcp-server-DongJunQAQ")  # 创建MCP Server并命名


def main() -> None:
    my_mcp.run(transport="stdio")  # 使用stdio的方式运行该MCP Server
