from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, PasswordField, SelectField, IntegerField
from wtforms.validators import Required, EqualTo, Email

from app import models


#===================================== FEEDBACK =======================================#

class SubmitFeedbackForm(Form):
    name = TextField('Name', validators=[Required()])
    rating = IntegerField('Rating', validators=[Required()])
    feedback = TextAreaField('Feedback', validators=[Required()])

#==================================== UNIVERSITY ======================================#


class EditUniversityForm(Form):
    name = TextField('Name', validators=[Required()])
    description = TextAreaField('Feedback')
    location = TextField('Location', validators=[Required()])
    logo_url = TextField('Logo url')


class AddUniversityForm(EditUniversityForm):
    pass

#======================================== USER ========================================#


class ChangeUserInfo(Form):
    name = TextField('Name', validators=[Required()])
    surname = TextField('Surname', validators=[Required()])
    mail = TextField('Mail', validators=[Required(), Email()])


class ChangeUserPassword(Form):
    pw = PasswordField('New Password', [Required(), EqualTo('confirmpw', message='Passwords must match')])
    confirmpw = PasswordField('Repeat Password', validators=[Required()])


class AddUserForm(ChangeUserPassword, ChangeUserInfo):
    pass


class ManageUserForm(AddUserForm):
    pw = PasswordField('New Password', [EqualTo('confirmpw', message='Passwords must match')])
    confirmpw = PasswordField('Repeat Password')


class AdminManageUserForm(ManageUserForm):
    role = SelectField('Role', choices=[(str(models.ROLE_USER), 'User'), (str(models.ROLE_UNIVERSITY), 'University'),
                                        (str(models.ROLE_ADMIN), 'Admin')])


#======================================= LOGIN ========================================#

class LoginForm(Form):
    mail = TextField('Mail', validators=[Required()])
    pw = PasswordField('Password', validators=[Required()])


#==================================== STUDYFIELD ======================================#


class AddStudyfieldForm(Form):
    name = TextField('Name', validators=[Required()])


#====================================== STUDY =========================================#


class AddStudyForm(Form):
    name = TextField('Name', validators=[Required()])
    url = TextField('URL', validators=[Required()])
    studyfield_id = IntegerField('Studyfield id', validators=[Required()])
