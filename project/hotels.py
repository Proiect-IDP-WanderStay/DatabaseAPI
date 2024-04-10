from flask import Blueprint

bp_hotel = Blueprint("hotels", __name__)

@bp_hotel.route("/")
def home():
    return "Hello, Hotels!"

@bp_hotel.route("/about")
def about():
    return "Hello, About!"