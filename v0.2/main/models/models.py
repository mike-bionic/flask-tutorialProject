from main import db
class ResCategory(db.Model):
	ResCatId = db.Column("ResCatId",db.Integer, primary_key=True)
	ResCatName = db.Column("ResCatName",db.String(100))
	Resource = db.relationship("Resources", backref="rescategory", lazy=True)
	


class Resource(db.Model):
	__tablename__ = 'tbl_dk_resource'
	ResId = db.Column("ResId",db.Integer, primary_key=True)
	ResCatId = db.Column("ResCatId", db.ForeignKey("ResCategory.ResCatId"))
	BrandId = db.Column("BrandId",db.Integer)
	UsageStatusId = db.Column("UsageStatusId",db.Integer)
	ResRegNo = db.Column("ResRegNo", db.String)
	ResName = db.Column("ResName", db.String)
	ResDesc = db.Column("ResDesc", db.String)
	ResFullDesc = db.Column("ResFullDesc", db.String)


	def to_json(self):
		data = {
			"ResId": self.ResId,
			"ResCatId": self.ResCatId,
			"BrandId": self.BrandId,
			"UsageStatusId": self.UsageStatusId,
			"ResRegNo": self.ResRegNo,
			"ResName": self.ResName,
			"ResDesc": self.ResDesc,
			"ResFullDesc": self.ResFullDesc
		}
		return data


class Users(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String)
	age = db.Column(db.Integer)


