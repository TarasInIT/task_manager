from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', [DataRequired(), Length(min=3, max=20)])
    email = StringField('Email',[DataRequired(), Email()])
    password = PasswordField('Пароль', [DataRequired(), Length(max=6)])
    confirm_password = PasswordField('Повторите пароль', [DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Пароль', [DataRequired()])
    submit = SubmitField('Войти')
