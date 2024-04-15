from flask import Blueprint, jsonify, request, Response
from .models import Room
from .helpers.oder import Order
from .helpers.filter import Filter, filter_generic

bp_hotel = Blueprint("hotels", __name__)




@bp_hotel.route("/")
def home():
    return "Hello, Hotels!"

@bp_hotel.route("/WanderRooms/getRooms", methods=['POST'])
def getRooms():
    payload = request.get_json(silent=True)

    filter_obj = Filter()
    if (payload and 'filter' in payload):
        filter_obj.read_filter(payload['filter'])
    print(filter_obj)
    order_obj = Order()
    if (payload and 'order' in payload):
        order_obj.read_order(payload['order'])

    rooms = Room.query.all()

    rooms_filtered = list(filter(lambda r : filter_generic(filter_obj, r), rooms))
    

    return jsonify(rooms_filtered)
