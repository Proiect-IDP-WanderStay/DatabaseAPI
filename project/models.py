from dataclasses import dataclass
from datetime import datetime, timezone

from . import db

@dataclass
class Contact(db.Model):
   __tablename__ = "Contact"

   id: int
   phone: str
   country: str
   city: str
   street: str
   email: str

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   phone = db.Column(db.String(128), nullable=False)
   country = db.Column(db.String(128), nullable=False)
   city = db.Column(db.String(128), nullable=False)
   street = db.Column(db.String(128), nullable=False)
   email = db.Column(db.String(128), nullable=False)
   
   def __init__(self, id, phone, country, city, street, email):
      self.id = id
      self.phone = phone
      self.country = country
      self.city = city
      self.street = street
      self.email = email



@dataclass
class Hotel(db.Model):
   __tablename__ = "Hotels"

   id: int
   name: str
   contact_id: int
   rating_id: int


   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.String(128), nullable=False)
   contact_id = db.Column(db.Integer, db.ForeignKey("Contact.id"), unique=False)
   rating_id = db.Column(db.Integer, db.ForeignKey("Contact.id"), unique=False)

   
   def __init__(self, id, name, contact_id, rating_id):
      self.id = id
      self.name = name
      self.contact_id = contact_id
      self.rating_id = rating_id


@dataclass
class Room(db.Model):
   __tablename__ = "Rooms"

   id: int
   hotel_id: int
   price: float
   nr_people: int

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   hotel_id = db.Column(db.Integer, db.ForeignKey("Hotels.id"), nullable=False)
   price = db.Column(db.Float(precision=5), nullable=False)
   nr_people = db.Column(db.Integer, nullable=False)
   
   def __init__(self, id, phone, country, city, street, email):
      self.id = id
      self.phone = phone
      self.country = country
      self.city = city
      self.street = street
      self.email = email


@dataclass
class User(db.Model):
   __tablename__ = "Users"

   id: int
   name: int
   password: str
   created_date: datetime
   mail: str

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.String(128), nullable=False)
   password = db.Column(db.String(128), nullable=False)
   created_date = db.Column(db.DateTime, nullable=False, unique=False, default=datetime.utcnow())
   mail = db.Column(db.String(128), nullable=False)

   def __init__(self, id, name, password, created_date, mail):
      self.id = id
      self.name = name
      self.password = password
      self.created_date = created_date
      self.mail = mail


@dataclass
class Rating(db.Model):
   __tablename__ = "Ratings"

   id: int
   comment: str
   user_id: int
   stars: float

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   comment = db.Column(db.String(128), nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey("Orase.id"))
   stars = db.Column(db.Float(precision=5), default=0)

   def __init__(self, id, comment, user_id, stars):
      self.id = id
      self.comment = comment
      self.user_id = user_id
      self.stars = stars


@dataclass
class Reservation(db.Model):
   __tablename__ = "Reservations"

   id: int
   user_id: int
   start_date: datetime
   end_date: datetime

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   user_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
   start_date = db.Column(db.DateTime, default=0)
   end_date = db.Column(db.DateTime, nullable=False, unique=False)

   def __init__(self, id, user_id, start_date, end_date):
      self.id = id
      self.user_id = user_id
      self.start_date = start_date
      self.end_date = end_date
