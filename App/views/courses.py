from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_login import current_user, login_required
courses_views = Blueprint('courses_views', __name__, template_folder='../templates')
from App.controllers import(get_courses_json, get_courses)
from App.models import Courses

#from App.forms import CourseForm

@courses_views.route('/courses')
@login_required
def courses():
    return render_template('courses.html')