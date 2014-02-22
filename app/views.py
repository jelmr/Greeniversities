from flask import render_template, g, redirect, url_for, flash
import flask_sijax

from app import app, models, db
from app.forms import SubmitFeedbackForm, EditUniversityForm, AddUniversityForm



## TEST
@flask_sijax.route(app, "/test")
def test():
    return render_template('test.html')


## HOME
@flask_sijax.route(app, "/")
def home():
    return render_template('index.html', page_id="home", title="Home")


## UNIVERSITIES
@flask_sijax.route(app, "/universities/")
def list_universities():
    universities = models.University.query.all()
    return render_template('uni_list.html', universities=universities, page_id="universities", title="Universities")

## ADMIN
@flask_sijax.route(app, "/admin/")
def admin():
    flash("Updated university")
    universities = models.University.query.all()
    return render_template("admin.html", page_id="admin", title="Administrator", universities=universities)

## ADD UNIVERSITY
@flask_sijax.route(app, "/add/university")
def add_university():

    form = AddUniversityForm()

    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        pw = form.pw.data
        description = form.description.data
        location = form.location.data

        university = models.University(name=name, username=username, password=pw, description=description, location=location)
        db.session.add(university)
        db.session.commit()

        return redirect(url_for('admin'))

    return render_template("add_university.html", page_id="admin", title="New university", form=form)


## EDIT UNIVERSITY
@flask_sijax.route(app, "/edit/university/<int:university_id>")
def edit_university(university_id):
    university = models.University.query.get(university_id)
    form = EditUniversityForm()

    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        pw = form.pw.data
        description = form.description.data
        location = form.location.data

        models.University.update(university, name, username, pw, description, location)
        return redirect(url_for('admin'))

    form.description.data = university.description
    return render_template("edit_university.html", page_id="admin", title="Edit - " + university.name,
                           university=university, form=form)


## VIEW SPECIFIC UNIVERSITY
@flask_sijax.route(app, "/universities/<int:university_id>")
def university(university_id=1):
    university = models.University.query.get(university_id)

    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()

    form = SubmitFeedbackForm()

    if form.validate_on_submit():
        models.Feedback.save_feedback(form.name.data, form.feedback.data, 5, university_id)

    return render_template("university.html", university=university, form=form, page_id="universities",
                           title=university.name + " - Universities")


## DELETE UNIVERSITY
@flask_sijax.route(app, "/delete/university/<int:university_id>")
def delete_university(university_id):
    models.University.delete_university(university_id)
    return redirect(url_for('admin'))

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


