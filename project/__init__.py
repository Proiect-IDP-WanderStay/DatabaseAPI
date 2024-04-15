from dataclasses import dataclass, field
from flask import Flask,  jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

from .hotels import bp_hotel

app = Flask(__name__)
app.config.from_object("project.config.Config")

# blueprints
app.register_blueprint(bp_hotel)


# database
db = SQLAlchemy(app)


from .models import Contact, Hotel, Room, User, Rating, Reservation
