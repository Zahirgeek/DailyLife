from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.apis import init_blue, init_api


def create_app(env):

    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(envs.get(env))

    # 初始化第三方
    init_ext(app)

    # 初始化路由
    # init_blue(app)

    init_api(app=app)

    return app
