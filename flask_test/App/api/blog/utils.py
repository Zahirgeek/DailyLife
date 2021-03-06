from flask import request, abort, g

from App.api.user.model_utils import get_user
from App.ext import cache
from App.utils import BLOG_USER


def _verify():
    token = request.args.get("token")

    if not token:
        abort(401, msg="not login")

    if not token.startswith(BLOG_USER):
        abort(403, msg="no access")

    user_id = cache.get(token)

    if not user_id:
        abort(401)

    user = get_user(user_id)

    if not user:
        abort(401, msg="user not avaliable")

    g.user = user
    g.auth = token


# 验证是否登录
def login_required(func):

    def wrapper(*args, **kwargs):

        _verify()

        return func(*args, **kwargs)

    return wrapper


# 验证管理员权限
def require_permission(func):
    def wrapper(*args, **kwargs):

        _verify()

        if not g.user.check_permission():
            abort(403)

        return func(*args, **kwargs)

    return wrapper

