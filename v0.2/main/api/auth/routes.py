from flask import (
	jsonify,
	make_response,
	request
)
from . import api
from main.common.database import users

@api.route("/api/login/")
def api_login():
	UName = request.args.get('username',type=str)
	UPass = request.args.get('password',type=str)

	status_code = 401
	message = "Access denided, check username or password"

	user = [user for user in users if user["UName"] == UName]
	if user:
		user = user[0]
		if user["UPass"] == UPass:
			status_code = 200
			message = "Access granted"

	return make_response(jsonify({"message": message}), status_code)