from flask import Blueprint, Flask, jsonify, request, Response
from .models import Room, Hotel, Contact
from .helpers.oder import Order
from .helpers.filter import Filter, filter_generic

bp_hotel = Blueprint("hotels", __name__)


@bp_hotel.route("/")
def home():
    return "Hello, Hotels!"

@bp_hotel.route("/WanderRooms/getRooms", method=['POST'])
def getRooms():
    payload = request.get_json(silent=True)

    filter = Filter()
    if (payload and 'filter' in payload):
        filter.read_filter(payload['filter'])
    
    order = Order()
    if (payload and 'order' in payload):
        order.read_order(payload['order'])

    rooms = Room.query.all()
    
    rooms_filtered = list(filter(lambda r : filter_generic(filter, r), rooms))
        

    return jsonify(rooms_filtered)
