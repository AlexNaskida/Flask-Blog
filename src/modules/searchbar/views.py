from flask import Blueprint
from src.modules.post.models import Post



searchbar_blueprint = Blueprint(
    "search", __name__, template_folder="templates", url_prefix="/blog"
)
# Pass form page to navbar for search
@searchbar_blueprint.context_processor
def base():
    form = SearchForm()
    posts = Post.query
    return dict(form=form, posts=posts)


@searchbar_blueprint.route("/search", methods=["POST"])
def search():
    form = SearchForm()
    posts = Posts.query

    if form.validate_on_submit():
        post.searched = form.searched.data
        posts = posts.filter(Posts.content.like('%' + post.searched + '%'))\
            .order_by(Posts.title).all()

        return render_template("search.html", form=form, searched=post.searched, posts=posts)