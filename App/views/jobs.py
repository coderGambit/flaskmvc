from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

jobs_views = Blueprint('jobs_views', __name__, template_folder='../templates')

from App.models import Jobs

from App.forms import JobForm


@jobs_views.route('/jobs')
def index():
    return render_template('jobs.html')