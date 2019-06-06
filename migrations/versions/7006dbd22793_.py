"""empty message

Revision ID: 7006dbd22793
Revises: a6916bbb6160
Create Date: 2019-06-06 01:55:53.137642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7006dbd22793'
down_revision = 'a6916bbb6160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('performance', sa.Column('owner_pic_url', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('performance', 'owner_pic_url')
    # ### end Alembic commands ###
