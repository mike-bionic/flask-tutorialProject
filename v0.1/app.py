from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datas import database

app = Flask(__name__)
app.config['SECRET_KEY'] = "sdfhlrhforiliriknvrer98oin"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ecommerce.db"

db = SQLAlchemy(app)

class Resources(db.Model):
	ResId = db.Column(db.Integer,nullable=False,primary_key=True)
	ResName = db.Column(db.String(100),nullable=False,unique=True)
	ResPriceVal = db.Column(db.Float,default=0.0)
	ResCatId = db.Column(db.Integer,db.ForeignKey("res_categories.ResCatId"))

class Res_categories(db.Model):
	ResCatId = db.Column(db.Integer,nullable=False,primary_key=True)
	ResCatName = db.Column(db.String(100),nullable=False)
	Resources = db.relationship("Resources",backref="res_categories",lazy=True)


@app.route("/login",methods=['GET','POST'])
def login():
	users = database["Users"]
	if request.method == 'GET':
		return render_template("/login.html",title="Ulgama gir!")
	elif request.method == 'POST':
		print(request.form)
		username = request.form['username']
		password = request.form['password']
		for user in users:
			if user["UName"] == username and user["UPass"] == password:
				return "Successfully logged in"
			else:
				return redirect('/login') 
				

@app.route("/")
def home():
	user = database['Users'][1]
	resources = Resources.query.all()
	categories = Res_categories.query.all()
	resources_data = []
	for resource in resources:
		this_resource_category = Res_categories.query.filter_by(ResCatId = resource.ResCatId).first()
		this_resource_category_name = this_resource_category.ResCatName
		data = {
			"ResName": resource.ResName,
			"ResPriceVal": resource.ResPriceVal,
			"Category": this_resource_category_name
		}
		resources_data.append(data)

	return render_template("main.html", title = "E-commerce!", user = user,
		resources = resources_data, categories = categories)

@app.route("/old/")
def home_old():
	user = database['Users'][1]
	resource = database['Resources'][1]["ResName"]
	print(resource)
	resources = database['Resources']
	categories = database["Res_categories"]
	
	for resource in resources:

		if resource['ResPriceVal'] <= 5000:
			resource["Description"] = "In arzan haryt"
		else:
			resource["Description"] = "Gymmat haryt"

		for category in categories:
			if category["ResCatId"] == resource['ResCatId']:
				resource["Category"] = category["ResCatName"]


	return render_template("/index.html",
		user=user,resources=resources,
		categories = categories)


# /product/2
@app.route("/product/<ResId>")
def product(ResId):
	ResId = int(ResId)
	resources = database['Resources']
	try:
		resource = [resource for resource in resources if resource["ResId"] == ResId][0]
	except:
		print("bug")

	this_resource = None
	
	for resource in resources:
		if resource["ResId"] == ResId:
			this_resource = resource
	
	if this_resource:
		print(f"this resource is {this_resource['ResName']} | {this_resource['ResPriceVal']}")
	else:
		print("resource not found")
		return "not found"
	print(resource)
	return render_template("/product.html",resource = resource, title=resource["ResName"])




# def calculate_price(price,tax):
# 	result = price - tax
# 	return result

# price = calculate_price(45,10)
# print(price)

if __name__=="__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)