---
description: 
alwaysApply: true
---
# task

这是一项非常冗长的任务，建议您充分利用完整的输出上下文来处理——整体输入和输出 tokens 控制在 200k tokens，充分利用上下文窗口长度将任务彻底完成，避免耗尽 tokens。

# CLAUDE.md

LLM 学习与实验项目。

## 环境

- Python 3.14 | 虚拟环境: `.venv/` | 运行: `python main.py` 或 `.venv/bin/python main.py`

## 目录结构

```
.
├── main.py              # 主入口
├── helper_functions.py  # LLM 工具函数（GLM/豆包）
├── dir_functions.py      # 目录操作函数
├── deeplearning_ai.ipynb # Jupyter 学习笔记
├── txt/                  # 示例文本文件
├── .env                  # 环境变量（API 密钥）
└── .venv/                # Python 虚拟环境
```

## 代码规范

- 入口使用 `if __name__ == "__main__":` + `main()` 函数
- 函数命名: snake_case
- 添加适当 docstring

## 依赖

- `openai` - OpenAI API 客户端
- `python-dotenv` - 环境变量管理

## LLM 工具函数

| 函数 | 说明 |
|------|------|
| `get_llm_response_glm(prompt)` | 调用 GLM 模型 |
| `print_llm_response_glm(prompt)` | 调用并打印 GLM |
| `get_llm_response_doubao(prompt)` | 调用豆包模型 |
| `print_llm_response_doubao(prompt)` | 调用并打印豆包 |
| `get_chat_completion(prompt, history)` | 支持历史的补全 |

## 环境变量 (.env)

- `ARK_API_KEY` - API 密钥
- `ARK_BASE_URL` - API 基础 URL
- `ARK_MODEL` - 豆包模型名称
- `GLM_MODEL` - GLM 模型名称
