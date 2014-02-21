from flask import render_template, url_for

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
def index_post(university_id):
    university = models.University.query.get(university_id)
    form = SubmitFeedbackForm()
    if form.validate_on_submit():
        feedback = models.Feedback(name=form.name, body=form.feedback)
        db.session.add(feedback)
        db.session.commit()
        return redirect(url_for('index', university_id=university_id))
    return "Error in form"



@app.route('/admin', methods=['GET'])
def admin():
    pass
