from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

courses_views = Blueprint('courses_views', __name__, template_folder='../templates')

from App.models import Courses

#from App.forms import CourseForm