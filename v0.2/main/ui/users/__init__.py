from flask import Blueprint

bp = Blueprint('users_bp', __name__)

from . import routes