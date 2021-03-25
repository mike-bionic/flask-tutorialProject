from main import db, create_app
from main.models import (
	Resource,
	Users
)

app = create_app()
app.app_context().push()

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