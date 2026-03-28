# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个用于学习和实验的 Python 项目，主要包含 LLM (大语言模型) 相关的工具函数和示例代码。

## 环境

- Python 3.14
- 虚拟环境: `.venv/`
- 运行脚本: `python main.py` 或 `.venv/bin/python main.py`

## 项目结构

```
.
├── main.py              # 主入口文件
├── helper_functions.py  # LLM 工具函数库
├── deeplearning_ai.ipynb # Jupyter Notebook 学习笔记
├── README.md            # 项目说明
├── .env                 # 环境变量配置 (API 密钥等)
└── .venv/               # Python 虚拟环境
```

## 代码风格

- 使用 `if __name__ == "__main__":` 保护语句配合 `main()` 函数作为入口点
- 函数使用 snake_case 命名
- 添加适当的文档字符串 (docstring)

## 依赖

主要依赖:
- `openai` - OpenAI API 客户端
- `python-dotenv` - 环境变量管理

## 主要功能模块

### helper_functions.py

提供与 LLM 交互的工具函数:

- `get_llm_response_glm(prompt)` - 调用 GLM 模型获取响应
- `print_llm_response_glm(prompt)` - 调用 GLM 模型并打印响应
- `get_llm_response_doubao(prompt)` - 调用豆包模型获取响应
- `print_llm_response_doubao(prompt)` - 调用豆包模型并打印响应
- `get_chat_completion(prompt, history)` - 支持对话历史的补全

### 环境变量配置

需要在 `.env` 文件中配置以下变量:
- `ARK_API_KEY` - API 密钥
- `ARK_BASE_URL` - API 基础 URL
- `ARK_MODEL` - 豆包模型名称
- `GLM_MODEL` - GLM 模型名称
