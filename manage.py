from flask_migrate import MigrateCommand
from flask_script import Manager

from app import app
from app.service.commands.init_db import DatabaseInitializeCommand

manager = Manager(app)

manager.add_command('init_db', DatabaseInitializeCommand)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
