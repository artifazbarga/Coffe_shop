"""empty message

Revision ID: 186e6ea1c660
Revises: c40f1d8faa7d
Create Date: 2020-11-03 11:53:12.417254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '186e6ea1c660'
down_revision = 'c40f1d8faa7d'
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
    sa.Column('phone', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Addcart')
    # ### end Alembic commands ###