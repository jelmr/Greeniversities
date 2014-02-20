from flask import render_template, flash, redirect
from app import app, db, models
from forms import LoginForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    fruit = models.Fruit.query.all()

    form = LoginForm()

    if form.validate_on_submit():
        u = models.Fruit(name=form.name.data, color=form.color.data)
        db.session.add(u)
        db.session.commit()
        return redirect('/index')

    return render_template("index.html", title='Home',  fruit=fruit, form=form)


@app.route('/css/style.css')
def style():
    return
