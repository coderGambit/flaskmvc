from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for, jsonify, json
from flask_login import current_user, login_required
from wtforms import Form, SelectMultipleField
courses_views = Blueprint('courses_views', __name__, template_folder='../templates')
from App.controllers import(get_courses_json, get_courses, get_jobs, get_jobs_json)
from App.models import Courses, Jobs, db, User
from App.forms import CourseForm
import ast

#<----------------Render Admin Course and parses jobs and courses------------->

@courses_views.route('/courses_admin', methods=['GET'])
@login_required
def coursesAdmin():
    jobs = get_jobs()
    courses = get_courses()
    return render_template('courses_admin.html', courses=courses, jobs=jobs)


#<---------------------------Insert Course Into Database------------------->

@courses_views.route('/insertcourse', methods=['POST'])
@login_required
def insertCourse():
    coursename = request.form['coursename']  
    coursedescription = request.form['coursedescription']  
    skills = request.form['skills']

    #<----Data validation----->
    if (len(coursename) == 0 or len(coursename)>100 or not course.strip()):
        return False
    if (len(coursedescription) == 0 or len(coursedescription) > 1000 or coursedescription.isdigit() or not coursedescription.strip()):
        return False
    if (len(skills) == 0 or len(skills) >100 or skills.isdigit() or not skills.strip()):
        return False 
    
    if form.validate_on_submit():    
        newcourse = Courses(courseName=data['coursename'], id=current_user.id, courseDescription=data['coursedescription'], skills=data['skills']) # create course object   
    jobids = ast.literal_eval(request.form['jobs']) #Get values as an array of JobID's
    accepted = []
    for jobid in jobids:
        job = Jobs.query.get(jobid) #Query eacj JobID
        accepted.append(job)
    newcourse.jobs = accepted
    db.session.add(newcourse)
    db.session.commit()
    return json.dumps(newcourse)

#<-------------------Delete Course----------------------->

@courses_views.route('/deleteCourse/<courseID>', methods=['DELETE'])
@login_required
def delete_course(courseID):
    course = Courses.query.filter_by(id=current_user.id, courseID=courseID).first() # query course
    if course:
        db.session.delete(course)
        db.session.commit()
        return course.courseID
    return 'Unauthorized or course not found'
#<------
# ----------------Edit Course Route-------------------------------->

@courses_views.route('/editCourse/<courseID>', methods=['PUT'])
@login_required
def edit_course(courseID):
    course = Course.query.filter_by(id=current_user.id, courseID=courseID).first()
    if course == None:
        return 'Invalid id or unauthorized'
    data = request.forms
    if 'courseName' in data:
        course.courseName = data['courseName']
    if 'courseDescription' in data:
        course.courseDescription = data['courseDescription']
    if 'skills' in data:
        course.skills = data['skills']
    if 'jobs' in data['jobs']:
        for jobid in data['jobs']:
            job = Jobs.query.get(jobid) #Query each JobID
            accepted.append(job)
    course.jobs = accepted 
    db.session.add(course)
    db.session.commit()
    return 'Updated', 201