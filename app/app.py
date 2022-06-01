from flask import Flask
from config.blueprint.router.common_routes import common_routes

app = Flask(__name__)
app.register_blueprint(common_routes)
