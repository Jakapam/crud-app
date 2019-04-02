import os
import sys
from flask_script import Manager,prompt, prompt_pass
from flask_migrate import Migrate, MigrateCommand
from config import DevelopmentConfig
from app import app, db
from models import User, Question, Token, Modifier, Response

app.config.from_object(DevelopmentConfig)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def createadminuser():
    username = prompt('Username')
    email = prompt('E-Mail')

    password = prompt_pass('User password')
    password_confirm = prompt_pass('Confirmed password')

    if not password == password_confirm:
        sys.exit('\nCould not create user: Passwords did not match')
    user = User(username=username, email=email, is_admin=True)
    user.set_password(password)
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        app.logging.error("Error creating user: {}".format(e))

    app.logging.info("Admin '{}' created".format(username))

if __name__ == '__main__':
    manager.run()