from flask import (
	make_response,
	jsonify,
	request,
	render_template,
	flash,
	redirect,
	url_for
)

from main import db
from . import bp
from main.models import Users
from .forms import UserAddForm

@bp.route("/ulanyjylar", methods=['GET', 'POST'])
def users_page():
	users = Users.query.all()
	form = UserAddForm()
	if form.validate_on_submit():
		newUser = Users(
			username = form.username.data,
			age = form.age.data
		)
		db.session.add(newUser)
		db.session.commit()
		flash(f"{newUser.username} has been added!", "success")
		return redirect(url_for("users_bp.users_page"))
	
	form.username.data = ''
	form.age.data = ''

	return render_template(
		"users.html",
		users = users,
		form = form
	)

@bp.route("/ulanyjylar/<int:id>/delete")
def delete_user(id):
	# user = Users.query(id)
	user = Users.query.filter_by(id = id).first()
	db.session.delete(user)
	db.session.commit()
	flash(f"{user.username} has beed deleted", 'warning')
	return redirect (url_for('users_bp.users_page'))