"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref

# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table
class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    plus_one = db.Column(db.String(55), nullable=True)
    phone = db.Column(db.String(15), nullable=False)
    events_attending = db.relationship("Event", secondary="guest_event_link")

class Event(db.Model):
    """Class Event represents the event table in our SQL database."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90), nullable=False)
    description = db.Column(db.String(140), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    guests = db.relationship("Guest", secondary="guest_event_link")

# TODO: Create a table `guest_event_table` with the following columns:
# - book_id: Integer column (foreign key)
# - genre_id: Integer column (foreign key)

guest_event_table = db.Table('guest_event_table',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')))