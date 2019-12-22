<!-- 项目的说明 -->

# 重新修改项目

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
