from json import dump, load, dumps
from pathlib import Path
from models.user import User
from models.task import Task
from utils import get_db_rows, save_into_db

get_db_user_from_db_userjson = get_db_rows(
    Path(__file__).parent.parent.joinpath(
        'db', 'user.json'))

save_user_into_db_userjson = save_into_db(
    Path(__file__).parent.parent.joinpath(
        'db', 'user.json'))


def save_task(user, new_task):
    db_users = get_db_user_from_db_userjson()
    user['tasks'].append(
        Task(
            name=new_task['name'],
            completed=False
        )
    )
    new_users = [
        db_user for db_user in db_users if db_user['name'] != user['name']]
    new_users.append(user)

    save_user_into_db_userjson(new_users)
    return dumps(new_users)


def delete_task(user, task_id):
    db_users = get_db_user_from_db_userjson()
    user['tasks'] = list(
        filter(
            lambda task: task['id'] != task_id,
            user['tasks']))
    new_users = [
        db_user for db_user in db_users if db_user['name'] != user['name']]
    new_users.append(user)
    save_user_into_db_userjson(new_users)
    return {'deleted': True}


def check_task(user, task_id):
    db_users = get_db_user_from_db_userjson()
    user['tasks'] = list(map(lambda task: Task(name=task['name'],
                                               completed=not task['completed'],
                                               id=task['id']) if task['id'] == task_id else task,
                             user['tasks']))
    new_users = [
        db_user for db_user in db_users if db_user['name'] != user['name']]
    new_users.append(user)
    save_user_into_db_userjson(new_users)
    return {'updated': True}
