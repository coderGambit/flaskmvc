from flask import Blueprint, redirect, render_template, request

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@index_views.route('/about')
def about():
    return render_template('about.html')

@index_views.route('/selectcourse')
def selectcourse():
    return render_template('selectcourse.html')

@index_views.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')