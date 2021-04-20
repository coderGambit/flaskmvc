from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for
from flask_login import current_user, login_required
from App.controllers import(get_courses_json, get_courses)
index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@index_views.route('/about')
def about():
    return render_template('about.html')

@index_views.route('/selectcourse')
def selectcourse():
    courses = Courses.query.all()
    return render_template('selectcourse.html', courses=courses)

@index_views.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')