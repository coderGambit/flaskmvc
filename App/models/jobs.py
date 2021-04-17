from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime

class Jobs(db.Model):
    jobID = db.Column(db.Integer, primary_key=True)
    jobName = db.Column(db.String(80), nullable=False)
    jobDescription = db.Column(db.String(1000), nullable=False)
    jobDescription = db.Column(db.String(1000), nullable=False)
    def toDict(self):
        return {
            "jobID": self.courseID,
            "jobName": self.courseName,
            "jobDescription": self.courseDescription
            }