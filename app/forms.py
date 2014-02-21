from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required





class SubmitFeedbackForm(Form):
    name = TextField('name', validators=[Required()])
    feedback = TextAreaField('feedback', validators=[Required()])
