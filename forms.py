from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL)


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    body = TextAreaField('Message', [
        DataRequired(),
        Length(min=4, message='Your message is too short.')])
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    """Sign up for a user account."""
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
    ])
    confirmPassword = PasswordField('Repeat Password', [
            EqualTo(password, message='Passwords must match.')
            ])
    title = SelectField('Title', [DataRequired()],
                        choices=[('Farmer', 'Farmer'),
                                 ('Corrupt Politician', 'Corrupt Politician'),
                                 ('No-nonsense City Cop', 'No-nonsense City Cop'),
                                 ('Professional Rocket League Player', 'Professional Rocket League Player'),
                                 ('Lonely Guy At A Diner', 'Lonely Guy At A Diner'),
                                 ('Pokemon Trainer', 'Pokemon Trainer')])
    website = StringField('Website', validators=[URL()])
    birthday = DateField('Your Birthday')
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
