from flask_restful import Resource, abort

from App.api.api_contant import HTTP_OK
from App.api.blog.utils import require_permission
from App.models.blog.blog_model import BlogModel


class BlogDeleteResource(Resource):

    @require_permission
    def delete(self, blogid):

        blog = BlogModel.query.get(blogid)

        if not blog:
            abort(400)

        if not blog.delete():
            abort(400)

        data = {
            "status": HTTP_OK,
            "msg": "delete ok",
        }

        return data