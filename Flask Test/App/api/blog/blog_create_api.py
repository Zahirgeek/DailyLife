from flask import g
from flask_restful import reqparse, Resource, abort, fields, marshal

from App.api.api_contant import HTTP_CREATE_OK
from App.api.blog.utils import login_required
from App.models.blog.blog_model import BlogModel

parse_blog = reqparse.RequestParser()
parse_blog.add_argument("title", type=str, required=True, help="请输入博客标题")
parse_blog.add_argument("content", type=str, required=True, help="请输入博客内容")

blog_fields = {
    "b_title": fields.String,
    "b_content": fields.String,
}


# 创建博客
class CreateBlogResource(Resource):

    @login_required
    def post(self):

        userid = g.user.id

        args = parse_blog.parse_args()

        blog = BlogModel()

        blog.b_title = args.get("title")
        blog.b_content = args.get("content")
        blog.b_user = userid

        if not blog.save():
            abort(400, msg="create fail")

        data = {
            "status": HTTP_CREATE_OK,
            "msg": "博客创建成功",
            "data": marshal(blog, blog_fields)
        }

        return data

