""" 脚本，比如启动服务器，与数据库交互 """

from flask_script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("runserver", Server(host='127.0.0.1', port=5000, use_debugger=True))

if __name__ == "__main__":
    manager.run()
