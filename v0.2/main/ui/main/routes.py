from flask import (
	jsonify,
	make_response,
	request,
	render_template	
)

from . import bp
from main.common.database import users, skills
from main.common.utils import get_user_data


@bp.route("/")
def index():
	message = "welcome to my web"
	user_data = get_user_data()
	return render_template(
		'index.html',
		message = message,
		users = user_data)


@bp.route("/main")
@bp.route("/home")
def home_page():
	data = {
		"message": "welcome to home page",
		"status": "ok"
	}
	return make_response(jsonify(data))