from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.models import User

from App.controllers import(get_users_json, get_users, create_user)
from App.forms import LogIn


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_users
    return render_template('users.html', users=users)

@user_views.route('/login')
def index():
    newuser = create_user('bob', 'bob@mail.com','bobpass')
    return render_template('login.html', newuser=newuser)

@user_views.route('/login', methods=['POST'])
def loginAction():
    form = LogIn()
    if form.validate_on_submit(): 
        data = request.form
        user = User.query.filter_by(username = data['username']).first()
    if user and user.check_password(data['password']): 
        flash('Logged in successfully.') 
        login_user(user) 
        return redirect(url_for('todos')) 
    flash('Invalid credentials')
    return redirect(url_for('index'))
