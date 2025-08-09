from mcp_server_dongjunqaq import tools


def test_get_platform_info():
    print(tools.get_platform_info())


def test_get_env():
    print(tools.get_env("Path"))


def test_decompress():
    print(tools.decompress("E:\新建文件夹\myfile.zip"))


def test_download_video():
    url = "https://www.bilibili.com/video/BV1RTtczyETu/"
    print(tools.download_video(url))


def test_query_command():
    # require = "创建one/two/san目录"
    require = "查找用户家目录下Downloads目录中t开头的文件"
    print(tools.query_command(require))


# test_get_platform_info()
# test_get_env()
# test_decompress()
# test_download_video()
test_query_command()
