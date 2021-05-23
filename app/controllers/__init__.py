from flask import Blueprint
from app.server.instance import server

@server.app.route("/")
def index():
        return 'wau its function two'

@server.app.route('/get_it')
def get_it():
    return 'Your ill get it all'