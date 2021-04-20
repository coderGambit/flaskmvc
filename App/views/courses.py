from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for
from flask_login import current_user, login_required
from wtforms import Form, SelectMultipleField
courses_views = Blueprint('courses_views', __name__, template_folder='../templates')
from App.controllers import(get_courses_json, get_courses, get_jobs)
from App.models import Courses, Jobs
from App.forms import CourseForm


#<----------------Course Form------------------------>

@courses_views.route('/courses', methods=['GET'])
def courses():
    form = CourseForm()
    courses = Courses.query.all()
    jobs = Jobs.query.all()
    return render_template('courses.html', form=form, courses=courses, jobs=jobs)

@courses_views.route("/courses", methods=["GET", "POST"])
def courseAction():
     form = CourseForm() # create form object
     if form.validate_on_submit():
        data = request.form # get data from form submission
        choices = request.form.getlist('jobscheckbox') #This is the name of the checkboxes
        newcourse = Courses(courseName=data['courseName'], courseDescription=data['courseDescription'], skills=data['skills'], jobs=choices) # create course object 
        db.session.add(newcourse) # save new course
        db.session.commit()
        flash('Job Created!')# send message
        return redirect(url_for('dashboard'))# redirect to the dashboard page
        flash('Error invalid input!')
        return redirect(url_for('dashboard')) 

#<-------------------Delete Course----------------------->

@courses_views.route('/deleteCourse/<id>', methods=['GET'])
@login_required
def delete_course(id):
    course = Course.query.filter_by(userid=current_user.id, id=id).first() # query course
    if course:
        db.session.delete(course)
        db.session.commit()
        flash('Course Deleted!')
        return redirect(url_for('courses'))
    flash('Unauthorized or course not found')
    return redirect(url_for('courses'))