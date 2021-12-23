from flask import Flask, g
from .blueprints import auth


app = Flask(__name__)

# Blueprints
app.register_blueprint(auth.bp)

if __name__ == '__main__':
  app.run(debug=True)
