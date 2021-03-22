from datas import database

resources = database['Resources']
categories = database['Res_categories']
# print(resources)
for resource in resources:
	if resource['ResPriceVal'] <= 5000:
		resource["Description"] = "In arzan haryt"
	else:
		resource["Description"] = "Gymmat haryt"
	for category in categories:
		if category["ResCatId"] == resource['ResCatId']:
			resource["Category"] = category["ResCatName"]
	# print(resource)

ResId = 3
# resource = [resource for resource in resources if resource["ResId"] == ResId][0]

def resource(ResId):
	res = ''
	for resource in resources:
		if resource["ResId"] == ResId:
			res = resource
	return res

def resource_in_while(ResId):
	i = 0
	while resources[i]["ResId"] != ResId:
		i += 1
		# break
	res = resources[i]
	print(res)
	return res
	

b = resource_in_while(ResId)
print(b)
# print(resource)
# for resource in database

# print(result)