"""empty message

Revision ID: bf1e3a48ea16
Revises: 
Create Date: 2020-11-01 11:39:20.899581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf1e3a48ea16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hotcoffee')
    op.drop_table('fruitjuice')
    op.drop_table('customers')
    op.drop_table('persons')
    op.drop_table('icedcoffee')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('icedcoffee',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name_ice', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('special', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('imge', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='icedcoffee_pkey')
    )
    op.create_table('persons',
    sa.Column('personid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lastname', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=255), autoincrement=False, nullable=True)
    )
    op.create_table('customers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nameuser', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('facebook', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('phonenumber', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('instegram', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='customers_pkey')
    )
    op.create_table('fruitjuice',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name_f', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('special', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('imge', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='fruitjuice_pkey')
    )
    op.create_table('hotcoffee',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name_hot', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('special', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('imge', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='hotcoffee_pkey')
    )
    # ### end Alembic commands ###