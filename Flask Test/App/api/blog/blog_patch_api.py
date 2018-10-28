from flask import g
from flask_restful import Resource, reqparse, abort, fields

from App.api.api_contant import HTTP_OK
from App.api.blog.utils import login_required
from App.models.blog.blog_model import BlogModel

parse_blog = reqparse.RequestParser()
parse_blog.add_argument("title", type=str)
parse_blog.add_argument("content", type=str)

blog_patch_fields = {
    "b_title": fields.String,
    "b_content": fields.String,
}


class BlogPatchResource(Resource):

    @login_required
    def patch(self, blogid):

        args = parse_blog.parse_args()

        blog = BlogModel.query.get(blogid)

        blog.b_title = args.get("title") or blog.b_title
        blog.b_content = args.get("content") or blog.b_content

        if not (blog.b_user == g.user.id or g.user.check_permission()):

            abort(403)

        if not blog.save():

            abort(400, msg="修改失败")

        data = {
            "status": HTTP_OK,
            "msg": "patch ok"
        }

        return data
