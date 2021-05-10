from app import db
from datetime import datetime

class Genre(db.Model):
  __tablename__ = 'genres'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)

artist_genre_table = db.Table('artist_genre_table',
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True)
)

venue_genre_table = ('venue_genre_table',
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id,'), primary_key=True),
    db.Column('venue_id', db.Integer, db.ForeignKey('venues.id'), primary_key=True)
)

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    website = db.Column(db.String(250))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(250))
 
    shows = db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self):
      return f"<Venue {self.id} name: {self.name}>"

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
      return f"<Artist {self.id} name: {self.name}>"

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
  __tablename__ = 'shows'

  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return f"<Show {self.id}, Artist {self.artist_id} Venue {self.venue_id}>"