from flask import Blueprint, jsonify, Response, abort, request
from .models import Room, Reservation
from .helpers.oder import Order
from .helpers.filter import Filter, filter_generic
from .helpers.checkers import check_if_free
from functools import wraps
import requests
from . import db

bp_hotel = Blueprint("hotels", __name__)

# e fix ala pus in docker-compose
USER_API_URL = "http://user:5000/users/checkUser"
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        
        myobj = {"dummy": "dummy_v"}
        check_response = requests.post(url=USER_API_URL, 
                                    headers={"Authorization": token}, 
                                    json=myobj)
        
        if check_response.status_code != 200:
            return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401 
        j = check_response.json()
        user_id = j['user_id']
        return f(user_id ,*args, **kwargs)

    return decorated


@bp_hotel.route("/")
def home():
    return "Hello, Hotels!"

@bp_hotel.route("/WanderRooms/getRooms", methods=['POST'])
def getRooms():
    payload = request.get_json(silent=True)

    filter_obj = Filter()
    if (payload and 'filter' in payload):
        filter_obj.read_filter(payload['filter'])

    order_obj = Order()
    if (payload and 'order' in payload):
        order_obj.read_order(payload['order'])

    rooms = Room.query.all()

    rooms_filtered = list(filter(lambda r : filter_generic(filter_obj, r), rooms))
    

    return jsonify(rooms_filtered)


@bp_hotel.route("/WanderRooms/reserveRoom", methods=['POST'])
@token_required
def reserve(user_id):
    payload = request.get_json(silent=True)

    if (not payload):
        return {
            "message": "No given info for the reservation ",
            "data": None,
            "error": "Bad request"
        }, 400
    
    if not ('start_date' in payload and 'end_date' in payload):
        return {
            "message": "Please provide start_date and end_date ",
            "data": None,
            "error": "Bad request"
        }, 401
    
    if not ('room_id' in payload):
        return {
            "message": "Please provide room_id ",
            "data": None,
            "error": "Bad request"
        }, 402

    if not check_if_free(payload['start_date'], payload['end_date'], payload['room_id']):
        return {
            "message": "Room is busy on the given date ",
            "data": None,
            "error": "Bad request"
        }, 403

    reservation = Reservation(user_id = user_id,
                            start_date = payload['start_date'],
                            end_date = payload['end_date'],
                            room_id = payload['room_id'])
    print(reservation.id)
    db.session.add(reservation)
    db.session.commit()

    return {
            "message": "The room was reserved ",
            "data": None,
        }, 200
