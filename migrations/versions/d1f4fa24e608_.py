"""empty message

Revision ID: d1f4fa24e608
Revises: c05ddfa71c73
Create Date: 2023-07-20 12:25:38.719056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f4fa24e608'
down_revision = 'c05ddfa71c73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint('fk_post_like_users', type_='foreignkey')
        batch_op.drop_column('like')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('like', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_post_like_users', 'users', ['like'], ['id'])

    # ### end Alembic commands ###
