from app import db, app
# from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship, backref
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    responses = relationship("Response", back_populates="user")
    password_digest = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_digest = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_digest, password)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), unique=False, nullable=False)
    modifiers = relationship("Modifier", back_populates="question")
    responses = relationship("Response", back_populates="question")

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    modifiers = relationship("Modifier", back_populates="token")

class Modifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    yes_modifier= db.Column(db.Integer, unique=False, nullable=False)
    no_modifier= db.Column(db.Integer, unique=False, nullable=False)
    token_id= db.Column(db.Integer, db.ForeignKey('token.id'))
    token = relationship("Token", back_populates="modifiers")
    question_id= db.Column(db.Integer, db.ForeignKey('question.id'))
    question = relationship("Question", back_populates="modifiers")

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(ENUM('yes', 'no', name="response_answer"), unique=False,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship(User, back_populates="responses")
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    question = relationship("Question", back_populates="responses")
    