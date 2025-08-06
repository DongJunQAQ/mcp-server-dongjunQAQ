import platform

from src.mcp_server_dongjunqaq import my_mcp


@my_mcp.tool()
def get_info() -> dict:
    """获取运行设备的相关信息"""
    host_info: dict[str:str] = {
        "system": platform.system(),
        "release": platform.release()
    }
    return host_info
