from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

##################################################################################################
# Se usar o Schema público então a linha metadata_obj = MetaData(schema="peed") não é necessária,# 
# e assim pode substituir o metadata_obj por db.metadata no db.Table                             #
##################################################################################################
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/demo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#metadata_obj = MetaData(schema="peed")
db = SQLAlchemy(app)

table = db.Table('usuario', db.metadata, autoload=True, autoload_with=db.engine)