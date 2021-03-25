from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from main.config import Config

db = SQLAlchemy()

def create_app(config_class = Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)

	from main.api.auth import api as auth_api
	app.register_blueprint(auth_api)

	from main.api.resources import api as resources_api
	app.register_blueprint(resources_api)
	
	from main.api.users import api as users_api
	app.register_blueprint(users_api)

	from main.ui.main import bp as main_bp
	app.register_blueprint(main_bp)
	
	from main.ui.resource import bp as resource_bp
	app.register_blueprint(resource_bp)

	from main.ui.users import bp as users_bp
	app.register_blueprint(users_bp)


	return app