from flask import Blueprint, redirect, url_for

home_controller = Blueprint('home', __name__)


@home_controller.route('/')
def home():
    '''
    Redirect to login as home page
    '''
    return redirect(url_for('login'))
