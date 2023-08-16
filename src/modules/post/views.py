from src.modules.auth.models import User
from src.modules.post.models import Post, db
from src.modules.post.forms import PostForm
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user


post_blueprint = Blueprint(
    "post", __name__, template_folder="templates", url_prefix="/blog"
)


@post_blueprint.route('/')
def blog():
    posts = Post.query.order_by(Post.date_posted)
    return render_template("blog.html", posts=posts)


@post_blueprint.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        poster = current_user.id
        print(poster)
        filter_post = Post.query.filter_by(slug=form.slug.data).first()

        if filter_post is None:
            new_post = Post().create(
                slug=form.slug.data,
                poster_id=poster,
                title=form.title.data,
                content=form.content.data
            )

            db.session.add(new_post)
            db.session.commit()
            flash("Post submitted")
            return redirect(url_for('post.blog'))
        else:
            flash("Post already exists")
    return render_template("add_post.html", form=form)


@post_blueprint.route('/post/<string:slug>')
def show_post(slug):
    post = Post.query.filter_by(slug=slug).first()
    if post:
        return render_template("show_post.html", post=post, slug=slug)
    else:
        return render_template("blog.html")


@post_blueprint.route('/post/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    form = PostForm()
    update_post = Post.query.get_or_404(id)

    id = current_user.id
    if id == update_post.poster.id:
        if request.method == "POST":
            update_post.slug = request.form['slug']
            update_post.title = request.form['title']
            update_post.content = request.form['content']
            try:
                db.session.commit()
                flash("Post updated")
                return redirect(url_for("post.blog"))
            except:
                flash("Error while updating")
    else:
        flash("Access Denied")
        return redirect(url_for("post.blog"))

    return render_template("edit_post.html", form=form, update_post=update_post, id=id)


@post_blueprint.route("/posts/delete/<int:id>")
@login_required
def delete_post(id):
    delete_post = Post.query.get_or_404(id)

    id = current_user.id
    if id == delete_post.poster.id:
        try:
            db.session.delete(delete_post)
            db.session.commit()
            flash("Post deleted")
            return redirect(url_for('post.blog'))
        except:
            flash("Error occurred")
        return render_template("post.html", form=form)
    else:
        flash("Access denied for deleting post")
        return redirect(url_for('post.blog'))


@post_blueprint.route("/<action>/<int:id>")
@login_required
def like_action(action, id):
    post = Post.query.filter_by(id=id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(request.referrer)