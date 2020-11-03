"""empty message

Revision ID: 7c6991e9902a
Revises: 186e6ea1c660
Create Date: 2020-11-03 12:18:21.349459

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7c6991e9902a'
down_revision = '186e6ea1c660'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Addcart', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('Addcart', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_column('Addcart', 'update_at')
    op.drop_column('Addcart', 'create_at')
    op.add_column('products', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('products', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_column('products', 'update_at')
    op.drop_column('products', 'create_at')
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_column('users', 'update_at')
    op.drop_column('users', 'create_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('update_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.add_column('products', sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('products', sa.Column('update_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('products', 'updated_at')
    op.drop_column('products', 'created_at')
    op.add_column('Addcart', sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('Addcart', sa.Column('update_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('Addcart', 'updated_at')
    op.drop_column('Addcart', 'created_at')
    # ### end Alembic commands ###
