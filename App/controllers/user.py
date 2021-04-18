from flask import redirect, render_template, request, session, url_for

from App.models import ( User )

def get_users_json():
    users = User.query.all()
    if not users:
        return jsonify([])
    json = [user.toDict() for user in users]
    return json 

def create_user(username, email, password):
    newuser = User(username=username, email=email) # create user object
    newuser.set_password(password) # set password
    db.session.add(newuser) # save user
    db.session.commit()
    return True

def get_users():
    return User.query.all()