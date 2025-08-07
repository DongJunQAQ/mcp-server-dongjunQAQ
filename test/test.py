from mcp_server_dongjunqaq import tools
from src.mcp_server_dongjunqaq import mcp

print(tools.get_platform_info())
print(tools.get_env("name"))
mcp.run(transport="streamable-http")  # 在本地开发调试时使用
