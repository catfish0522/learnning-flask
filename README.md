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
  - [Datebase](#datebase)
    - [安装MongoDB](#%e5%ae%89%e8%a3%85mongodb)
    - [运行MongoDB](#%e8%bf%90%e8%a1%8cmongodb)
    - [配置MongoDB](#%e9%85%8d%e7%bd%aemongodb)
    - [开发](#%e5%bc%80%e5%8f%91)
  - [Get Todos](#get-todos)
    - [前端](#%e5%89%8d%e7%ab%af)
    - [后台](#%e5%90%8e%e5%8f%b0)
  - [Save Todo](#save-todo)
    - [前端](#%e5%89%8d%e7%ab%af-1)
    - [后台](#%e5%90%8e%e5%8f%b0-1)
  - [Update Todo](#update-todo)
    - [前端](#%e5%89%8d%e7%ab%af-2)

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

## Datebase

使用MongoDB存储数据，Flask应用通过MongoEngine与MongoDB交互。

### 安装MongoDB

可以参考官方[文档](https://docs.mongodb.com/manualtutorial)进行安装。

### 运行MongoDB

安装完成后，可以通过以下命令，启动或者关闭MongoDB：

```shell
sudo systemctl start mongodb
sudo systemctl stop mongodb
```

在终端中使用mongo命令打开MongoDB的控制台进行操作。为了方便操作数据库，可以安装第三方的控制台工具。推荐使用Robomongo开源免费的跨平台工具。

### 配置MongoDB

在工程中配置MongoDB，首先在`config.py`进行添加：

```python
MONGODB_SETTINGS = {'DB': 'todo_db'}
```

### 开发

在`__init__.py`中导入MongoEngine，并且实例化：

```python
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object("config")

db = MongoEngine(app)

from app import views, models
```

然后创建数据模型，用于映射MongoDB中的Document对象，在`models.py`中：

```python
import datetime
from app import db


class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)
```

比较简单，只有三个字段，分别表示：todo的内容，todo的发布时间，todo的完成状态。

在`manage.py`中加入数据库的命令：

```python
from flask_script import Manager, Server
from app import app
from app.models import Todo

manager = Manager(app)

manager.add_command("runserver",
    Server(host='127.0.0.1', port=5000, use_debugger=True))

@manager.command
def save_todo():
    todo = Todo(content="my fitst todo")
    todo.save()


if __name__ == "__main__":
    manager.run()
```

然后，在终端中运行：

```shell
sudo mongod
```

```shell
python manage.py save_todo
```

此时，使用Robomongo，就可以查看到插入的数据。

## Get Todos

使用`manage.py`插入几条todo，然后，实现在前端展示所有todo的功能。

### 前端

在模板中，使用表格展示所有的todo：

```html
<table class="table">
    <thead>
        <tr>
            <td>Conten</td>
            <td>Time</td>
            <td>Status</td>
        </tr>
    </thead>
    <tbody>
    {% for t in todos %}
        <tr>
            <td>{{ t.content }}</td>
            <td>{{ t.time }}</td>
            <td>{{ t.status }}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>
```

使用一个循环，输出了所有的todo。

### 后台

在`views.py`中，要从后台数据库获取所有的todo：

```python
from app import app
from flask import render_template
from app.models import Todo


@app.route('/')
def to_do():
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)
```

在`to_do`方法中：

- 获取所有的todo
- 返回模板和所有的todo

运行项目，在浏览器中就可以看到所有的todo。

## Save Todo

之前都是用`manage.py`脚本保存的todo，那如何在前端浏览器上添加呢？

- 使用表单接受输入，并传给Flask后台。
- Flask获取到前端来的数据，将数据保存到MongoDB中。

### 前端

现在`index.html`模板中，加入一个表单，可以输入的todo的内容：

```html
<form class="input-group" action="/add" method="POST">
    <input class="form-control" id="content" name="content" type="text" value="">
    <span class="input-group-btn">
        <button class="btn btn-primary" type="submit">Add</button>
    </span>
</form>
```

### 后台

然后在`views.py`中：

```python
from app import app
from flask import render_template, request
from app.models import Todo


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['post', ])
def add():
    content = request.form.get("content")
    todo = Todo(content=content)
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)
```

获取到数据，将数据保存。

运行项目，在浏览器中，添加一个 todo，是不是很简单？

## Update Todo

实现了保存与展示 Todo 的功能，那如何控制 Todo 的完成与未完成的状态呢？

这时候就可以使用 status 标志位，0就是未完成，1就是完成，所以，更新它的值就可以了。

### 前端

先在前端每条 todo 后，加入 do 和 undo 两个按钮：

- 如果 todo 的 status 未完成，则显示 do 按钮
- 如果 todo 的 status 已完成，则显示 undo 按钮

```html
<form class="input-group" action="/add" method="post">
    <input class="form-control" id="content" name="content" type="text" value="">
    <span class="input-group-btn">
        <button class="btn btn-primary" type="submit">Add</button>
    </span>
</form>


<table class="table">
    <thead>
        <tr>
            <th>Content</th>
            <th>Time</th>
            <th>Operation</th>
        </tr>
    </thead>
    <tbody>
    {% for t in todos %}
        <tr>
            <td>{{ t.content }}</td>
            <td>{{ t.time }}</td>
            <td>
            {% if t.status == 0 %}
            <a href="/done/{{ t.id }}" class="btn btn-primary">Done</a>
            {% else %}
            <a href="/undone/{{ t.id }}" class="btn btn-primary">Undone</a>
            {% endif%}
            </td>
        </tr>
    {% endfor %}
    </tbody>
</table>```

修改了之前的展示表格，修改最后一列用于显示按钮，按钮要根据 todo 的状态进行显示。

### 后台

前端写好后，开始添加后台的支持，在 `views.py` 中：

```python
from app import app
from flask import render_template, request
from app.models import Todo


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['post', ])
def add():
    content = request.form.get("content")
    todo = Todo(content=content)
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)


@app.route('/done/<string:todo_id>')
def done(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)


@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)
```

两个方法思路是一样的，从前端传来 todo 的 id，然后，根据 id 获取 todo 后更新 status。
