from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.event import remove

from app.models import Task
from app import db
from app.forms import TaskForm

# Створюємо blueprint
tasks = Blueprint('tasks', __name__)
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@tasks.route('/tasks')
@login_required
def tasks_list():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)


@tasks.route('/tasks/add', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, is_done=form.is_done.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully', 'success')
        return redirect(url_for('tasks.tasks_list'))
    return render_template('task_form.html', form=form)


@tasks.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('You do not have permission to edit this task.', 'danger')
        return redirect(url_for('tasks.tasks_list'))

    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.is_done = form.is_done.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks.tasks_list'))
    return render_template('task_form.html', form=form, task=task)


@tasks.route('/tasks/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):  # Удаление задачи
    task = Task.query.get_or_404(task_id)  # Получаем задачу по ID
    if task.user_id != current_user.id:  # Проверяем, принадлежит ли задача текущему пользователю
        flash('You do not have permission to delete this task.', 'danger')
        return redirect(url_for('tasks.tasks_list'))

    db.session.delete(task)  # Удаляем задачу из базы данных
    db.session.commit()  # Сохраняем изменения
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('tasks.tasks_list'))



