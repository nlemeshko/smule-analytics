"""empty message

Revision ID: cc35f8a2e6ca
Revises: 38bd6b6bd67c
Create Date: 2021-11-20 12:04:56.654046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc35f8a2e6ca'
down_revision = '38bd6b6bd67c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('performance_favorite', sa.Column('rating_nbr', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('performance_favorite', 'rating_nbr')
    # ### end Alembic commands ###
