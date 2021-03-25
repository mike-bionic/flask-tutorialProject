class Config:
	FLASK_ENV = 'development'
	TESTING = True
	SECRET_KEY = "asdlfkhyueflbawkueyfhklaskdvjfsnadIUGxee3r"
	# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/dbSapHasap'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///accounting.db'