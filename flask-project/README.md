<!-- 项目的说明 -->

# Save Todo

之前都是用`manage.py`脚本保存的todo，那如何在前端浏览器上添加呢？

- 使用表单接受输入，并传给Flask后台。
- Flask获取到前端来的数据，将数据保存到MongoDB中。

## 前端

现在`index.html`模板中，加入一个表单，可以输入的todo的内容：

```html
<form class="input-group" action="/add" method="POST">
    <input class="form-control" id="content" name="content" type="text" value="">
    <span class="input-group-btn">
        <button class="btn btn-primary" type="submit">Add</button>
    </span>
</form>
```

## 后台

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

运行项目，在浏览器中，添加一个todo，是不是很简单？
