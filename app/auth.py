from flask import Blueprint, url_for, flash, render_template, redirect

# Відсутній імпорт login_user, logout_user, login_required.
from flask_login import login_user, logout_user, login_required

from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        # Додано bcrypt.generate_password_hash() для хешування пароля.
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        # user.set_password(user)
        # ❌ Неправильне використання user.set_password(user) — слід передавати пароль, а не об'єкт.

        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # Додано bcrypt.generate_password_hash() для хешування пароля.
        # if user and bcrypt.check_password_hash(user.password, form.password.data):

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        flash('Invalid email or password', 'danger')
        return render_template('login.html', title='Login', form=form)


@auth.route('/logout')
@login_required
def logout():

    logout('You have been logged out.', 'success')

    # ❌ Помилка у logout:
    # logout('You have been logged out.', 'success') → має бути logout_user() + flash().

    return redirect(url_for('main.index'))


