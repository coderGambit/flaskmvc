from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime
from .user import *
from .jobs import *

class Courses (db.Model):
    courseID = db.Column(db.Integer, primary_key=True)
    id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
    jobID = db.Column('jobID', db.Integer, db.ForeignKey('jobs.jobID'))
    courseName = db.Column(db.String(80), nullable=True)
    courseDescription = db.Column(db.String(1000), nullable=True)
    skills = db.Column(db.String(100), nullable=True)
    jobs = db.relationship('Jobs')
    def toDict(self):
        return{
            'courseID': self.courseID,
            'courseName': self.courseName,
            'courseDescription': self.courseDescription,
            'skills': self.skills,
            'jobinfo':self.jobs.toDict()
            }