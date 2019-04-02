import os
import sys
from flask_script import Manager,prompt, prompt_pass
from flask_migrate import Migrate, MigrateCommand
from config import DevelopmentConfig
from app import app, db
from models import User, Question, Token, Modifier, Response

import pdb

app.config.from_object(DevelopmentConfig)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def shell():
    pdb.set_trace()

@manager.command
def createadminuser():
    username = prompt('Username')
    email = prompt('E-Mail')

    password = prompt_pass('User password')
    password_confirm = prompt_pass('Confirm password')

    if not password == password_confirm:
        sys.exit('\nCould not create user: Passwords did not match')
    user = User(username=username, email=email, is_admin=True)
    user.set_password(password)
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        app.logger.error("Error creating user: {}".format(e))

    app.logger.info("Admin '{}' created".format(username))

@manager.command
def mockdata():

    user = User(
        username = "User1",
        email = "email@email.com",
        is_admin = False, 
    )

    user.set_password("pass")

    question_cool = Question(
        body="Is it cool?"
    )

    question_neat = Question(
        body="Is this neat?"
    )

    token_cool = Token(name="cool")
    token_neat = Token(name="neat")

    mod_cool = Modifier(
        yes_modifier = 1,
        no_modifier = -1,
        token = token_cool,
        question = question_cool
    )

    mod_neat = Modifier(
        yes_modifier = 1,
        no_modifier = -1,
        token = token_neat,
        question = question_neat
    )

    resp_yes_neat = Response(
        user = user,
        answer = "yes",
        question = question_neat
    )

    resp_no_cool = Response(
        user = user,
        answer = "no",
        question = question_cool
    )

    data = [ user, question_cool, question_neat, token_cool, token_neat, mod_cool, mod_neat, resp_no_cool, resp_yes_neat ]
    app.logger.info("Inserting mock data...")
    for datum in data:
        db.session.add(datum)

    db.session.commit()
    app.logger.info("Mock data inserted")

if __name__ == '__main__':
    manager.run()