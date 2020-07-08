from flask import Flask
from .admin import admin
from .web import web


app = Flask(__name__)

app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(web,url_prefix='/web')
