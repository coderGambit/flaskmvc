from flask import redirect, render_template, request, session, url_for

from App.models import ( Courses )


def get_courses_json():
    courses = Courses.query.all()
    if not courses:
        return jsonify([])
    json = [course.toDict() for course in courses]
    return json 

def get_courses():
    return Courses.query.all()