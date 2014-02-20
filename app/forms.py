from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('name', validators = [Required()])
    color = TextField('color', validators = [Required()])
