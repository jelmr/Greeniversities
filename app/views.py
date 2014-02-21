from flask import render_template

from app import app, models
from app.forms import SubmitFeedbackForm


@app.route('/', methods=['GET'])
@app.route('/university/<int:university_id>', methods=['GET'])
def index(university_id=1):
    university = models.University.query.get(university_id)
    feedback_form = SubmitFeedbackForm()
    return render_template("index.html", title='Home', university=university, form=feedback_form)


@app.route('/', methods=['POST'])
@app.route('/university/<int:university_id>', methods=['POST'])
def index_post():
    pass


@app.route('/admin', methods=['GET'])
def admin():
    pass