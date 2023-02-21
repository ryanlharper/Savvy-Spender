"""empty message

Revision ID: e303f1b4130e
Revises: 847d069e5c8d
Create Date: 2023-02-12 15:47:27.179943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e303f1b4130e'
down_revision = '847d069e5c8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('budgetyears',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('year', sa.String(length=4), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('budgetyears')
    # ### end Alembic commands ###
