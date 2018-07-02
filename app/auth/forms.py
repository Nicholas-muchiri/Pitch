from wtforms import ,ValidationError, StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    first_name = StringField('Enter your First Name', validators = [Required()])
    last_name = StringField('Enter your Last Name', validators = [Required()])
    username = StringField('Enter a username', validators = [Required()])
    email = StringField('Your Email Address', validators = [Required(), Email()])
    password = PasswordField('Password', validators = [Required(),
    EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

    def validate_email(self, data_field):
            if User.query.filter_by(email = data_field.data).first():
                raise ValidationError('That account has been taken')
    
class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators = [Required(), Email()])
    password = PasswordField('Password', validators = [Required()])
    remember = BooleanField('Remember my password.')
    submit = SubmitField('Sign In')