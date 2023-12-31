"""empty message

Revision ID: 2a9a799c0916
Revises: 6e15432efa2c
Create Date: 2023-07-20 14:41:42.837956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a9a799c0916'
down_revision = '6e15432efa2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_like')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_like',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('post_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='fk_post_like_post_id_post'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_post_like_user_id_users'),
    sa.PrimaryKeyConstraint('id', name='pk_post_like')
    )
    # ### end Alembic commands ###
