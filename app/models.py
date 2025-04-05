from datetime import datetime
from app import db  # Імпортуємо об'єкт db із нашого додатку
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Унікальний ID користувача
    username = db.Column(db.String(80), unique=True, nullable=False)  # Унікальне ім'я
    email = db.Column(db.String(120), unique=True, nullable=False)  # Унікальний email
    password_hash = db.Column(db.String(128), nullable=False) # Хеш пароля

    def set_password(self, password):
        """Хешуємо пароль перед збереженням"""
        self.password_hash = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Перевіряємо пароль"""
        return check_password_hash(self.password_hash, password)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Унікальний ID задачі
    title = db.Column(db.String(80), unique=False, nullable=False)  # Назва задачі
    is_done = db.Column(db.Boolean, default=False)  # Статус задачі (True або False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Прив’язка до User, Поле для зовнішнього ключа (зв'язок із таблицею користувачів)

    def __repr__(self):
        return f"<Task {self.title}"

