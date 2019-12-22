# learnning-flask

用于学习 Flask 的 Git 仓库

<!-- TOC -->
- [learnning-flask](#learnning-flask)
  - [About Flask](#about-flask)
  - [Hello World](#hello-world)

## About Flask

Flask是一个微内核的Web开发框架。

Flask主要依赖两个库：

- [Jinja2](https://palletsprojects.com/p/jinja/)，模板引擎。
- [Werkzeug](https://palletsprojects.com/p/werkzeug/)，一个WSGI套件。

如何理解微内核呢？文档里是这样说的：
> The "micro" in microframework means Flask aims to keep the core simple but extensible.

内核精简，易于扩展，功能不失强大。

## Hello World

从Hello World开始Flask之旅

创建`app.py`文件：

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
```

这就是一个最简单的Flask应用。

尝试运行它，然后通过浏览器进行访问：

```shell
python app.py
```

此时，只要访问`http://127.0.0.1:5000/`，就可以看到Hello World。

那这些代码都做了什么呢？

1. 导入Flask类，使用这个类可以创建应用。
2. 创建app，也就是一个Flask应用实例。
3. 创建index方法，使用app.route装饰器绑定路由规则，当访问`http://127.0.0.1:5000/`时，运行该方法，这样就可以在浏览器上看到了返回结果Hello World。
4. 运行Flask应用。
