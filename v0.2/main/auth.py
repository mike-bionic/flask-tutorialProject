from flask import (
	jsonify,
	make_response,
	request,
	render_template,
	flash,
	redirect,
	url_for
)

from . import app
from .database import users
from .forms import LoginForm

@app.route("/api/login/")
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


@app.route("/login/", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		status_code = 401
		message_style = "danger"

		message = "Access denided, check username or password"

		user = [user for user in users if user["UName"] == form.username.data]
		if user:
			user = user[0]
			if user["UPass"] == form.password.data:
				status_code = 200
				message = "Access granted"
				message_style = 'success'
				flash(message, message_style)
				return redirect(url_for('index'))
		
		flash(message, message_style)

	return render_template(
		'auth/login.html',
		form = form
	)