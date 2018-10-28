from App.api.blog import blog_api
from App.api.user import user_api


def init_api(app):
    user_api.init_app(app)
    blog_api.init_app(app)