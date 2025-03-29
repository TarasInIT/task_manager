from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return '<h1>Hello, World!</h1>'

"""
🔹 Можливі покращення
 - Вивід усіх задач у веб-інтерфейсі
 - Форма для додавання нової задачі
 - Зміна статусу задачі (зроблена/незроблена)
 - Видалення задачі

from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Task

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()  # Отримуємо всі задачі
    return render_template('index.html', tasks=tasks)  # Відправляємо у шаблон

@main.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, is_done=False, user_id=1)  # user_id = 1 тимчасово
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.is_done = not task.is_done  # Перемикаємо статус
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))
"""