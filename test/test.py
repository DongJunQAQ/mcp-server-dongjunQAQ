from mcp_server_dongjunqaq import tools


def test_get_platform_info():
    print(tools.get_platform_info())


def test_get_env():
    print(tools.get_env("Path"))


def test_decompress():
    print(tools.decompress("C:\\Users\\2222\Videos\Captures\文件一.zip"))


def test_download_video():
    url = "https://www.bilibili.com/video/BV1RTtczyETu/"
    print(tools.download_video(url))


# test_get_platform_info()
# test_get_env()
test_decompress()
# test_download_video()
