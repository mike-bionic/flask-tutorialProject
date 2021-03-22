from .database import users, skills

def get_user_data():
	data = []
	for user in users:
		user_skills = [skill for skill in skills if skill["UId"] == user["UId"]]
		user["Skills"] = user_skills
		data.append(user)

	return data