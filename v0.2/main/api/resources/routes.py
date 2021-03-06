from flask import make_response, jsonify, request

from . import api
from main.models import Resource


@api.route("/products/")
def products():
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

	status_code = 200 if data else 404
	response = {
		"status": 1 if data else 0,
		"total": len(data),
		"message": "Resources",
		"data": data
	}

	return make_response(jsonify(response)), status_code


@api.route("/products/<int:id>")
def product(id):
	data = {}
	resource = Resource.query.filter_by(ResId = id).first()
	if resource:
		data = resource.to_json()
	
	status_code = 200 if data else 404
	response = {
		"status": 1 if data else 0,
		"total": 1 if data else 0,
		"message": "Resources",
		"data": data
	}

	return make_response(jsonify(response)), status_code