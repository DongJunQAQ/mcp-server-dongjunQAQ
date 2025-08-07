# MCP-Server-DongJunQAQ
## 可用工具：

- get_platform_info - 获取平台的相关信息（如操作系统版本、CPU类型、总内存容量等等）；

- get_env - 获取系统中指定环境变量的值；

  必填参数：

  ​    key：环境变量的键

- get_compress_format - 获取该MCP Server所支持的压缩格式；

- make_archive - 打包并压缩指定目录或是单个文件；

  必填参数：

  ​    src：需要打包的文件或目录

  ​    compress_format：压缩格式

  ​    

## 配置：

为`Cherry Studio`进行配置，添加以下内容到你的Cherry Studio设置中，使用`uvx`（推荐）进行配置：

```json
{
  "mcpServers": {
    "MCP-Server-DongJunQAQ": {
      "registryUrl": "http://mirrors.aliyun.com/pypi/simple/",
      "command": "uvx",
      "args": ["mcp-server-dongjunqaq"]
    }
  }
}
```

当使用 `uv` 时无需进行特定安装，我们将使用 `uvx` 直接运行MCP-Server-DongJunQAQ。