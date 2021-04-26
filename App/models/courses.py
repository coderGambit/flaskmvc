from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime
from .courses import *
from .user import *
from .jobs import *
from .coursejobs import *

class Courses (db.Model):
    courseID = db.Column(db.Integer, primary_key=True)
    id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
    courseName = db.Column(db.String(80), nullable=True)
    courseDescription = db.Column(db.String(1000), nullable=True)
    skills = db.Column(db.String(100), nullable=True)

    def toDict(self):
        return{
            'courseID': self.courseID,
            'courseName': self.courseName,
            'courseDescription': self.courseDescription,
            'skills': self.skills
            }