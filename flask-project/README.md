<!-- 项目的说明 -->

# Datebase

使用MongoDB存储数据，Flask应用通过MongoEngine与MongoDB交互。

## 安装MongoDB

可以参考官方[文档](https://docs.mongodb.com/manualtutorial)进行安装。

## 运行MongoDB

安装完成后，可以通过以下命令，启动或者关闭MongoDB：

```shell
sudo systemctl start mongodb
sudo systemctl stop mongodb
```

在终端中使用mongo命令打开MongoDB的控制台进行操作。为了方便操作数据库，可以安装第三方的控制台工具。推荐使用Robomongo开源免费的跨平台工具。

## 配置MongoDB

在工程中配置MongoDB，首先在`config.py`进行添加：

```python
MONGODB_SETTINGS = {'DB': 'todo_db'}
```

## 开发

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
