from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for, jsonify, json
from sqlalchemy.exc import IntegrityError
from flask_login import current_user, login_required
courses_views = Blueprint('courses_views', __name__, template_folder='../templates')
from App.controllers import(get_courses_json, get_courses, get_jobs, get_jobs_json)
from App.models import Courses, Jobs, db, User, CourseJobs
import ast

#<----------------Render Admin Course and parses jobs and courses------------->

@courses_views.route('/courses_admin', methods=['GET'])
@login_required
def coursesAdmin():
    jobs = get_jobs()
    courses = get_courses()
    return render_template('courses_admin.html', courses=courses, jobs=jobs)

def encoder_course(course):
    if isinstance(course, Courses):
        return {'courseName':course.courseName, 'courseDescription': course.courseDescription, 'skills':course.skills
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
        return "Error"
    if (len(coursedescription) == 0 or len(coursedescription) > 1000 or coursedescription.isdigit() or not coursedescription.strip()):
        return "Error"
    if (len(skills) == 0 or len(skills) >100 or skills.isdigit() or not skills.strip()):
        return "Error" 
    else:
        newcourse = Courses(courseName=coursename, id=current_user.id, courseDescription=coursedescription, skills=skills) # create course object   
        
        jobids = ast.literal_eval(request.form.get('jobs')) #Get values as an array of JobID's
        courseID = newcourse.toDict()["courseID"]
        db.session.add(newcourse)
        
        for jobid in jobids:
            job = Jobs.query.get(jobid)
            courseJob = CourseJobs(courseID=courseID, jobID=jobid, jobs=job)
            try:
                db.session.add(courseJob)
                db.session.commit()
            except IntegrityError:
                return "course Job already added"
        return json.dumps(newcourse, default = encoder_course)

#<-------------------Delete Course----------------------->

@courses_views.route('/deleteCourse/<courseID>', methods=['GET'])
@login_required
def delete_course(courseID):
    course = Courses.query.filter_by(id=current_user.id, courseID=courseID).first() # query course
    if course:
        db.session.delete(course)
        db.session.commit()
        return course.courseID
    return 'Unauthorized or course not found'

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