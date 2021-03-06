"""empty message

Revision ID: f6696b85066a
Revises: be972bc9bd18
Create Date: 2020-11-01 22:15:07.797934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6696b85066a'
down_revision = 'be972bc9bd18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('special',
    sa.Column('id', sa.INTEGER(), nullable=False),
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
    op.drop_table('special')
    # ### end Alembic commands ###
