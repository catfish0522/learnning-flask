# learnning-flask

用于学习 Flask 的 Git 仓库

<!-- TOC -->
- [learnning-flask](#learnning-flask)
  - [About Flask](#about-flask)
  - [Hello World](#hello-world)
  - [Project](#project)
    - [Flask 工程结构](#flask-%e5%b7%a5%e7%a8%8b%e7%bb%93%e6%9e%84)
    - [安装依赖](#%e5%ae%89%e8%a3%85%e4%be%9d%e8%b5%96)
    - [重新修改项目](#%e9%87%8d%e6%96%b0%e4%bf%ae%e6%94%b9%e9%a1%b9%e7%9b%ae)

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

## Project

### Flask 工程结构

一个项目往往有很多文件，为了更好的对项目进行管理，同时也为了后期的扩展，需要好好设计一下工程的骨架结构。

``` shell
flask-project
├── app                         # app目录
│   ├── __init__.py             # 初始化app包
│   ├── models.py               # 数据模型
│   ├── static                  # 静态文件目录
│   │   ├── bootstrap.css       # 样式文件
│   │   └── index.css           # 样式文件
│   ├── templates               # 模板目录
│   │   └── index.html          # 模板文件
│   └── views.py                # 视图
├── config.py                   # 应用配置信息，比如数据库配置
├── manage.py                   # 脚本，比如启动服务器，与数据库交互
├── README.md                   # 项目的说明
├── requirenments.txt           # 添加项目的依赖
└── run.py                      # 项目运行脚本
```

使用app包来组织应用，前端使用Bootstrap，也加入进来。

### 安装依赖

首先，在 `requirenments.txt` 添加项目的依赖。

> Flask

> flask-mongoengine

> Flask-Script

然后使用pip安装这些依赖。

``` shell
sudo pip install -r requirenments.txt
```

### 重新修改项目

在这个项目中，实现Hello World。

在 `__init__.py` 中：

``` python
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

from app import views, models
```

此时，在app包中实例化Flask的应用，从 `config.py` 中加载配置。

在 `views.py` 中：

``` python
from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html", text="Hello New World")
```

此时，不是直接返回数据，而是通过模板渲染数据。

在 `index.html` 模板文件中，最终会通过 `{{}}` 将Hello World展示出来。__更多的展现方式参考[Jinja2](https://palletsprojects.com/p/jinja/)文档__

``` jinja
{{ text }}
```

然后，可以在Flask-Script中，运行项目。

往 `manage.py` 中，加入代码：

``` python
from flask_script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("runserver", Server(host='127.0.0.1', port=5000, use_debugger=True))

if __name__ == "__main__":
    manager.run()
```

此时，这样运行这个项目：

``` shell
python manage.py runserver
```

此时，又可以在浏览器中看到亲切的Hello World。
