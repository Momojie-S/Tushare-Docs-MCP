# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

Tushare Docs MCP Server 是一个 MCP (Model Context Protocol) 服务器，为 Claude 等 AI 工具提供 Tushare API 文档查询功能。Tushare 是获取中国股市数据的 Python 库。

## 架构

```
src/tushare_docs_mcp/
├── __init__.py      # 包导出
├── main.py          # CLI 入口，处理传输模式
├── tools.py         # 使用 FastMCP 定义 MCP 工具
└── docs/
    ├── tushare_basic.md           # 基础用法说明
    └── non-official/
        ├── catalog.md             # 文档目录索引
        └── {分类}/                 # 按数据类型组织
            └── {子分类}/
                └── {接口名}.md     # 单个接口文档
```

服务器使用 `mcp.server.FastMCP` 暴露三个工具：
- `tushare_basic`: 返回 Tushare 库基础用法
- `tushare_docs_catalog`: 返回完整文档目录
- `tushare_docs(docs_path)`: 按路径返回特定接口文档

文档路径使用空格分隔，例如：`"01_股票数据 01_基础数据 01_股票列表"`

## 常用命令

本项目使用 `uv` 作为包管理工具，所有命令需通过 `uv run` 执行。

### 运行服务器
```bash
# stdio 模式（用于 Claude Desktop/Code）
uv run python -m tushare_docs_mcp.main stdio

# HTTP 模式（默认端口 8888）
uv run python -m tushare_docs_mcp.main

# HTTP 模式指定端口
uv run python -m tushare_docs_mcp.main 8080
```

### 安装依赖
```bash
uv sync
```

### 构建发布包
```bash
uv run python -m build
```

### 上传到 PyPI
```bash
# 使用 .pypirc 中配置的 repository
uv run twine upload dist/* --repository tushare-docs-mcp
```

### 代码检查
```bash
uv run ruff check src/
```

## 环境要求

- Python >= 3.11
- uv 包管理器
- 使用 `importlib.resources` 访问打包的文档文件
