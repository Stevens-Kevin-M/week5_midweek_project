from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask_migrate import Migrate
from ship_inventory.models import db as root_db, login_manager, ma
from flask_sqlalchemy import SQLAlchemy


# CORS - Cross Origin Resource Sharing
from flask_cors import CORS

from ship_inventory.helpers import JSONEncoder

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app)
ma.init_app(app)
CORS(app)

app.json_encoder = JSONEncoder

# Specifying a route for non-authorized users
login_manager.login_view = 'signin' 
from ship_inventory import models