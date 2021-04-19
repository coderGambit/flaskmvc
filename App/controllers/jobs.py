from flask import redirect, render_template, request, session, url_for

from App.models import ( Jobs )

def get_jobs_json():
    jobs = Jobs.query.all()
    if not jobs:
        return jsonify([])
    json = [job.toDict() for job in jobs]
    return json 

def get_jobs():
    return Jobs.query.all()