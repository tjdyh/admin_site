from flask import render_template, session, redirect, url_for, current_app, flash
from datetime import datetime
from . import main
from .forms import NameForm


@main.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@main.route('/test')
def test_index():
    return render_template('test.html', current_time=datetime.utcnow())

# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         old_name = session.get('name')
#         if old_name is not None and old_name != form.name.data:
#             flash('Looks like you have changed your name!')
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())