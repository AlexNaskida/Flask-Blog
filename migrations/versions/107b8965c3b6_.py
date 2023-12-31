"""empty message

Revision ID: 107b8965c3b6
Revises: 
Create Date: 2023-07-19 16:01:18.073951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107b8965c3b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poster_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(batch_op.f('uq_post_slug'), ['slug'])
        batch_op.create_foreign_key(batch_op.f('fk_post_poster_id_users'), 'users', ['poster_id'], ['id'])
        batch_op.drop_column('author')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_users_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_users_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_users_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_users_email'), type_='unique')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_post_poster_id_users'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('uq_post_slug'), type_='unique')
        batch_op.drop_column('poster_id')

    # ### end Alembic commands ###
