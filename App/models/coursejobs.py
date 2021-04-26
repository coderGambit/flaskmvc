from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime
from .courses import *
from .user import *
from .jobs import *

association_table = db.Table('association_table',
                             db.Column('courseID', db.Integer, db.ForeignKey('courses.courseID')),
                             db.Column('jobID', db.Integer, db.ForeignKey('jobs.jobID')))
