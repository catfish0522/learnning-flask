# Update Todo

实现了保存与展示 Todo 的功能，那如何控制 Todo 的完成与未完成的状态呢？

这时候就可以使用 status 标志位，0就是未完成，1就是完成，所以，更新它的值就可以了。

## 前端

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
</table>
```

修改了之前的展示表格，修改最后一列用于显示按钮，按钮要根据 todo 的状态进行显示。

## 后台

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
