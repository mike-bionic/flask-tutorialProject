from flask import Blueprint

api = Blueprint('resource_api', __name__)

from . import routes