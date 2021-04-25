from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for, json
from flask_login import current_user, login_required
jobs_views = Blueprint('jobs_views', __name__, template_folder='../templates')
from App.controllers import(get_jobs_json, get_jobs)
from App.models import db, Jobs


#<----------------Render Admin Jobs Page and parses jobs------------->

@jobs_views.route('/jobs_admin', methods=['GET'])
@login_required
def coursesAdmin():
    jobs = get_jobs()
    return render_template('jobs_admin.html', jobs=jobs)

#<----------Fixes Serialization Format------------------------------------->

def encoder_jobs(job):
    if isinstance(job, Jobs):
        return {'jobName':job.jobName, 'jobDescription': job.jobDescription, 'requirements':job.requirements
        }
    raise TypeError(f'Object{job} is not of type Jobs')

#<---------------------------Insert Course Into Database------------------->

@jobs_views.route('/insertJob', methods=['POST'])
@login_required
def insertCourse():
    jobname = request.form.get('jobname') 
    jobdescription = request.form.get('jobdescription') 
    requirements = request.form.get('requirements')
    
    #<----Data validation----->
    
    if (len(jobname) == 0 or len(jobname)>100 or not jobname.strip() or jobname.isdigit()):
        return ""
    if (len(jobdescription) == 0 or len(jobdescription) > 1000 or jobdescription.isdigit() or not jobdescription.strip()):
        return ""
    if (len(requirements) == 0 or len(requirements) >100 or requirements.isdigit() or not requirements.strip()):
        return "" 
    else:
        newjob = Jobs(jobName=jobname, jobDescription=jobdescription, requirements=requirements) # create job object
        db.session.add(newjob) # save new job
        db.session.commit()
    return json.dumps(newjob.toDict())
        
#<-------------------Delete Course----------------------->

@jobs_views.route('/deleteJob/<jobID>', methods=['GET'])
@login_required
def delete_job(jobID):
<<<<<<< HEAD
    job = Jobs.query.get(jobID)  # query course
    if job is None:
        return 'Unauthorized or job not found'
    db.session.delete(job)
=======
    job = Jobs.query.get(jobID)# query course
    if job:
        db.session.delete(job)
        db.session.commit()
        return jobID
    return 'Unauthorized or job not found'

#<---------------Edit Job ----------------------->

@jobs_views.route('/editJob/<jobID>', methods=['PUT'])
@login_required
def edit_job(jobID):
    job = Jobs.query.filter_by(id=current_user.id, jobID=jobID).first()
    if job == None:
        return 'Invalid id or unauthorized'
    data = request.forms
    if 'jobname' in data:
        job.jobName = data['jobname']
    if 'jobdescription' in data:
        job.jobDescription = data['jobdescription']
    if 'requirements' in data:
        job.requrements = data['requirements']  
    db.session.add(job) 
>>>>>>> cf5e7f2cc304a85c771c0015f29d41b301610aef
    db.session.commit()
    return job.toDict
    