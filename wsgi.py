'''
to wiyh gunicorn :
gunicorn --bind 0.0.0.0:5000 wsgi:gunicorn_app
'''

from app.server.instance import  server
from app.controllers import *


if __name__ == '__main__':
    server.run()
else:
    gunicorn_app=server.app