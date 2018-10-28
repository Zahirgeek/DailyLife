from flask import g
from flask_restful import Resource, reqparse, fields, abort, marshal

from App.api.api_contant import HTTP_CREATE_OK
from App.api.user.utils import login_required
from App.models.user.user_model import BlogUser

blog_user_fields = {
    "username": fields.String,
    "password": fields.String(attribute="_password"),
    "phone": fields.String,
}

parse_patch = reqparse.RequestParser()
parse_patch.add_argument("username")
parse_patch.add_argument("password")
parse_patch.add_argument("phone")


class UsersPatchResource(Resource):

    @login_required
    def patch(self):
        args = parse_patch.parse_args()

        user = BlogUser.query.get(g.user.id)

        user.username = args.get("username") or user.username
        user.password = args.get("password") or user.password
        user.phone = args.get("phone") or user.phone

        if not user.save():
            abort(400, msg="修改信息失败")

        data = {
            "status": HTTP_CREATE_OK,
            "msg": "patch ok",
            "data": marshal(user, blog_user_fields),
        }

        return data