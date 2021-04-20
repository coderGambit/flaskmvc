from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for
from flask_login import current_user, login_required
jobs_views = Blueprint('jobs_views', __name__, template_folder='../templates')
from App.controllers import(get_jobs_json, get_jobs)
from App.models import db, Jobs
from App.forms import JobForm


#<-------------Job Form----------------------->
@jobs_views.route('/jobs', methods=['GET'])
def jobs():
    form = JobForm()
    jobs = Jobs.query.all()
    return render_template('jobs.html', form=form, jobs=jobs)

@jobs_views.route('/jobs', methods=['POST'])
def jobAction():
  form = JobForm() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newjob = Jobs(jobName=data['jobname'], jobDescription=data['jobdescription'], requirements=data['requirements']) # create job object
    db.session.add(newjob) # save new job
    db.session.commit()
    flash('Job Created!')# send message
    return redirect(url_for('jobs_views.jobs'))# redirect to the dashboard page
  flash('Error invalid input!')
  return redirect(url_for('jobs_views.jobs'))

#<---------------Edit Job Still Editing----------------------->

@jobs_views.route('/editJob/<jobID>', methods=['GET'])
def edit_job(jobID): # get the job id from url
    form = JobForm()
    return render_template('edit.html', jobID=jobID, form=form)# pass the form and todo id to the template

@jobs_views.route('/editJob/<jobID>', methods=['POST'])
def edit_job_action(jobID):
  form = JobForm()
  if form.validate_on_submit():
    job = Job.query.filter_by(id=current_user.id, jobID=jobID).first() # query  todo
    job.jobName = data['jobname'] 
    job.jobDescription = data['jobdescription']
    job.requirements = data['requirements']
    db.session.add(job) 
    db.session.commit()
    flash('Job Updated!')
    return redirect(url_for('jobs_views.jobs'))
  flash('Invalid data')
  return redirect(url_for('jobs_views.jobs'))