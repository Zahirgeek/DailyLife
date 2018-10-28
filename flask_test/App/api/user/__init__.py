from flask_restful import Api

from App.api.user.heart_api import CreateHeartResource, GetHeartResource, GetUsersResource
from App.api.user.user_api import BlogUsersResource
from App.api.user.user_delete_api import UsersDeleteResource
from App.api.user.user_patch_api import UsersPatchResource

user_api = Api(prefix="/user")

# 用户登录,注册
user_api.add_resource(BlogUsersResource, "/blogusers/")
# 用户信息修改
user_api.add_resource(UsersPatchResource, "/userpatch/")
# 用户逻辑删除
user_api.add_resource(UsersDeleteResource, "/userdelete/<int:userid>/")

# 收藏
user_api.add_resource(CreateHeartResource, "/createheart/<int:blogid>/")
# 获取某用户的所有收藏
user_api.add_resource(GetHeartResource, "/gethearts/<int:userid>/")
# 获取收藏某博客的所有用户
user_api.add_resource(GetUsersResource, "/getheartusers/<int:blogid>/")