from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField, SelectMultipleField, widgets, TextField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms.fields.html5 import EmailField

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class JobForm(FlaskForm):
    jobname = TextField('Job Name', validators=[InputRequired()])
    jobdescription =TextField('Job Description', validators=[InputRequired()])
    requirements = TextField('Requirments', validators=[InputRequired()])
    submit = SubmitField('Submit Job', render_kw={'class': 'btn waves-effect waves-light white-text'})


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class CourseForm(FlaskForm):
    coursename = TextField('Course Name', validators=[InputRequired()])
    coursedescription = TextField('Course Description', validators=[InputRequired()])
    skills = TextField('Course Skills', validators=[InputRequired()])
    jobchoices = MultiCheckboxField('jobs',coerce=int)
    submit = SubmitField("Submit Course")
