from flask_restful import Api

from App.api.blog.blog_create_api import CreateBlogResource
from App.api.blog.blog_delete_api import BlogDeleteResource
from App.api.blog.blog_patch_api import BlogPatchResource

blog_api = Api(prefix="/blog")

# 博客创建
blog_api.add_resource(CreateBlogResource, "/createblog/")
# 博客修改
blog_api.add_resource(BlogPatchResource, "/patchblog/<int:blogid>/")
# 博客删除
blog_api.add_resource(BlogDeleteResource, "/deleteblog/<int:blogid>/")