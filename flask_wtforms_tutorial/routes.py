from flask import url_for, render_template, redirect
from flask import current_app as app
from .forms import ContactForm, SignupForm


@app.route('/')
def home():
    return render_template('index.jinja2',
                           template='home-template')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('contact.jinja2',
                           form=form,
                           template='form-template')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('signup.jinja2',
                           form=form,
                           template='form-template')


@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.jinja2',
                           template='success-template')
