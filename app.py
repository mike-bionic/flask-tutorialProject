from flask import Flask, render_template, request, redirect

from datas import database

app = Flask(__name__)

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
	resource = [resource for resource in resources if resource["ResId"] == ResId][0]
	print(resource)
	return render_template("/product.html",resource = resource, title=resource["ResName"])




# def calculate_price(price,tax):
# 	result = price - tax
# 	return result

# price = calculate_price(45,10)
# print(price)

if __name__=="__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)