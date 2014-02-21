from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('name', validators = [Required()])
    color = TextField('color', validators = [Required()])


class SubmitFeedbackForm(Form):
    name = TextField('name', validators = [Required()])
    feedback = TextAreaField('name', validators = [Required()])
