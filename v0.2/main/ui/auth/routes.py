from flask import flash, redirect, render_template, url_for

from . import bp
from .forms import LoginForm
from main.common.database import users

@bp.route("/login/", methods=["GET", "POST"])
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
				return redirect(url_for('main_bp.index'))
		
		flash(message, message_style)

	return render_template(
		'auth/login.html',
		form = form,
		title = "Login"
	)