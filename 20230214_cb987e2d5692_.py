"""empty message

Revision ID: cb987e2d5692
Revises: 2bc868288757
Create Date: 2023-02-14 17:10:48.188546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb987e2d5692'
down_revision = '2bc868288757'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('name', sa.String(length=128), nullable=False))
    op.drop_column('categories', 'catname')
    op.add_column('subcategories', sa.Column('name', sa.String(length=128), nullable=False))
    op.drop_column('subcategories', 'subcatname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subcategories', sa.Column('subcatname', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_column('subcategories', 'name')
    op.add_column('categories', sa.Column('catname', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_column('categories', 'name')
    # ### end Alembic commands ###
