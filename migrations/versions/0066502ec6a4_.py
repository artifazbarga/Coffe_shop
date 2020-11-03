"""empty message

Revision ID: 0066502ec6a4
Revises: 7c6991e9902a
Create Date: 2020-11-03 12:24:25.219661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0066502ec6a4'
down_revision = '7c6991e9902a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Addcart',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.Column('des', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('kind', sa.INTEGER(), nullable=False),
    sa.Column('phone', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Addcart')
    # ### end Alembic commands ###
