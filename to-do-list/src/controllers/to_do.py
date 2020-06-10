from flask import Blueprint, request, render_template
from services.user import get_user
from services.to_do import save_task, delete_task, check_task

to_do_controller = Blueprint('to-do', __name__)


@to_do_controller.route('/to-do/<name>', methods=['POST', 'GET'])
def to_do(name):
    '''
    Route to get the tasks and post a task

    :param name: of the user
    '''
    user = get_user(name)
    if request.method == 'POST':
        return save_task(user, dict(request.get_json()))
    if request.method == 'GET':
        return render_template('to_do.html', user=user)


@to_do_controller.route('/to-do/<name>/<int:task_id>',
                        methods=['PATCH', 'DELETE'])
def task(name, task_id):
    '''
    Route to update or delete a task

    :param name: of the user

    :param task_id: of the task
    '''
    user = get_user(name)
    if request.method == 'DELETE':
        return delete_task(user, task_id)
    if request.method == 'PATCH':
        return check_task(user, task_id)
