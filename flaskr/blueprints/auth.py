from flask import Blueprint, request, Response, g, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequestKeyError
from flaskr.db import Database

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.before_request
def before_request():
  g.db = Database()


@bp.after_request
def after_request(response):
  if 'db' in g:
    db = g.pop('db')
    db.close()
  return response


@bp.route('/login', methods=['POST'])
def login():
  try:
    username = request.form['username']
    password = request.form['password']

    user = g.db.get_user(username)
    if user is None:
      return Response('User not found', status=404)
    elif check_password_hash(user[1], password):
      # Update the session and global for flask
      session.clear()
      session['username'] = user[0]

      return Response(f'{user[0]} logged in', status=200)

  except BadRequestKeyError:
    return Response('Bad Request', status=400)


@bp.route('/register', methods=['POST'])
def register():
  # Get form data
  try:
    username = request.form['username']
    password = request.form['password']
  except BadRequestKeyError:
    return Response('Bad Request', status=400)

  # Insert into the db
  try:
    hashed_password = generate_password_hash(password)
    g.db.insert_user(username, hashed_password)
  except Exception:
    return Response('User is already registered!', status=400)

  return 'User Registered!'


@bp.route('/logout', methods=['POST'])
def logout():
  username = session.get('username')
  session.clear()
  return Response(f'{username} logged out!') if username is not None else Response('No one is logged in!')
