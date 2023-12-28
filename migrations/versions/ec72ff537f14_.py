"""empty message

Revision ID: ec72ff537f14
Revises: 6760eedb73e1
Create Date: 2023-12-24 19:00:29.091596

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ec72ff537f14'
down_revision = '6760eedb73e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('performance_bkp20231217')
    with op.batch_alter_table('title_metadata', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating_nbr', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('singer_type', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('title_metadata', schema=None) as batch_op:
        batch_op.drop_column('singer_type')
        batch_op.drop_column('rating_nbr')

    op.create_table('performance_bkp20231217',
    sa.Column('key', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('ensemble_type', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('child_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('app_uid', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('arr_key', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('orig_track_city', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('orig_track_country', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('media_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('video_media_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('video_media_mp4_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('web_url', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('total_performers', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total_listens', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total_loves', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total_comments', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total_commenters', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('performed_by', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('performed_by_url', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('owner_account_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('owner_lat', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('owner_lon', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('filename', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('owner_handle', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('owner_pic_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('artist', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('cover_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('expire_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('fixed_title', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('perf_status', sa.VARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('performers', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('short_ind', sa.VARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('performer_handles', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('performer_ids', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('parent_key', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('display_pic_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
