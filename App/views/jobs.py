from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_login import current_user, login_required
jobs_views = Blueprint('jobs_views', __name__, template_folder='../templates')
from App.models import Jobs
from App.forms import JobForm

@jobs_views.route('/jobs')
@login_required
def jobs():
    return render_template('jobs.html')