from flask import Blueprint, redirect, url_for

home_controller = Blueprint('home', __name__)


@home_controller.route('/')
def home():
    return redirect(url_for('login'))
