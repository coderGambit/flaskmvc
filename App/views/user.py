from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_login import current_user, login_required
user_views = Blueprint('user_views', __name__, template_folder='../templates')
from App.models import User
from App.controllers import(get_users_json, get_users, create_user)

#@user_views.route('/users', methods=['GET'])
#def get_user_page():
    #users = get_users
    #return render_template('users.html', users=users)

@user_views.route('/dashboard')
@login_required
def dashboard():
    name = current_user.username
    return render_template('dashboard.html', name=name)