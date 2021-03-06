from app import db
from datetime import datetime
import re

from flask_security import UserMixin, RoleMixin


def slugify(string):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', string)


post_tags = db.Table('post_tags',
                 db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                 db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    date = db.Column(db.TIMESTAMP, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        # self.slug = slugify(self.name)
        self.generate_slug()



    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return '{}'.format(self.name)


###   FLASK SECURITY  ###

roles_users = db.Table('roles_users',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                 db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    login = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('user', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        pass


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    title = db.Column(db.String(255))
    email = db.Column(db.String(100))
    text = db.Column(db.String(10000))












