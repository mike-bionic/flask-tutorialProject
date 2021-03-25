from flask import Blueprint

bp = Blueprint('resource_bp', __name__)

from . import routes