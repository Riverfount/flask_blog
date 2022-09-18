from flask import Flask, Blueprint, abort, redirect, render_template, request, url_for

from blog.posts import get_all_posts, get_post_by_slug, new_post, update_post_by_slug

bp = Blueprint("post", __name__, template_folder="templates")


@bp.route('/')
def index():
    posts = get_all_posts()
    return render_template('index.html.j2', posts=posts)


@bp.route('/<string:slug>')
def detail(slug):
    post = get_post_by_slug(slug)
    if not post:
        return abort(404, 'Not Found.')
    return render_template('post.html.j2', post=post)


@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        slug = new_post(title, content)
        return redirect(url_for('post.detail', slug=slug))
    return render_template('form.html.j2')



def init_app(app: Flask):
    app.register_blueprint(bp)
