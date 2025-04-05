from flask import Blueprint

# Створюємо blueprint для "головної" частини сайту
main = Blueprint('main', __name__)

@main.route('/')  # Головна сторінка — маршрут "/"
def index():
    # Просто повертаємо HTML-текст
    return '<h1>Hello, World!</h1>'
