from flask import Flask
from flask_restful import Api
from cassandra.cqlengine import connection
from config import app_config
from catalog.restful.catalog import Catalog
from catalog.restful.catalogs import Catalogs
#from cassandra.cqlengine.management import sync_table
#from catalog.models.catalog import Catalog as db
#sync_table(db)
# config_name = os.getenv('APP_ENVIRON')
config_name = "development"
catalog_app = Flask(__name__)
catalog_app.config.from_object(app_config[config_name])
connection.setup([catalog_app.config['DATABASE_HOST']], catalog_app.config['DATABASE_KEYSPACE'], protocol_version=3)

api = Api(catalog_app)
api.add_resource(Catalogs, '/catalog')
api.add_resource(Catalog, '/catalog/<string:catalog_id>')
