<!-- 项目的说明 -->

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
