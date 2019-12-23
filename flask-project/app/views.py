""" 视图 """

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
