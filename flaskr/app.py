from flask import Flask, g
from flaskr.blueprints import auth
from flaskr.blueprints import admin
import os


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')


# Blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)


@app.route('/test')
def test():
  return 'Testing'


if __name__ == '__main__':
  app.run(debug=True)
