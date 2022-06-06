from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv


class DatabaseConnector:
    def __init__(self):
        self.database = None

    def config(self, flask_app: Flask):
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = self.get_database_uri()
        self.database = SQLAlchemy(app=flask_app)

    @staticmethod
    def get_database_uri():
        host = getenv('DATABASE_HOST')
        user = getenv('POSTGRES_USER')
        password = getenv('POSTGRES_PASSWORD')
        schema = getenv('POSTGRES_DB')
        port = getenv('DATABASE_PORT')
        return f'postgresql://{user}:{password}@{host}:{port}/{schema}'

    def get_database(self) -> SQLAlchemy:
        return self.database
