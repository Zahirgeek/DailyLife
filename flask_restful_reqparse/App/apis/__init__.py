from flask_restful import Api

from App.apis.goods_api import GoodsListResource, GoodsResource

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(GoodsListResource,"/goods/")
api.add_resource(GoodsResource, "/getgoods/<int:id>/", endpoint="single_goods")
