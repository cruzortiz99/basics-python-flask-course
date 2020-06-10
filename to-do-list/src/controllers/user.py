from flask import Blueprint, request, render_template, make_response
from services.user import get_user, register_user

user_controller = Blueprint('user', __name__)


@user_controller.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Render home page
    '''
       if request.method == 'POST':
            name = request.get_json()['name']
            return get_user(name)
        return render_template('login.html')


@user_controller.route('/register', methods=['POST'])
def register():
    '''
    Route to register a user
    '''
    try:
        new_user = register_user(dict(request.get_json()))
        return new_user
    except Exception:
        return make_response({'message': 'User already exists'}, 403)
