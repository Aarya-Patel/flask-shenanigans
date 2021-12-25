import os
import psycopg2
from psycopg2.errors import UniqueViolation


class Database():
  def __init__(self):
    try:
      self.conn = psycopg2.connect(
          host=os.environ.get('PSQL_HOST'),
          dbname=os.environ.get('PSQL_DBNAME'),
          user=os.environ.get('PSQL_USER'),
          password=os.environ.get('PSQL_PASSWORD')
      )
    except Exception:
      raise Exception

  def insert_user(self, username, password):
    """Insert a user into the table"""
    # Using 'with' will create a transaction that will automatically be commited on success
    with self.conn as conn:
      with conn.cursor() as cur:
        try:
          cur.execute(
              'INSERT INTO Users (username, password) VALUES (%s,%s)', (username, password))
        except UniqueViolation:
          raise UniqueViolation

  def get_user(self, username):
    """Finds the user with the given username"""
    with self.conn as conn:
      with conn.cursor() as cur:
        cur.execute('SELECT * FROM Users WHERE username = %s', (username,))
        data = cur.fetchone()
        return data

  def get_all_users(self):
    """Gets all the users within the db"""
    with self.conn as conn:
      with conn.cursor() as cur:
        cur.execute('SELECT username FROM Users')
        data = cur.fetchall()
        return data

  def close(self):
    """Close the db connection"""
    self.conn.close()
