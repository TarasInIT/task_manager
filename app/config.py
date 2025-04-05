import os  # Імпортуємо модуль os для роботи із змінними середовища

class Config:

    '''Зараз SECRET_KEY заданий прямо в коді, що не дуже безпечно. Краще використовувати .env файл або передавати через змінні середовища.
    # SECRET_KEY = os.getenv('SECRET_KEY', 'mysupersecretkey')  # Беремо ключ із змінної середовища'''


    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysupersecretkey') # Секретний ключ для безпеки додатку (наприклад, для сесій і CSRF-захисту)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db' # Встановлюємо URI бази даних (у цьому випадку використовується SQLite)
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Вимикаємо відстеження змін у SQLAlchemy для оптимізації продуктивності
