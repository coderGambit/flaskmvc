from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime
from .courses import *
from .user import *
from .jobs import *
from .coursejobs import *

class CourseJobs (db.Model):
    courseID = db.Column('courseID', db.Integer, db.ForeignKey('courses.courseID'), primary_key=True)
    jobID = db.Column('jobID', db.Integer, db.ForeignKey('jobs.jobID'), primary_key=True)
    jobs = db.relationship('Jobs')
    def toDict(self):
        return{
            "jobs": self.jobs.toDict()
        }
