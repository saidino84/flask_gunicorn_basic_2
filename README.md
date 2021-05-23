
just install flask

to run with python use:
python3 main.py

to run with gunicorn:
gunicorn --bind 0.0.0.0:5000 wsgi:gunicorn_app# flask_gunicorn_basic_2
