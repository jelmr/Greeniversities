from flask import render_template, g, redirect, url_for
import flask_sijax
from app import app, models
from app.forms import SubmitFeedbackForm

## HOME
@flask_sijax.route(app, "/")
def home():
    return render_template('index.html', page_id="home", title="Home")


## UNIVERSITIES
@flask_sijax.route(app, "/universities/")
def list_universities():

    return render_template('uni_list.html', universities=universities, page_id="universities", title="Universities")

## ADMIN
@flask_sijax.route(app, "/admin/")
def admin():
    universities = models.University.query.all()
    return render_template("admin.html", page_id="admin", title="Administrator", universities=universities)

## EDIT UNIVERSITY
@flask_sijax.route(app, "edit/university/<int:university_id>")
def edit_university(university_id):
    university = models.University.query.get(university_id)




## SPECIFIC UNIVERSITY
@flask_sijax.route(app, "/universities/<int:university_id>")
def university(university_id=1):
    university = models.University.query.get(university_id)

    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()

    form = SubmitFeedbackForm()

    if form.validate_on_submit():
        models.Feedback.save_feedback(form.name.data, form.feedback.data, 5, university_id)

    return render_template("university.html", university=university, form=form, page_id="universities", title=university.name+" - Universities")


## DELETE FEEDBACK
@flask_sijax.route(app, "/delete/feedback/<int:feedback_id>")
def delete_feedback(feedback_id):
    post = models.Feedback.query.get(feedback_id)
    university_id = post.university.id
    models.Feedback.delete_feedback(feedback_id)
    return redirect(url_for('university', university_id=university_id))



class SijaxHandler(object):
    @staticmethod
    def delete_post(obj_response, post_id):
        models.Feedback.delete_feedback(post_id)
        obj_response.remove("#" + str(post_id))

    @staticmethod
    def add_post(obj_response, name, message, university_id):
        feedback = models.Feedback.save_feedback(name, message, 5, university_id)
        obj_response.html_prepend("#posts", render_template("post.html", post=feedback))
        obj_response.script("$('#feedback_form')[0].reset();")


