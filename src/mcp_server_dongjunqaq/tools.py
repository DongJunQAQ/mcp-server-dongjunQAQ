import os
import platform
import shutil

import psutil


def get_platform_info() -> dict:
    """获取平台的相关信息"""
    platform_info: dict[str:str] = {
        "操作系统": platform.system(),
        "系统发行版本": platform.release(),
        "系统版本信息": platform.version(),
        "平台网络名": platform.node(),
        "平台架构": platform.machine(),
        "CPU信息": platform.processor(),
        "总内存(GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),  # round(...,2)将一个数四舍五入并保留2位小数
    }
    return platform_info


def get_env(key: str) -> str:
    """获取指定环境变量的值"""
    path_env = os.getenv(key)
    return path_env


def get_compress_format() -> dict:
    """获取支持的压缩格式"""
    return {".zip": "zip", ".tar": "tar", ".gz.tar": "gztar", ".bz.tar": "bztar", ".xz.tar": "xztar"}


def make_archive(des: str, src: str, compress_format: str) -> str:
    """
    打包并压缩指定内容；
    :param des:打包后输出的文件名
    :param compress_format:压缩格式
    :param src:需要打包的文件或目录
    :return:打包后的文件名+压缩格式后缀名
    """
    shutil.make_archive(des, compress_format, src)
    return f'已打包为{des}.{compress_format}文件'

# 1.解包文件
# 2.研究下MCP中提示词的用法
