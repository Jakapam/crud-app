from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    questions = relationship("Question", back_populates="user")
    tokens = relationship("Token", back_populates="user")
    responses = relationship("Response", back_populates="user")


    def __repr__(self):
        return '<User %r>' % self.username

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="questions")
    
class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    responses = relationship("Response", back_populates="token")

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(ENUM('yes', 'no', name="response_answer"), unique=False,nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="responses")
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship("Question", back_populates="questions")
    token_id = Column(Integer, ForeignKey('token.id'))
    token = relationship("Token", back_populates="responses")