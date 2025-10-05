import sys
from tushare_docs_mcp.tools import mcp


def main():
    """
    启动 Tushare Docs MCP 服务器
    支持不同的传输方式:
    - 不带参数或指定 http: 使用 HTTP 传输
    - 指定 stdio: 使用标准输入输出传输
    """
    if len(sys.argv) > 1 and sys.argv[1] == "stdio":
        # 使用 stdio 传输，适用于 Claude 等工具
        mcp.run(transport="stdio")
    else:
        # 默认使用 HTTP 传输，支持指定端口
        port = 3000  # 默认端口
        if len(sys.argv) > 1 and sys.argv[1].isdigit():
            port = int(sys.argv[1])
        elif len(sys.argv) > 2 and sys.argv[2].isdigit():
            port = int(sys.argv[2])

        mcp.settings.port = 8888
        mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()