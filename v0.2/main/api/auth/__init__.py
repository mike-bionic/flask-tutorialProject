from flask import Blueprint

api = Blueprint('auth_api', __name__)

from . import routes