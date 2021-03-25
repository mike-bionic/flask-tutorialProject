from flask import Blueprint

api = Blueprint('users_api', __name__)

from . import routes