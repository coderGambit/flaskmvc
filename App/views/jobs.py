from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_login import current_user, login_required
jobs_views = Blueprint('jobs_views', __name__, template_folder='../templates')
from App.controllers import(get_jobs_json, get_jobs)
from App.models import Jobs
from App.forms import JobForm

@jobs_views.route('/jobs', methods=['GET'])
@login_required
def jobs():
    form = JobForm()
    return render_template('jobs.html', form=form)