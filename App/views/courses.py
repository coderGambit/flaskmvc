from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for, jsonify, json
from flask_login import current_user, login_required
from wtforms import Form, SelectMultipleField
courses_views = Blueprint('courses_views', __name__, template_folder='../templates')
from App.controllers import(get_courses_json, get_courses, get_jobs)
from App.models import Courses, Jobs, db, User
from App.forms import CourseForm

#<----------------Course Form------------------------>

@courses_views.route('/courses', methods=['GET'])
@login_required
def courses():
    jobs = Jobs.query.all()
    form = CourseForm()
    courses = Courses.query.all()
    form.jobchoices.choices = [(job.jobID, job.jobName) for job in jobs ]
    courseskills = [course.skills for course in courses]
    skills = []
    for skill in courseskills: 
        skill = skill.replace('.', '')
        skill = skill.replace(',', '')
        skills.append(skill)
    return render_template('courses.html', form=form, courses=courses, jobs=jobs, skills=skills)

@courses_views.route("/courses", methods=["GET", "POST"])
@login_required
def courseAction():
     form = CourseForm() # create form object
     if form.validate_on_submit():
        data = request.form # get data from form submission
        newcourse = Courses(courseName=data['coursename'],id=current_user.id, courseDescription=data['coursedescription'], skills=data['skills']) # create course object 
        db.session.add(newcourse) # save new course
        accepted = []
        c_records = Jobs.query.all()
        for choice in c_records:
            if choice.jobID in form.jobchoices.data:
                accepted.append(choice)
        newcourse.jobs = accepted
        db.session.add(newcourse)
        db.session.commit()
        flash('Course Created!')# send message
        return redirect(url_for('courses_views.courses'))# redirect to the dashboard page  
        flash('Error invalid input!')
        return redirect(url_for('courses_views.courses')) 
     

# Rondell added the following *********************************************

@app.route('/courses_admin')
def coursesAdmin():
    # dummy data, get courses from database and send it to the frontend
    # send all the courses and jobs available in the database
    # this is ther page where the admin will view, edit, delete, and add courses
    # route for the add course function defined below this function as insertCourse()
    courses = [
        {
            'courseName': "INFO 2604",
            'courseDescription': "Data Structures",
            'skills': ["data Structures", "Algorithms", "C", "C++"]
        },
        {
            'courseName': "INFO 2602",
            'courseDescription': "Web Programming",
            'skills': ["HTML", "CSS", "JavaScript", "Python"]
        }
    ]
    jobs = [
        {
            "jobID": "123456",
            "jobName": "Software Engineer",
            "jobDescription": "Build Great Software!",
            "requirements": "CS/E Degree"
        },
        {
            "jobID": "5676454",
            "jobName": "Vagrant",
            "jobDescription": "Harrass People in the Streets",
            "requirements": "2 years living on the streets"
        },
        {
            "jobID": "34566",
            "jobName": "Backend Developer",
            "jobDescription": "Build Great Backend Software!",
            "requirements": "CS/E Degree"
        },
        {
            "jobID": "43898934",
            "jobName": "Frontend Developer",
            "jobDescription": "Build Great Frontend Software!",
            "requirements": "CS/E Degree"
        },
        {
            "jobID": "5676454",
            "jobName": "Java Developer",
            "jobDescription": "Build Everything with Java",
            "requirements": "CS/E Degree"
        }
    ]
    return render_template('courses_admin.html', courses=courses, jobs=jobs)


@app.route('/insertCourse', methods=['POST'])
def insertCourse():
    # retrieve and print form info
    print(request.form['coursename'])
    print(request.form['coursedescription'])
    print(request.form['skills'])

    # sorry, was trying to get the jobs as an array of json jobs object
    # but i can't send it is an object so it getting converted to a string
    # the print statement will show the format so you will have to split the string to extract the objects, 
    # then split it again to get the id and name of the job, then split it one more time to get the actual values
    # Alternatively, I could just send an array of jobIDs and you could just use that?
    print(request.form['jobs'])

    # TODO validate form information return "false" if it has invalid information

    # TODO generate a new course object, insert into the database, and pass the course info back to the frontend the same way you were doing before
    # return course information
    return ""

#****************************************************************

#<-------------------Delete Course----------------------->

@courses_views.route('/deleteCourse/<courseID>', methods=['GET'])
@login_required
def delete_course(courseID):
    course = Courses.query.filter_by(id=current_user.id, courseID=courseID).first() # query course
    if course:
        db.session.delete(course)
        db.session.commit()
        flash('Course Deleted!')
        return redirect(url_for('courses_views.courses'))
    flash('Unauthorized or course not found')
    return redirect(url_for('courses_views.courses'))

#<----------------------Select Course Route-------------------------------->

@courses_views.route('/selectCourse/<courseID>', methods=['GET'])
def course_jobs(courseID):
    courses = Courses.query.filter_by(courseID=courseID).first() # query course (Once models fix add user ID)
    return render_template('courseJobs.html', courses=courses)