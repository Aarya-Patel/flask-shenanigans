from flask import Response, session
import functools


def require_auth(func):
  """Wraps the view to require a user to be logged in"""
  @functools.wraps(func)
  def auth_wrapper(*args, **kwargs):
    if 'username' not in session:
      return Response('Unathorized! Please log in to continue...', status=401)
    return func(*args, **kwargs)
  return auth_wrapper
