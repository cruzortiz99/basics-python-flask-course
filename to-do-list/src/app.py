from flask import Flask, render_template, request, redirect, url_for, abort, make_response
from pathlib import Path
from controllers.to_do import to_do_controller
from controllers.user import user_controller
from controllers.home import home_controller

resources_folder = Path(__file__).parent.joinpath('resources')

app = Flask(
    __name__,
    template_folder=resources_folder.joinpath('templates'),
    static_url_path='/static',
    static_folder=str(resources_folder))

app.register_blueprint(to_do_controller)
app.register_blueprint(user_controller)
app.register_blueprint(home_controller)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
