from flask import Flask, request, redirect, url_for
from flask_mail import Mail

from config import Configuration

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security, current_user


app = Flask(__name__, static_url_path='/templates/static')
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

mail = Mail(app)


###   ADMIN  ###
from models import *


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class AdminHomeView(AdminMixin, AdminIndexView):
    pass


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'tags', 'body']


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']


class UserAdminView(AdminMixin, BaseModelView):
    form_columns = ['id', 'full_name', 'login', 'password', 'email', 'active', 'roles']
    column_exclude_list = ('password', )


class MessageAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'email', 'title', 'text']


admin = Admin(app, 'FlaskApp', url='/blog', index_view=AdminHomeView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(UserAdminView(User, db.session))
admin.add_view(MessageAdminView(Messages, db.session))



###  FLASK SECURITY###

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
