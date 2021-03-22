from flask import (
	jsonify,
	make_response,
	request,
	render_template	
)

from . import app
from .database import users, skills
from .utils import get_user_data

@app.route("/")
def index():
	message = "welcome to my web"
	user_data = get_user_data()
	return render_template(
		'index.html',
		message = message,
		users = user_data)


@app.route("/main")
@app.route("/home")
def home_page():
	data = {
		"message": "welcome to home page",
		"status": "ok"
	}
	return make_response(jsonify(data))


@app.route("/users/")
def get_users():
	data = []
	for user in users:
		user_skills = [skill for skill in skills if skill["UId"] == user["UId"]]
		user["Skills"] = user_skills
		data.append(user)
	return make_response(jsonify(users))


@app.route("/users/<id>/")
def get_user(id):
	data = [user for user in users if user['UId'] == int(id)]
	if data:
		data[0]["Skills"] = [skill for skill in skills if skill["UId"] == data[0]["UId"]]
	return make_response(jsonify(data))


# 200 - ok
# 201 - inserted
# 404 - not Fi
# 400 - bad request
# 401 - auth denied
# 403 - forbidden
# 500 - server
# 302 - redirect
