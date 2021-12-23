from flask import Blueprint, request, Response, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequestKeyError
from ..db import Database

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
      return Response(f'{user[0]} logged in', status=200)

  except BadRequestKeyError:
    return Response('Bad Request', status=400)

  return 'logging in'


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
    # db = Database()
    hashed_password = generate_password_hash(password)
    g.db.insert_user(username, hashed_password)
    # db.close()
  except Exception:
    return Response('User is already registered!', status=400)

  return 'User Registered!'
