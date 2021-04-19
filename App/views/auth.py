from flask import Blueprint, redirect, render_template, request, jsonify
auth_views = Blueprint('auth_views', __name__, template_folder='../templates')
from flask_login import logout_user, login_user, login_required
from App.models import User
from App.controllers import(get_users_json, get_users, create_user)
from App.forms import LogIn


@auth_views.route('/login')
def index():
    return render_template('login.html')

@auth_views.route('/login', methods=['POST'])
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

@auth_views.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  flash('Logged Out!')
  return redirect(url_for('index'))
