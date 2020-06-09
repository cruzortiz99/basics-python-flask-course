from flask import Flask, render_template, request, redirect, url_for, abort
from pathlib import Path
from json import load, dump, dumps
from services.user import get_user, register_user
from services.to_do import save_task, delete_task, check_task


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
        return get_user(name)
    return render_template('login.html')


@app.route('/to-do/<name>', methods=['POST', 'GET'])
def to_do(name):
    user = get_user(name)
    if request.method == 'POST':
        return save_task(user, dict(request.get_json()))
    if request.method == 'GET':
        return render_template('to_do.html', user=user)


@app.route('/to-do/<name>/<int:task_id>', methods=['PATCH', 'DELETE'])
def task(name, task_id):
    user = get_user(name)
    if request.method == 'DELETE':
        return delete_task(user, task_id)
    if request.method == 'PATCH':
        return check_task(user, task_id)


@app.route('/register', methods=['POST'])
def register():
    new_user = register_user(dict(request.get_json()))
    return new_user


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
