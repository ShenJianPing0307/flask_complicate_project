from . import admin

@admin.route('/home')
def home():
    return 'home'