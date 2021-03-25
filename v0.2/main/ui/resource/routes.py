from flask import (
	request,
	render_template
)

from . import bp
from main.models import Resource


@bp.route("/harytlar")
def products_page():
	ResId = request.args.get('id', None, type=int)
	ResCatId = request.args.get('categoryId', None, type=int)
	data = []

	if ResId:
		resources = Resource.query.filter_by(ResId = ResId).all()
	
	if ResCatId:
		resources = Resource.query.filter_by(ResCatId = ResCatId).all()
	else:
		resources = Resource.query.all()

	data = [resource.to_json() for resource in resources]


	return render_template(
		"products.html",
		resources = data
	)