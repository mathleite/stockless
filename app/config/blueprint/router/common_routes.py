from flask import Blueprint
from datetime import datetime, timedelta, timezone

common_routes = Blueprint('common_routes', __name__)


@common_routes.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@common_routes.route('/health-check')
def health_check():
    current_date = datetime.today().astimezone(timezone(timedelta(hours=-3)))
    return {
        'status': 200,
        'datetime':  current_date.strftime('%Y-%m-%d %H:%M:%S')
    }
