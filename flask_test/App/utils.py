import uuid
'''
根据登录用户类型返回唯一token
'''
BLOG_USER = "blog_user"
ADMIN_USER = "admin_user"


def generate_token(prefix=None):
    token = prefix + uuid.uuid4().hex
    return token


def generate_blog_user_token():
    return generate_token(prefix=BLOG_USER)


def generate_admin_user_token():
    return generate_token(prefix=ADMIN_USER)
