from flask import Blueprint


web = Blueprint(
    'web',
    __name__,
    template_folder='templates',
    static_url_path='static'
)

from . import views