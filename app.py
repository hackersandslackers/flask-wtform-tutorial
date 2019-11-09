from flask import Flask, url_for, render_template, redirect
from forms import ContactForm, SignupForm

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
app.config['RECAPTCHA_PUBLIC_KEY'] = 'iubhiukfgjbkhfvgkdfm'
app.config['RECAPTCHA_PARAMETERS'] = {'size': '100%'}


@app.route('/')
def home():
    return render_template('index.html',
                           template='home-template')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'), code=200)
    return render_template('contact.html',
                           form=form,
                           template='form-template')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('success'), code=200)
    return render_template('signup.html',
                           form=form,
                           template='form-template')


@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',
                           template='success-template')
