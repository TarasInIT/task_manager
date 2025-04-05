from flask import Blueprint, url_for, flash, render_template, redirect
from app import db, bcrypt  # Імпортуємо базу даних і bcrypt для хешування паролів
from app.forms import RegistrationForm, LoginForm  # Імпортуємо форми реєстрації та логіну
from app.models import User  # Імпортуємо модель користувача
from flask_login import login_user, logout_user, login_required


# Створюємо blueprint для групи маршрутів, пов’язаних з аутентифікацією
auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])  # Маршрут для реєстрації
def register():
    form = RegistrationForm()  # Ініціалізуємо форму
    if form.validate_on_submit():  # Перевіряємо, чи форма була надіслана і коректна
        # Хешування пароля через bcrypt (варіант 1 - вручну):
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # Створення нового користувача з даними з форми.
        user = User(username=form.username.data, email=form.email.data)

        # Альтернативний спосіб – встановлення пароля через метод моделі (варіант 2):
        user.set_password(form.password.data)  # Метод сам хешує пароль

        db.session.add(user)  # Додаємо користувача до сесії бази даних
        db.session.commit()  # Зберігаємо зміни
        flash('Congratulations, you are now a registered user!', 'success')  # Повідомлення успіху
        return redirect(url_for('auth.login'))  # Переадресація на сторінку логіну
    return render_template('register.html', title='Register', form=form)  # Відображення шаблону


@auth.route('/login', methods=['GET', 'POST'])  # Маршрут для логіну
def login():
    form = LoginForm()  # Ініціалізація форми логіну
    if form.validate_on_submit():  # Перевірка форми
        user = User.query.filter_by(email=form.email.data).first()  # Пошук користувача за email

        # Перевірка пароля (варіант 1 — безпосередньо з bcrypt):
        # if user and bcrypt.check_password_hash(user.password, form.password.data):

        # Перевірка пароля (варіант 2 — через метод моделі, наприклад check_password())
        if user and user.check_password(form.password.data):
            login_user(user)  # Вхід користувача (потрібен імпорт login_user)
            flash('Login successful!', 'success')  # Повідомлення про успішний вхід
            return redirect(url_for('main.index'))  # Перенаправлення на головну
        flash('Invalid email or password', 'danger')  # Якщо логін або пароль невірні
    return render_template('login.html', title='Login', form=form)  # Відображення шаблону


@auth.route('/logout')  # Маршрут для виходу з акаунту
@login_required  # Декоратор, щоб тільки авторизовані користувачі могли вийти
def logout():
    logout_user()  # Вихід користувача (потрібен імпорт logout_user)
    flash('You have been logged out.', 'success')  # Повідомлення
    return redirect(url_for('main.index'))  # Перенаправлення на головну
