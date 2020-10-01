from flask import Flask, render_template

from datas import database

app = Flask(__name__)

@app.route("/")
def home():
	user = database['Users'][1]
	resource = database['Resources'][1]["ResName"]
	print(resource)
	resources = database['Resources']
	
	filtered_resources = []
	for resource in resources:
		if resource['ResPriceVal'] >= 5000:
			filtered_resources.append(resource)
	return render_template("/index.html",
		user=user,resources=resources,filtered_resources=filtered_resources)




# def calculate_price(price,tax):
# 	result = price - tax
# 	return result

# price = calculate_price(45,10)
# print(price)

if __name__=="__main__":
	app.run(host="0.0.0.0",debug=True)