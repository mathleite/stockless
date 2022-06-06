from flask import Flask
from config.blueprint.router.common_routes import common_routes
from config.database.database_connector import DatabaseConnector
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.register_blueprint(common_routes)
database = DatabaseConnector()
database.config(flask_app=app)
db = database.get_database()

# Uncomment to test database creation
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# db.create_all()
