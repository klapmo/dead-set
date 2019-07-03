class Artist(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True) # Creates a unique key in table to identify each User
    name = db.Column(db.String(120), index=True, unique=True) # Creates email for each, unique=True makes sure they dont give duplicates
    sort_name = db.Column(db.String(128), unique=True)
    mbid = db.Column(db.Integer, unique=True)
    # posts = db.relationship('Post', backref='author', lazy='dynamic') # TODO Create relationship for Posts

    # def __repr__(self):
    #     return '<USER {}>'.format(self.email)


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String(140))
    state = db.Column(db.String(140))
    country = db.Column(db.String(140))
    state_code = db.Column(db.String(3))
    country_code = db.Column(db.String(3))
    # timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    # user_ID = db.Column(db.Integer,db.ForeignKey('user.id'))

    # def __repr__(self):
    #     return '<POST {}>'.format(self.body)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140))
    artist_ID = db.Column(db.String(140),db.ForeignKey('artist.id'))
    count = db.Column(db.Integer)

class Set(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140))
    song_ID = db.Column(db.String(140),db.ForeignKey('song.id'))
    encore = db.Column(db.Integer)
    song_loc = db.Column(db.Integer)
    set_loc = db.Column(db.Integer)

class Setlist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    set_ID = db.Column(db.String(140),db.ForeignKey('set.id'))
    event_ID = db.Column(db.Integer)
    set_loc = db.Column(db.Integer, db.ForeignKey('set.set_loc'))

class Concert(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    artist_ID = db.Column(db.String(140),db.ForeignKey('artist.id'))
    venue_ID = db.Column(db.String(140),db.ForeignKey('venue.id'))
    last_updated = db.Column(db.DateTime)
    event_date = db.Column(db.DateTime)
    tour = db.Column(db.String(140))
    event_id = db.Column(db.Integer)

