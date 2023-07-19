from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"

    def __repr__(self):
        p = self
        return f"<Playlist id={p.id}, name={p.name}, description={p.description}"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Song(db.Model):
    """Song."""
    __tablename__ = "songs"

    def __repr__(self):
        s = self
        return f"<Song id={s.id}, title{s.title}, artist={s.artist}"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.Text, nullable=False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlists_songs"

    def __repr__(self):
        a = self
        return f"<PlaylistSong id={a.id}, playlist_id={a.playlist_id}, song_id={a.song_id}"
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.ForeignKey('id.playlists')
    song_id = db.ForeignKey('id.songs')


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)