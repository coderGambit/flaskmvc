from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_login import current_user, login_required
jobs_views = Blueprint('jobs_views', __name__, template_folder='../templates')
from App.controllers import(get_jobs_json, get_jobs)
from App.models import Jobs
from App.forms import JobForm

@jobs_views.route('/jobs', methods=['GET'])
def jobs():
    form = JobForm()
    return render_template('jobs.html', form=form)


@jobs_views.route('/jobs', methods=['POST'])
def jobAction():
  form = JobForm() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newjob = Jobs(jobName=data['jobName'], jobDescription=data['jobDescription'], requirements=data['requirements']) # create user object
    db.session.add(newjob) # save new job
    db.session.commit()
    flash('Job Created!')# send message
    return redirect(url_for('dashboard'))# redirect to the dashboard page
  flash('Error invalid input!')
  return redirect(url_for('dashboard')) 