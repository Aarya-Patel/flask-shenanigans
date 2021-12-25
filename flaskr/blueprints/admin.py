from flask import Blueprint, session, Response
from flaskr.db import Database
from flaskr.middlewares.auth import require_auth
import json

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/getallusers')
@require_auth
def get_all_users():
  db = Database()
  all_users = []
  for user in db.get_all_users():
    all_users.append(user[0])
  return Response(json.dumps(all_users), content_type='application/json')
