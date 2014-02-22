from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, PasswordField
from wtforms.validators import Required, EqualTo


class SubmitFeedbackForm(Form):
    name = TextField('name', validators=[Required()])
    feedback = TextAreaField('feedback', validators=[Required()])


class EditUniversityForm(Form):
    username = TextField('name', validators=[Required()])
    pw = PasswordField('New Password', [EqualTo('confirmpw', message='Passwords must match')])
    confirmpw = PasswordField('Repeat Password')
    name = TextField('name', validators=[Required()])
    description = TextAreaField('feedback')
    location = TextField('name', validators=[Required()])


class AddUniversityForm(EditUniversityForm):
    pw = PasswordField('New Password', [Required(), EqualTo('confirmpw', message='Passwords must match')])
    confirmpw = PasswordField('Repeat Password', validators=[Required()])