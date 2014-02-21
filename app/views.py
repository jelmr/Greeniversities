import datetime

from flask import render_template, redirect

from app import app, models, db
from app.forms import SubmitFeedbackForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/university/<int:university_id>', methods=['GET', 'POST'])
def index(university_id=1):
    university = models.University.query.get(university_id)
    feedback_form = SubmitFeedbackForm()

    if feedback_form.validate_on_submit():
        u = models.Feedback(name=feedback_form.name.data, body=feedback_form.feedback.data, rating=5, university=university)
        db.session.add(u)
        db.session.commit()
        return redirect('/')

    return render_template("index.html", title='Home', university=university, form=feedback_form)


@app.route('/feedback/<int:feedback_id>', methods=['GET', 'DELETE'])
def delete_post(feedback_id):
    post = models.Feedback.query.get(feedback_id)
    db.session.delete(post)
    db.session.commit()
    return 'Succes', 204