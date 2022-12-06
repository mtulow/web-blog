from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import database_uri


# create the app
app = Flask(__name__)
# configure the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri()
# create the extension
db = SQLAlchemy(app)



@app.route('/')
def hello():
	return "Hello, Docker!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)