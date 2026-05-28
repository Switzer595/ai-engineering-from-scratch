# pyproject.toml Notes

`pyproject.toml` 是 Python 项目的配置文件，用来记录项目名称、Python 版本要求、依赖包等信息。

## dependencies

`dependencies` 用来记录项目运行时必须安装的基础依赖，例如：

- numpy
- pandas
- matplotlib
- scikit-learn

这些依赖是项目正常运行所需要的。

## optional-dependencies

`optional-dependencies` 用来记录可选依赖。

例如，有些项目只有在训练模型时才需要 PyTorch，只有调用大模型 API 时才需要 openai、anthropic 或其他 SDK。

示例：

```toml
[project.optional-dependencies]
torch = ["torch"]
llm = ["openai"]