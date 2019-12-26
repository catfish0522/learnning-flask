# Delete Todo

当完成一个 todo，想要删除它，那该如何实现呢?

- 前端每个 todo 后面都加一个删除按钮
- 后端响应前端，从数据库中删除 todo。

## 前端

上一小结已经加过按钮，删除按钮直接加在后面即可。

```html
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
                <a href="/delete/{{ t.id }}" class="btn btn-danger">Delete</a>
            </td>
        </tr>
    {% endfor %}
    </tbody>
```

## 后台

后台，添加删除方法，`views.py` 中：

```python
@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)
```

delete 方法会根据传来的 id，找到 todo，然后进行删除。