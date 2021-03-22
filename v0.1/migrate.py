from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "sdfhlrhforiliriknvrer98oin"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ecommerce.db"

db = SQLAlchemy(app)

class Resources(db.Model):
	ResId = db.Column(db.Integer,nullable=False,primary_key=True)
	ResName = db.Column(db.String(100),nullable=False)
	ResPriceVal = db.Column(db.Float,default=0.0)
	ResCatId = db.Column(db.Integer,db.ForeignKey("res_categories.ResCatId"))

class Res_categories(db.Model):
	ResCatId = db.Column(db.Integer,nullable=False,primary_key=True)
	ResCatName = db.Column(db.String(100),nullable=False)
	Resources = db.relationship("Resources",backref="res_categories",lazy=True)

db.drop_all()
db.create_all()

from datas import database

for category in database['Res_categories']:
	new_category = Res_categories(**category)
	db.session.add(new_category)

for resource in database["Resources"]:
	new_resource = Resources(**resource)
	db.session.add(new_resource)

db.session.commit()
