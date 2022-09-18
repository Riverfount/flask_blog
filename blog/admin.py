from datetime import datetime
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required
from slugify import slugify
from wtforms import form, fields, validators
from blog.database import mongo

# Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)


class PostsForm(form.Form):
    title = fields.StringField('Title', [validators.data_required()])
    slug = fields.HiddenField('Slug')
    content = fields.TextAreaField('Content')
    published = fields.BooleanField('Published', default=True)


class AdminPosts(ModelView):
    column_list = ('title', 'slug', 'published', 'date')
    form = PostsForm

    def on_model_change(self, form, model, is_created):
        model['slug'] = slugify(model['title'])
        # Todo: Verificar se o slug já existe!
        if is_created:
            model['date'] = datetime.now()


def init_app(app):
    admin = Admin(app, name=app.config.get('TITLE'), template_mode="bootstrap4")
    admin.add_view(AdminPosts(mongo.db.post, 'Posts'))
