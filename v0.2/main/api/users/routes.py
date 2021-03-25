from flask import make_response, jsonify

from . import api
from main.common.database import users, skills

@api.route("/users/")
def get_users():
	data = []
	for user in users:
		user_skills = [skill for skill in skills if skill["UId"] == user["UId"]]
		user["Skills"] = user_skills
		data.append(user)
	return make_response(jsonify(users))


@api.route("/users/<id>/")
def get_user(id):
	data = [user for user in users if user['UId'] == int(id)]
	if data:
		data[0]["Skills"] = [skill for skill in skills if skill["UId"] == data[0]["UId"]]
	return make_response(jsonify(data))