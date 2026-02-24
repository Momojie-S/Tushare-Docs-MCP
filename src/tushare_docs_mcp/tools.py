from functools import lru_cache
from importlib import resources

from mcp.server import FastMCP

# Create an MCP server
mcp = FastMCP("tushare-docs-mcp")

# 缓存基础路径，避免重复调用 resources.files()
_DOCS_ROOT = resources.files("tushare_docs_mcp") / "docs"
_NON_OFFICIAL_ROOT = _DOCS_ROOT / "non-official"


@lru_cache(maxsize=1)
def _read_basic() -> str:
    """读取基础用法文档（带缓存）"""
    return (_DOCS_ROOT / "tushare_basic.md").read_text(encoding="utf-8")


@lru_cache(maxsize=1)
def _read_catalog() -> str:
    """读取文档目录（带缓存）"""
    return (_NON_OFFICIAL_ROOT / "catalog.md").read_text(encoding="utf-8")


@lru_cache(maxsize=256)
def _read_doc(docs_path: str) -> str:
    """读取指定文档（带缓存）"""
    docs_arr = docs_path.split(" ")
    docs_arr[-1] = f"{docs_arr[-1]}.md"

    ref = _NON_OFFICIAL_ROOT
    for docs_sub_path in docs_arr:
        ref = ref / docs_sub_path

    if not ref.is_file():
        return f"{docs_path} not found"
    return ref.read_text(encoding="utf-8")


@mcp.tool()
def tushare_basic() -> str:
    """
    获取tushare库的基础用法说明
    Returns:
        str: markdown格式的说明文档
    """
    return _read_basic()


@mcp.tool()
def tushare_docs_catalog() -> str:
    """
    获取tushare库的接口文档目录
    Returns:
        str: markdown格式的目录
    """
    return _read_catalog()


@mcp.tool()
def tushare_docs(docs_path: str) -> str:
    """
    获取tushare库特定接口的文档
    Args:
        docs_path (str): 文档路径，目录间使用空格分隔，从 tushare_docs_catalog 获取。例子： "01_股票数据 01_基础数据 01_股票列表"
    Returns:
        str: markdown格式的接口文档
    """
    return _read_doc(docs_path)
