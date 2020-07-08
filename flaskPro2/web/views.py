from . import web

@web.route('/home')
def home():
    return 'home'