from flask import render_template, g, redirect, url_for, flash, request
from flask.ext.login import login_user, logout_user, login_required, current_user
import flask_sijax

from app import app, models, db, lm
from app.forms import SubmitFeedbackForm, EditUniversityForm, AddUniversityForm, AddUserForm, ManageUserForm, LoginForm





#======================================== HOME ========================================#

## HOME
@flask_sijax.route(app, "/")
def home():
    return render_template('index.html', page_id="home", title="Home")

#======================================== ADMIN =======================================#

## ADMIN
@flask_sijax.route(app, "/admin/")
@login_required
def admin():
    universities = models.University.query.all()
    users = models.User.query.all()
    return render_template("admin.html", user=g.user, page_id="admin", title="Administrator", universities=universities, users=users)

## LOGIN
@flask_sijax.route(app, "/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        mail = form.mail.data
        pw = form.pw.data

        user = models.User.query.filter_by(mail=mail).first()

        if (not user is None) and (user.check_password(pw)):
            login_user(user)
            return redirect(request.args.get("next") or url_for("admin"))
        flash("Invalid login combination.", "danger")
    return render_template('login.html', page_id="admin", title="Login", form=form)

## LOGOUT
@flask_sijax.route(app, "/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

#==================================== UNIVERSITY =====================================#

## UNIVERSITIES
@flask_sijax.route(app, "/universities/")
def list_universities():
    universities = models.University.query.all()
    return render_template('uni_list.html', universities=universities, page_id="universities", title="Universities")

## ADD UNIVERSITY
@flask_sijax.route(app, "/add/university")
@login_required
def add_university():
    form = AddUniversityForm()

    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        pw = form.pw.data
        description = form.description.data
        location = form.location.data

        university = models.University(name=name, username=username, password=pw, description=description,
                                       location=location)
        db.session.add(university)
        db.session.commit()
        flash("The university %r has been created!" % str(name), "success")
        return redirect(url_for('admin'))

    return render_template("add_university.html", page_id="admin", title="New university", form=form)


## EDIT UNIVERSITY
@flask_sijax.route(app, "/edit/university/<int:university_id>")
@login_required
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

        flash("Changes to %r have been saved!" % str(name), "success")
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
@login_required
def delete_university(university_id):
    models.University.delete_university(university_id)
    return redirect(url_for('admin'))

#====================================== FEEDBACK ======================================#

## DELETE FEEDBACK
@flask_sijax.route(app, "/delete/feedback/<int:feedback_id>")
@login_required
def delete_feedback(feedback_id):
    post = models.Feedback.query.get(feedback_id)
    university_id = post.university.id
    models.Feedback.delete_feedback(feedback_id)
    return redirect(url_for('university', university_id=university_id))


#======================================== USER ========================================#

## ADD USER
@flask_sijax.route(app, "/add/user")
@flask_sijax.route(app, "/add/user/<int:role>")
@login_required
def add_user(role=0):
    form = AddUserForm()

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        pw = form.pw.data
        mail = form.mail.data
        user = models.User(name=name, surname=surname, password=pw, mail=mail, role=role)

        db.session.add(user)
        db.session.commit()
        flash("The user %r has been created!" % str(name+' '+surname), "success")
        return redirect(url_for('admin'))

    return render_template("add_user.html", page_id="admin", title="New user", form=form)

## EDIT USER
@flask_sijax.route(app, "/edit/user/<int:user_id>")
@login_required
def edit_user(user_id):
    user = models.User.query.get(user_id)
    form = ManageUserForm(role=user.role)
    if form.validate_on_submit():
        user.name = form.name.data
        user.surname = form.surname.data
        user.mail = form.mail.data
        user.role = int(form.role.data)

        pw = form.pw.data
        if pw != "":
            user.set_password(pw)

        db.session.commit()
        flash("Changes to user %r have been saved!" % str(form.name.data+" "+form.surname.data), "success")
        return redirect(url_for('admin'))

    return render_template("edit_user.html", page_id="admin", title="Edit - " + user.mail,
                           user=user, form=form)

## DELETE USER
@flask_sijax.route(app, "/delete/user/<int:user_id>")
@login_required
def delete_user(user_id):
    models.User.delete_user(user_id)
    return redirect(url_for('admin'))

#======================================= SIJAX ========================================#

## SIJAX REQUESTS
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


#======================================= LOGIN ========================================#

## LOGIN SYSTEM
@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user