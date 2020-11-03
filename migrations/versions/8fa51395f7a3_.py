"""empty message

Revision ID: 8fa51395f7a3
Revises: ff932ffeabce
Create Date: 2020-11-03 10:27:18.024044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fa51395f7a3'
down_revision = 'ff932ffeabce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Addcart',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('create_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('update_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.Column('des', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('kind', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Addcart')
    # ### end Alembic commands ###
