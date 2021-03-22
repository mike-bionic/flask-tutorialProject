from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///accounting.db"

class Resource(db.Model):
	__tablename__ = 'tbl_dk_resource'
	ResId = db.Column("ResId",db.Integer, primary_key=True)
	ResCatId = db.Column("ResCatId",db.Integer)
	BrandId = db.Column("BrandId",db.Integer)
	UsageStatusId = db.Column("UsageStatusId",db.Integer)
	ResRegNo = db.Column("ResRegNo", db.String)
	ResName = db.Column("ResName", db.String)
	ResDesc = db.Column("ResDesc", db.String)
	ResFullDesc = db.Column("ResFullDesc", db.String)

class Users(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String)
	age = db.Column(db.Integer)

db.drop_all()
db.create_all()


resource = Resource()
resource.ResName = "hello"

db.session.add(resource)
db.session.commit()


user = Users()
user.username = "mike"
user.age = 22
db.session.add(user)
db.session.commit()


user = Users()
user.username = "mekan"
user.age = 21
db.session.add(user)
db.session.commit()