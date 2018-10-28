from App.ext import db
from App.models import BaseModel
from App.models.blog.blog_model import BlogModel
from App.models.user.user_model import BlogUser


class HeartModel(BaseModel):

    h_user = db.Column(db.Integer, db.ForeignKey(BlogUser.id))
    h_blog = db.Column(db.Integer, db.ForeignKey(BlogModel.id))