from flask_restful import Resource, abort

from App.api.api_contant import HTTP_OK
from App.api.user.utils import require_permission
from App.models.user.user_model import BlogUser


class UsersDeleteResource(Resource):

    @require_permission
    def delete(self, userid):

        user = BlogUser.query.get(userid)

        user.is_delete = True

        if not user.save():
            abort(410, msg="用户删除失败")

        data = {
            "status": HTTP_OK,
            "msg": "delete ok",
        }

        return data
