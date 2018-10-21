from flask import abort
from flask_restful import Resource, marshal, fields, marshal_with, reqparse

from App.models import Goods
# 模板
goods_fields = {
    "g_name": fields.String,
    "g_price": fields.Float,
}

list_fields = {
    "id": fields.Integer,
    "g_name": fields.String,
    "g_price": fields.Float,
    "uri": fields.Url("single_goods", absolute=True),
}

single_goods_fields = {
    "data": fields.Nested(goods_fields),
    "status": fields.Integer,
    "msg": fields.String
}

goods_list_fields = {
    "data": fields.List(fields.Nested(list_fields)),
    "status": fields.Integer,
    "msg": fields.String,
}

parser = reqparse.RequestParser()
# required=True必须提交字段
parser.add_argument("g_name", required=True, help="please input g_name", location="form")
parser.add_argument("g_price",type=float, required=True, help="please input g_price", location="form")

class GoodsListResource(Resource):
    # 获取全部商品
    @marshal_with(goods_list_fields)
    def get(self):

        goods_list = Goods.query.all()

        data = {
            "status": 200,
            "msg": "get success",
            "data": goods_list,
        }

        return data
    # 添加商品
    def post(self):

        # g_name = request.form.get("g_name")
        # g_price = request.form.get("g_price")

        args = parser.parse_args()

        g_name = args.get("g_name")
        g_price = args.get("g_price")

        goods = Goods()

        goods.g_name = g_name

        goods.g_price = g_price

        data = {
            "status": 201,
            "msg": "create success",
            "data": marshal(goods, goods_fields)
        }

        if not goods.save():

            abort(400)


        return data

class GoodsResource(Resource):

    # 获取单个商品信息
    @marshal_with(single_goods_fields)
    def get(self, id):

        goods = Goods.query.get(id)

        data = {
            "status": 200,
            "msg": "get success",
            "data": goods,
        }

        if not goods:
            return abort(404)

        return data

    # 删除商品
    def delete(self, id):

        goods = Goods.query.get(id)

        if not goods:
            data = {
                "status": 400,
                "msg": "goods doesn't exist",
            }
            return data

        if not goods.delete():
            data = {
                "status": 400,
                "msg": "fail",
            }
            return data

        data = {
            "status": 204,
            "msg": "delete success.",
        }
        return data

    # 更新
    def put(self, id):

        goods = Goods.query.get(id)

        # g_name = request.form.get("g_name")
        # g_price = request.form.get("g_price")

        args = parser.parse_args()
        g_name = args.get("g_name")
        g_price = args.get("g_price")

        if not goods:
            abort(404)

        goods.g_name = g_name
        goods.g_price = g_price

        if not goods.save():
            abort(400)

        data = {
            "status": 201,
            "msg": "put success",
            "data": marshal(goods, goods_fields)
        }

        return data

    # 差量更新(缺省值不会改变)
    @marshal_with(single_goods_fields)
    def patch(self, id):
        goods = Goods.query.get(id)

        # g_name = request.form.get("g_name")
        # g_price = request.form.get("g_price")
        args = parser.parse_args()

        g_name = args.get("g_name")
        g_price = args.get("g_price")

        if not goods:
            abort(404)

        goods.g_name = g_name or goods.g_name
        goods.g_price = g_price or goods.g_price

        if not goods.save():
            abort(400)

        data = {
            "status": 201,
            "msg": "patch success",
            "data": goods,
        }

        return data