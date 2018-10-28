from App.ext import db
from App.models import BaseModel
from App.models.user.user_model import BlogUser


class BlogModel(BaseModel):

    b_title = db.Column(db.String(64))
    b_content = db.Column(db.String(512))

    b_user = db.Column(db.Integer, db.ForeignKey(BlogUser.id))