from flask_sqlalchemy import SQLAlchemy

# Inintialize SQLAlchemy
db = SQLAlchemy()

# Define classes for each of the tables
class Performance(db.Model):
    key = db.Column(db.String(30), primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    expire_at = db.Column(db.DateTime, nullable=True)
    title = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(200), nullable=True)
    ensemble_type = db.Column(db.String(10), nullable=True)
    perf_status = db.Column(db.String(1), nullable=True)
    child_count = db.Column(db.Integer, nullable=True)
    app_uid = db.Column(db.String(20), nullable=True)
    arr_key = db.Column(db.String(30), nullable=True)
    orig_track_city = db.Column(db.String(40), nullable=True)
    orig_track_country = db.Column(db.String(40), nullable=True)
    media_url = db.Column(db.String(200), nullable=True)
    video_media_url = db.Column(db.String(200), nullable=True)
    video_media_mp4_url = db.Column(db.String(200), nullable=True)
    web_url = db.Column(db.String(300), nullable=True)
    cover_url = db.Column(db.String(200), nullable=True)
    total_performers = db.Column(db.Integer, nullable=True)
    total_listens = db.Column(db.Integer, nullable=True)
    total_loves = db.Column(db.Integer, nullable=True)
    total_comments = db.Column(db.Integer, nullable=True)
    total_commenters = db.Column(db.Integer, nullable=True)
    performed_by = db.Column(db.String(50), nullable=True)
    performed_by_url = db.Column(db.String(50), nullable=True)
    owner_account_id = db.Column(db.BigInteger, db.ForeignKey('singer.account_id'), nullable=False)
    owner_handle = db.Column(db.String(50), nullable=True)
    owner_pic_url = db.Column(db.String(200), nullable=True)
    owner_lat = db.Column(db.Float, nullable=True)
    owner_lon = db.Column(db.Float, nullable=True)
    filename = db.Column(db.String(200), nullable=True)
    performers = db.Column(db.String(100), nullable=True)
    performer_ids = db.Column(db.String(200), nullable=True)
    performer_handles = db.Column(db.String(200), nullable=True)
    fixed_title = db.Column(db.String(100), nullable=True)
    short_ind = db.Column(db.String(1), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class Singer(db.Model):
    account_id = db.Column(db.BigInteger, primary_key=True)
    performed_by = db.Column(db.String(50), nullable=True)
    url = db.Column(db.String(50), nullable=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    pic_url = db.Column(db.String(200), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    lon = db.Column(db.Float, nullable=True)
    is_vip = db.Column(db.Boolean, nullable=True)
    is_verified = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class PerformanceSinger(db.Model):
    performance_key = db.Column(db.String(30), db.ForeignKey('performance.key'), primary_key=True)
    singer_account_id = db.Column(db.BigInteger, db.ForeignKey('singer.account_id'), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class PerformanceFavorite(db.Model):
    favorited_by_username = db.Column(db.String(50), primary_key=True)
    performance_key = db.Column(db.String(30), db.ForeignKey('performance.key'), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class TitleMapping(db.Model):
    smule_title = db.Column(db.String(100), primary_key=True)
    mapped_title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class ExcludeList(db.Model):
    list_type = db.Column(db.String(100), primary_key=True)
    item_name = db.Column(db.String(100), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
