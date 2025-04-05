from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy() # підключення бібліотеки
login_manager = LoginManager() # підключення логін менеджера
bcrypt = Bcrypt() # підключення кріптографії

def create_app():
    app = Flask(__name__)  # Створюємо екземпляр Flask-додатку
    app.config.from_object('app.config.Config')  # Завантажуємо конфігурацію

    db.init_app(app)  # Ініціалізуємо SQLAlchemy
    Migrate(app, db)  # Підключаємо Flask-Migrate
    login_manager.init_app(app) # ініціалізація логінменеджера
    bcrypt.init_app(app) # ініціалізація криптографії

    login_manager.login_view = 'auth.login'  # Сторінка входу для неавторизованих користувачів

    # Імпорт blueprint'ів
    from app.routes import main
    from app.auth import auth

    # Реєстрація blueprint'ів
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")

    return app

# Функція завантаження користувача для Flask-Login
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
