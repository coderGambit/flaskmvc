from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime
from .user import *
from .jobs import *

class CourseJobs (db.Model):
    courseID = db.Column('courseID', db.Integer, db.ForeignKey('course.courseID'), primary_key=True)
    jobID = db.Column('jobID', db.Integer, db.ForeignKey('jobs.jobID'), primary_key=True)
    jobs = db.relationship('Jobs')

    def toDict(self):
        return{
            "jobs": self.jobs.toDict()
        }


# Add the following code to the problem area and let me know if it work
#   courseID = newcourse.toDict()["courseID"]
#   for jobid in jobids:
#          job = Jobs.query.get(jobid)
#          courseJob = CourseJob(courseID=courseID, jobID=jobid, job=job)
#          try:
#           db.session.add(courseJob)
#           db.session.commit()
#          except IntegrityError:
#           db.session.rollback()
#           return "courseJob already added"
