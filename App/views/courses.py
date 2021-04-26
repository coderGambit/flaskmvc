from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for, jsonify, json
from sqlalchemy.exc import IntegrityError
from flask_login import current_user, login_required
courses_views = Blueprint('courses_views', __name__, template_folder='../templates')
from App.controllers import(get_courses_json, get_courses, get_jobs, get_jobs_json)
from App.models import Courses, Jobs, db, User, CourseJobs
import ast
import uuid

#<----------------Render Admin Course and parses jobs and courses------------->

@courses_views.route('/courses_admin', methods=['GET'])
@login_required
def coursesAdmin():
    jobs = get_jobs()
    courses = get_courses()
    for course in courses:
        course.skills = course.skills.split(',')
    return render_template('courses_admin.html', courses=courses, jobs=jobs)

def encoder_course(course):
    if isinstance(course, Courses):
        return {'courseID':course.courseID,'courseName':course.courseName, 'courseDescription': course.courseDescription, 'skills':course.skills
        }
    raise TypeError(f'Object{course} is not of type Jobs')

#<---------------------------Insert Course Into Database------------------->

@courses_views.route('/insertCourse', methods=['POST'])
@login_required
def insertCourse():
    coursename = request.form.get('coursename')  
    coursedescription = request.form.get('coursedescription') 
    skills = request.form.get('skills')

    #<----Data validation----->

    if (len(coursename) == 0 or len(coursename)>100 or not coursename.strip()):
        return ""
    if (len(coursedescription) == 0 or len(coursedescription) > 1000 or coursedescription.isdigit() or not coursedescription.strip()):
        return ""
    if (len(skills) == 0 or len(skills) >100 or skills.isdigit() or not skills.strip()):
        return "" 
    else:
        newcourse = Courses(courseName=coursename, courseID=uuid.uuid4().int & 0xfffff, courseDescription=coursedescription, skills=skills) # create course object
        
        jobids = ast.literal_eval(request.form.get('jobs')) #Get values as an array of JobID's

        
        for jobid in jobids:
            job = Jobs.query.get(jobid)
            courseJob = CourseJobs(courseID=courseID, jobID=jobid)

            try:
                db.session.add(courseJob)
                db.session.commit()
            except IntegrityError:
                return "course Job already added"

        courseID = newcourse.toDict()["courseID"]
        db.session.add(newcourse)
        return json.dumps(newcourse, default = encoder_course)

#<-------------------Delete Course----------------------->

@courses_views.route('/deleteCourse/<courseID>', methods=['GET'])
@login_required
def delete_course(courseID):

    course = Courses.query.get(courseID) # query course
    if course:

        cjobs = CourseJobs.query.filter_by(courseID)
        for courseJob in cjobs:
            db.session.delete(courseJob)

        db.session.delete(course)
        db.session.commit()
        return courseID
    return 'Unauthorized or course not found'