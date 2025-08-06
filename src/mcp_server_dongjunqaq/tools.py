import platform

from src.mcp_server_dongjunqaq import my_mcp


@my_mcp.tool()
def get_platform_info() -> dict:
    """获取平台的相关信息"""
    platform_info: dict[str:str] = {
        "system": platform.system(),
        "release": platform.release()
    }
    return platform_info
