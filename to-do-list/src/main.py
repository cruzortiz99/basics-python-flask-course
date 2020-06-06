from flask import Flask, render_template, request, redirect, url_for, abort
from pathlib import Path
from json import load, dump, dumps


resources_folder = Path(__file__).parent.joinpath('resources')

app = Flask(
    __name__,
    template_folder=resources_folder.joinpath('templates'),
    static_url_path='/static',
    static_folder=str(resources_folder))


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.get_json()['name']
        return list(filter(lambda user: user['name'] == name, load(
            open(Path(__file__).parent.joinpath('db', 'user.json')))))[0]
    return render_template('login.html')


@app.route('/to-do/<name>', methods=['POST', 'GET'])
def to_do(name):
    user = list(filter(lambda user: user['name'] == name, load(
        open(Path(__file__).parent.joinpath('db', 'user.json')))))[0]
    if request.method == 'POST':
        db_users = load(
            open(
                Path(__file__).parent.joinpath(
                    'db',
                    'user.json')))
        user = list(
            filter(
                lambda db_user: db_user['name'] == name,
                db_users))[0]
        higher_db_task_id = sorted(
            user['tasks'],
            key=lambda task: task['id'],
            reverse=True)
        user['tasks'].append({
            'id': higher_db_task_id[0]['id'] + 1 if len(higher_db_task_id) > 0 else 0,
            'name': dict(request.get_json())['name'],
            'completed': False
        })
        users = [user for user in db_users if user['name'] != name]
        users.append(user)
        dump(
            users,
            open(
                Path(__file__).parent.joinpath(
                    'db',
                    'user.json'),
                mode='w'))
        return dumps(users)
    if request.method == 'GET':
        return render_template('to_do.html', user=user)


@app.route('/to-do/<name>/<int:task_id>', methods=['PATCH', 'DELETE'])
def task(name, task_id):
    if request.method == 'DELETE':
        db_users = load(
            open(
                Path(__file__).parent.joinpath(
                    'db',
                    'user.json')))
        user = list(filter(lambda user: user['name'] == name, db_users))[0]
        user['tasks'] = list(
            filter(
                lambda task: task['id'] != task_id,
                user['tasks']))
        users = [db_user for db_user in db_users if db_user['name'] != name]
        users.append(user)
        dump(users, open(
            Path(__file__).parent.joinpath(
                'db',
                'user.json'), mode='w'))
        return {'deleted': True}
    if request.method == 'PATCH':
        db_users = load(
            open(
                Path(__file__).parent.joinpath(
                    'db',
                    'user.json')))
        user = list(filter(lambda user: user['name'] == name, db_users))[0]

        def checkTask(task_id):
            def taskChecker(task):
                if task['id'] == task_id:
                    task['completed'] = not task['completed']
                return task
            return taskChecker

        user['tasks'] = list(
            map(
                checkTask(task_id),
                user['tasks']))
        users = [db_user for db_user in db_users if db_user['name'] != name]
        users.append(user)
        dump(users, open(
            Path(__file__).parent.joinpath(
                'db',
                'user.json'), mode='w'))
        return {'updated': True}


@app.route('/register', methods=['POST'])
def register():
    new_user = {
        'name': dict(request.get_json())['name'],
        'tasks': []
    }
    db_users = load(open(Path(__file__).parent.joinpath('db', 'user.json')))
    if len([db_user for db_user in db_users if db_user['name'] == new_user['name']]):
        return abort(403)
    db_users.append(new_user)
    dump(
        db_users,
        open(
            Path(__file__).parent.joinpath(
                'db',
                'user.json'),
            mode='w'))
    return new_user


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
