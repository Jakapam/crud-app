from app import db, app
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship, backref
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    isAdmin = db.Column(db.Boolean, unique=False, nullable=False)
    questions = relationship("Question", back_populates="user")
    responses = relationship("Response", back_populates="user")
    password_digest = db.Column(db.String(128))

    def set_password(self, password):
        self.password_digest = bcrypt.generate_password_hash(password)
    
    def check_password(self, password):
        return bcrypt.check_password(self.password_digest, password)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="questions")
    modifiers = relationship("Modifier", back_populates="question")

class Modifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    yes_modifier: Column(Integer, nullable=False)
    no_modifier: Column(Integer, nullable=False)
    token_id: Column(Integer, ForeignKey('token.id'))
    token = relationship("Token", 
        backref=backref("modifiers", cascade="all, delete-orphan"))
    question_id: Column(Integer, ForeignKey('question.id'))
    question = relationship("Question",
        backref=backref("modifiers", cascade="all, delete-orphan"))

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    responses = relationship("Response", back_populates="token")
    modifiers = relationship("Modifier", back_populates="token")

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(ENUM('yes', 'no', name="response_answer"), unique=False,nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="responses")
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship("Question", back_populates="questions")
    