from flask_wtf import FlaskForm
from flaskapp.models import User
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(),Length(min =2, max=20)])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken.")



class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(),Length(min =2, max=20)])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class BookingForm(FlaskForm):
    Day = StringField('Day', validators=[DataRequired()])
    Time = StringField('Time', validators=[DataRequired()])
    Name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Done')