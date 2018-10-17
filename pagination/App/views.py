import random

from flask import Blueprint, request, render_template

from App.ext import db
from .models import User

blue = Blueprint('blue', __name__,template_folder='../templates',url_prefix='/user')


def init_blue(app):
    app.register_blueprint(blue)

# 添加数据
@blue.route('/usersadd/')
def usersadd():

    for i in range(50):
        user = User()
        user.u_name = "xiao%d" % random.randrange(100000)
        user.u_age = random.randint(1, 100)

        db.session.add(user)

    db.session.commit()

    return 'user创建完成'

# test
@blue.route('/getusers/')
def getusers():

    # page = request.args.get('page', 1, int)
    #
    # per_page = request.args.get('per_page', 5, int)
    # users = User.query.offset(per_page * (page-1)).limit(per_page)
    #
    # return render_template('users.html', users=users)

    users = User.query.paginate().items

    return render_template('users.html', users=users)


    # pagination = User.query.paginate()
    #
    # per_page = request.args.get('per_page', 5, type=int)
    #
    # return render_template('users.html', pagination=pagination, per_page=per_page)

@blue.route('/getbaseusers/')
def getbaseusers():

    pagination = User.query.paginate()
    # 默认一页显示10条数据
    per_page = request.args.get('per_page', 10, type=int)

    users = User.query.paginate().items

    return render_template('baseusers.html', users=users, pagination=pagination, per_page=per_page)

