import json
from flask import Blueprint, request, abort
from flask_restx import Namespace, Resource, Api, fields
from src.extensions.database import db
from src.modules.post.models import Post
from src.modules.auth.models import User
from flask_restx import reqparse

api_blueprint = Blueprint(
    "api", __name__, url_prefix="/api"
)

api = Api(api_blueprint)

post_model = api.model("Posts", {
    "id": fields.Integer(),
    "slug": fields.String(),
    "poster_id": fields.Integer(),
    "title": fields.String(),
    "content": fields.String()
})

parser = reqparse.RequestParser()
parser.add_argument('slug', type=str, required=True, help="Slug cannot be blank!")
parser.add_argument('poster_id', type=int, required=True, help="Username cannot be blank!")
parser.add_argument('title', type=str, required=True, help="Title cannot be blank!")
parser.add_argument('content', type=str, required=True, help="Content cannot be blank!")


@api.route('/posts')
class Posts(Resource):
    @api.marshal_list_with(post_model)
    def get(self):
        return Post.query.all()

    @api.expect(parser)
    @api.marshal_with(post_model)
    def post(self):

        args = parser.parse_args()

        slug = Post.query.filter_by(slug=args['slug']).first()
        user = User.query.filter_by(id=args['poster_id']).first()

        if slug:
            abort(409)

        if not user:
            abort(404)

        post = Post().create(
            slug=args['slug'],
            title=args['title'],
            content=args['content'],
            poster_id=args['poster_id']
        )
        return post, 201



@api.route('/posts/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
class PostModification(Resource):

    @api.marshal_with(post_model)
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post

    @api.expect(parser)
    @api.marshal_with(post_model)
    def put(self, post_id):

        args = parser.parse_args()

        update_post = Post.query.get_or_404(post_id)
        if update_post:
            update_post.slug = args['slug']
            update_post.title = args['title']
            update_post.content = args['content']
            update_post.poster_id = args['poster_id']
    
            db.session.commit()

            return update_post

        else:
            abort(404, "Couldn't find post")


    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)

        if post:
            db.session.delete(post)
            db.session.commit()
            return {'message': 'Post deleted successfully'}
        else:
            abort(404)

