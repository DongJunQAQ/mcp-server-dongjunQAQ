from mcp_server_dongjunqaq import get_platform_info
from src.mcp_server_dongjunqaq import mcp

print(get_platform_info())
mcp.run(transport="streamable-http")  # 在本地开发调试时使用
