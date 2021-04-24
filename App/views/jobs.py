from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for
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

#<---------------------------Insert Course Into Database------------------->

@jobs_views.route('/insertjob', methods=['POST'])
@login_required
def insertCourse():
    jobname = request.form['jobname']  
    jobdescription = request.form['jobdescription']  
    requirements = request.form['requirements']
    #<----Data validation----->
    if (len(jobname) == 0 or len(jobname)>100 or not course.strip() or jobname.isdigit() or not jobname.strip()):
        return "Error"
    if (len(jobdescription) == 0 or len(jobdescription) > 1000 or jobdescription.isdigit() or not coursedescription.strip()):
        return "Error"
    if (len(requirements) == 0 or len(requirements) >100 or skills.isdigit() or not skills.strip()):
        return "Error" 
    if form.validate_on_submit():    
        newjob = Courses(jobName=data['jobName'], id=current_user.id, jobDescription=data['jobDescription'], requrements=data['requirements']) # create job object   
        jobids = ast.literal_eval(request.form['jobs']) #Get values as an array of JobID's
        db.session.add(newjob) # save new job
        db.session.commit()
        return json.dumps(newjob)
        
#<-------------------Delete Course----------------------->

@jobs_views.route('/deleteJob/<jobID>', methods=['DELETE'])
@login_required
def delete_job(jobID):
    job = Job.query.filter_by(id=current_user.id, jobID=jobID).first() # query course
    if job:
        db.session.delete(job)
        db.session.commit()
        return job.jobID
    return 'Unauthorized or job not found'

#<---------------Edit Job ----------------------->

@jobs_views.route('/editJob/<jobID>', methods=['PUT'])
@login_required
def edit_job(jobID):
    job = Jobs.query.filter_by(id=current_user.id, jobID=jobID).first()
    if job == None:
        return 'Invalid id or unauthorized'
    data = request.forms
    if 'jobName' in data:
        job.jobName = data['jobName']
    if 'jobDescription' in data:
        job.jobDescription = data['jobDescription']
    if 'requirements' in data:
        job.requrements = data['requirements']  
    db.session.add(job) 
    db.session.commit()
    return 'Updated', 201