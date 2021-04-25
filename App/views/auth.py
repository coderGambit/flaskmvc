from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for
from flask_login import current_user, login_required
auth_views = Blueprint('auth_views', __name__, template_folder='../templates')
from flask_login import logout_user, login_user, login_required
from App.models import User
from App.forms import LogIn


@auth_views.route('/login', methods=['GET'])
def index():
  form = LogIn()
  return render_template('login.html', form=form)

@auth_views.route('/login', methods=['POST'])
def loginAction():
    form = LogIn()
    if form.validate_on_submit(): # respond to form submission
        data = request.form
        user = User.query.filter_by(username = data['username']).first()
        if user and user.check_password(data['password']): # check credentials
         login_user(user) # login the user
         return redirect(url_for('user_views.dashboard')) # redirect to main page if login successful
    return redirect(url_for('auth_views.index'))

@auth_views.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth_views.index'))
