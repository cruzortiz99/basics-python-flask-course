from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path


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
        return {"user_name": "Cruz"}
    return render_template('login.html')


@app.route('/to-do/<name>', methods=['POST', 'GET'])
def to_do(name):
    user = {
        'name': name,
        'tasks': [
            {
                'id': 1,
                'name': 'Name 1',
                'completed': False
            },
            {
                'id': 2,
                'name': 'Name 2',
                'completed': False
            },
            {
                'id': 3,
                'name': 'Name 3',
                'completed': True
            }
        ]
    }
    return render_template('to_do.html', user=user)


@app.route('/register', methods=['POST'])
def register():
    new_user = dict(request.get_json())
    return new_user


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
