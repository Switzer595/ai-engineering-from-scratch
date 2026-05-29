# Editor Setup Notes

## Installed Extensions

- Python
- Pylance
- Jupyter
- Black Formatter
- GitLens
- Remote - SSH

## VS Code Settings

已配置：

- Python type checking: basic
- Format on save
- Rulers: 88, 120
- Notebook output scrolling
- Auto save
- PowerShell terminal integration

## Pylance and Black Test

已创建 `format_test.py`，用于测试：

- 保存时自动格式化 Python 代码
- Pylance 类型检查提示

## Remote SSH

Remote SSH 用于通过本地 VS Code 连接远程 GPU 服务器，并像编辑本地文件一样编辑远程文件。

当前没有可用远程 GPU 服务器，因此本练习只学习概念，不进行实际连接。

以后需要准备：

- 服务器 IP
- 用户名
- SSH key 或密码