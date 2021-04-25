from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for
from flask_login import current_user, login_required
from App.controllers import(get_courses_json, get_courses)
index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index():
    courses = [
        {
            "courseID": "1",
            'courseName': "INFO 2604",
            'courseDescription': "Data Structures",
            'skills': ["data Structures", "Algorithms", "C", "C++", "Python", "Prolog", "Sql", "PostgreSql"],
            "jobInfo": [
                {
                    "jobID": "123456",
                    "jobName": "Software Engineer",
                    "jobDescription": "Build Great Software!",
                    "requirements": "CS/E Degree"
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
                    "jobID": "56764594",
                    "jobName": "Java Developer",
                    "jobDescription": "Build Everything with Java",
                    "requirements": "CS/E Degree"
                }
            ]
        },
        {
            "courseID": "2",
            'courseName': "INFO 2602",
            'courseDescription': "Web Programming",
            'skills': ["HTML", "CSS", "JavaScript", "Python"],
            "jobInfo": [
                {
                    "jobID": "384974",
                    "jobName": "Aerospace Engineer",
                    "jobDescription": "Build Great Aeroplanes!",
                    "requirements": "CS/E Degree"
                },
                {
                    "jobID": "34726",
                    "jobName": "Musician",
                    "jobDescription": "Play the Guitar",
                    "requirements": "CS/E Degree"
                },
                {
                    "jobID": "3475",
                    "jobName": "Footballer",
                    "jobDescription": "Come play for Barcelona",
                    "requirements": "CS/E Degree"
                },
                {
                    "jobID": "324756",
                    "jobName": "Radio DJ",
                    "jobDescription": "Talk on the radio",
                    "requirements": "CS/E Degree"
                }
            ]
        },
        {
            "courseID": "3",
            'courseName': "COMP 1400",
            'courseDescription': "Intro to Compsci",
            'skills': ["data Structures", "Algorithms", "C", "C++", "Python", "Prolog", "Sql", "PostgreSql"],
            "jobInfo": [
                {
                    "jobID": "123456",
                    "jobName": "Software Engineer",
                    "jobDescription": "Build Great Software!",
                    "requirements": "CS/E Degree"
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
                    "jobID": "56764594",
                    "jobName": "Java Developer",
                    "jobDescription": "Build Everything with Java",
                    "requirements": "CS/E Degree"
                }
            ]
        },
        {
            "courseID": "4",
            'courseName': "FOUN 1101",
            'courseDescription': "Sci-Tech",
            'skills': ["HTML", "CSS", "JavaScript", "Python"],
            "jobInfo": [
                {
                    "jobID": "384974",
                    "jobName": "Aerospace Engineer",
                    "jobDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet commodo nulla facilisi nullam vehicula. Massa massa ultricies mi quis hendrerit dolor magna eget est. Justo nec ultrices dui sapien eget mi. Diam in arcu cursus euismod quis viverra nibh. Potenti nullam ac tortor vitae purus. Lorem donec massa sapien faucibus et molestie ac. Suspendisse ultrices gravida dictum fusce ut. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Consequat mauris nunc congue nisi vitae suscipit tellus. Eget sit amet tellus cras adipiscing. Tristique senectus et netus et malesuada. Consequat interdum varius sit amet mattis. Volutpat ac tincidunt vitae semper quis lectus. Vitae suscipit tellus mauris a diam maecenas sed enim ut. Nunc id cursus metus aliquam eleifend mi in nulla. \nFames ac turpis egestas maecenas pharetra convallis. Egestas sed tempus urna et pharetra pharetra massa. Vitae semper quis lectus nulla. Amet porttitor eget dolor morbi non arcu risus. Consequat mauris nunc congue nisi vitae. Sed libero enim sed faucibus turpis in eu. Tincidunt lobortis feugiat vivamus at augue eget arcu. Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper. Leo integer malesuada nunc vel risus commodo viverra. Turpis egestas pretium aenean pharetra. Accumsan lacus vel facilisis volutpat est.\nNon arcu risus quis varius quam quisque id. Aliquam ut porttitor leo a diam sollicitudin. Gravida in fermentum et sollicitudin ac. Mattis enim ut tellus elementum sagittis. Vel pretium lectus quam id. Proin sed libero enim sed. Turpis tincidunt id aliquet risus feugiat in ante. Dignissim convallis aenean et tortor at. Erat velit scelerisque in dictum non consectetur. Suscipit adipiscing bibendum est ultricies integer quis auctor elit. Arcu non odio euismod lacinia. Cursus mattis molestie a iaculis at. Feugiat in fermentum posuere urna nec tincidunt praesent semper. Rhoncus est pellentesque elit ullamcorper dignissim cras. Pellentesque habitant morbi tristique senectus et netus et malesuada. Auctor urna nunc id cursus metus aliquam eleifend. Neque volutpat ac tincidunt vitae semper quis lectus nulla.\n Accumsan tortor posuere ac ut consequat semper viverra. Id aliquet risus feugiat in ante metus dictum at. Sagittis orci a scelerisque purus semper. Non consectetur a erat nam at. Dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras. Adipiscing diam donec adipiscing tristique risus nec feugiat in fermentum. Etiam sit amet nisl purus in mollis nunc sed id. Quis eleifend quam adipiscing vitae proin sagittis nisl. Vitae sapien pellentesque habitant morbi tristique senectus et netus et. Pellentesque id nibh tortor id aliquet lectus. Egestas pretium aenean pharetra magna ac placerat. Rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis. Cursus eget nunc scelerisque viverra mauris. Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla. Eu ultrices vitae auctor eu augue ut lectus.\n                    Adipiscing diam donec adipiscing tristique risus nec. Pellentesque elit eget gravida cum sociis natoque penatibus et magnis. Viverra vitae congue eu consequat ac felis. Ut placerat orci nulla pellentesque dignissim enim. Sed lectus vestibulum mattis ullamcorper velit. Suscipit adipiscing bibendum est ultricies integer quis auctor. Viverra nam libero justo laoreet. Tristique et egestas quis ipsum. Condimentum mattis pellentesque id nibh tortor. Vitae elementum curabitur vitae nunc. Iaculis nunc sed augue lacus viverra. Tortor dignissim convallis aenean et. Morbi blandit cursus risus at ultrices mi. Molestie a iaculis at erat pellentesque adipiscing. Rutrum quisque non tellus orci ac auctor augue mauris. Nibh tellus molestie nunc non. Cursus eget nunc scelerisque viverra mauris in aliquam sem fringilla. Quam adipiscing vitae proin sagittis nisl rhoncus.",
                    "requirements": "CS/E Degree"
                },
                {
                    "jobID": "34726",
                    "jobName": "Writer",
                    "jobDescription": "Aerospace Engineer",
                    "jobDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet commodo nulla facilisi nullam vehicula. Massa massa ultricies mi quis hendrerit dolor magna eget est. Justo nec ultrices dui sapien eget mi. Diam in arcu cursus euismod quis viverra nibh. Potenti nullam ac tortor vitae purus. Lorem donec massa sapien faucibus et molestie ac. Suspendisse ultrices gravida dictum fusce ut. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Consequat mauris nunc congue nisi vitae suscipit tellus. Eget sit amet tellus cras adipiscing. Tristique senectus et netus et malesuada. Consequat interdum varius sit amet mattis. Volutpat ac tincidunt vitae semper quis lectus. Vitae suscipit tellus mauris a diam maecenas sed enim ut. Nunc id cursus metus aliquam eleifend mi in nulla. \nFames ac turpis egestas maecenas pharetra convallis. Egestas sed tempus urna et pharetra pharetra massa. Vitae semper quis lectus nulla. Amet porttitor eget dolor morbi non arcu risus. Consequat mauris nunc congue nisi vitae.",
                    "requirements": "CS/E Degree"
                },
                {
                    "jobID": "3475",
                    "jobName": "Editor",
                    "jobDescription": "Edit for the newspaper",
                    "requirements": "CS/E Degree"
                }
            ]
        }
    ]
    return render_template('index.html', courses=courses)