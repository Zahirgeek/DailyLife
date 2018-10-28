from flask import g
from flask_restful import Resource, abort, fields, marshal

from App.api.api_contant import HTTP_OK
from App.api.user.utils import login_required
from App.models.blog.blog_model import BlogModel
from App.models.user.user_model import BlogUser
from App.models.user_blog_heart.heart_model import HeartModel

heart_fields = {
    "h_user": fields.Integer,
    "h_blog": fields.Integer,
}

blog_title_fields = {
    "b_title": fields.String,
}

user_fields = {
    "username": fields.String,
}

# 收藏
class CreateHeartResource(Resource):

    @login_required
    def get(self, blogid):

        heart = HeartModel()
        heart.h_blog = blogid
        heart.h_user = g.user.id

        if not heart.save():
            abort(400)

        data = {
            "status": HTTP_OK,
            "msg": "create ok",
            "data": marshal(heart, heart_fields)
        }

        return data


class GetHeartResource(Resource):

    def get(self, userid):

        user_hearts = HeartModel.query.filter(HeartModel.h_user==userid).all()

        hears_list = []

        for user_heart in user_hearts:

            hears_list.append(BlogModel.query.get(user_heart.h_blog))

        data = {
            "status": HTTP_OK,
            "msg": "get ok",
            "data": marshal(hears_list, blog_title_fields)
        }

        return data


class GetUsersResource(Resource):

    def get(self, blogid):

        heart_users = HeartModel.query.filter(HeartModel.h_blog==blogid).all()

        user_list = []

        for heart_user in heart_users:

            user_list.append(BlogUser.query.get(heart_user.h_user))

        data = {
            "status": HTTP_OK,
            "msg": "get ok",
            "data": marshal(user_list, user_fields)
        }

        return data


