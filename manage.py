from app import create_app, db
from app.models import User, Role, Category, Pitch, Review
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server


app =  create_app('development')
# app =  create_app("management")

manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role, Category = Category, Pitch = Pitch, Review = Review)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()