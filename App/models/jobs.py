from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime

class Jobs(db.Model):
    jobID = db.Column(db.Integer, primary_key=True)
    id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
    jobName = db.Column(db.String(80), nullable=False)
    jobDescription = db.Column(db.String(1000), nullable=False)
    requirements = db.Column(db.String(1000), nullable=False)
    def toDict(self):
        return {
            "jobID": self.jobID,
            "jobName": self.jobName,
            "jobDescription": self.jobDescription,
            "requirements": self.requirements
            }