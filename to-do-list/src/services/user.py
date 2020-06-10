from pathlib import Path
from json import load, dump
from models.user import User
from utils import get_db_rows, save_into_db

get_db_user_from_db_userjson = get_db_rows(
    Path(__file__).parent.parent.joinpath(
        'db', 'user.json'))
save_users_into_db_userjson = save_into_db(
    Path(__file__).parent.parent.joinpath(
        'db', 'user.json'))


def get_user(name):
    '''
    Get user by name

    :param name: of the user
    '''
    return list(
        filter(
            lambda user: user['name'] == name,
            get_db_user_from_db_userjson()))[0]


def register_user(user_data):
    '''
    Register a new user

    :param user_data: dictionary model of the data sent
    '''
    new_user = User(name=user_data['name']).__dict__
    db_users = get_db_user_from_db_userjson()
    if len([db_user for db_user in db_users if db_user['name'] == new_user['name']]):
        raise Exception([('message', 'User already exists')])
    db_users.append(new_user.__dict__)
    save_users_into_db_userjson(db_users)
    return new_user
