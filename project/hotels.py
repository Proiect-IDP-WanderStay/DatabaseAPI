from flask import Blueprint, jsonify, Response, abort, request
from .models import Room, Reservation
from .helpers.oder import Order
from .helpers.filter import Filter, filter_generic
from .helpers.checkers import check_if_free
from functools import wraps
import requests
from . import db
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, Gauge, Summary, Histogram, Info, start_http_server

room_reservations_counter = Counter('room_reservations_counter', 
                'This is a counter for room reservations')
room_reservations_cancels = Counter('room_reservations_cancels', 
                'This is a counter for room cancels')
i = Info('IO_API', 'This is IO API Info')
i.info({'version': '1.0.1', 'buildhost': 'wanderstay'})


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


@bp_hotel.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


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
def reserve():
    payload = request.get_json(silent=True)

    if (not payload):
        return {
            "message": "No given info for the reservation ",
            "data": None,
            "error": "Bad request"
        }, 400
    
    user_id = payload["user_id"]
    if (not 'user_id' in payload):
        return {
            "message": "IO_API: Please provide user_id",
            "error": "Bad request"
        }, 400
    

    if not ('start_date' in payload and 'end_date' in payload):
        return {
            "message": "Please provide start_date and end_date ",
            "error": "Bad request"
        }, 400
    
    if not ('room_id' in payload):
        return {
            "message": "Please provide room_id ",
            "error": "Bad request"
        }, 400

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

    db.session.add(reservation)
    db.session.commit()

    room_reservations_counter.inc()
    return {
            "message": "The room was reserved ",
        }, 200


@bp_hotel.route("/WanderRooms/cancelRoom", methods=['POST'])
def cancel():
    payload = request.get_json(silent=True)
    if (not payload) or (not 'reservation_id' in payload):
        return {
            "message": "The reservation was not specified ",
            "error": "Bad request"
        }, 400
    
    user_id = payload["user_id"]
    if (not 'user_id' in payload):
        return {
            "message": "IO_API: Please provide user_id",
            "error": "Bad request"
        }, 400

    reservation = Reservation.query.filter_by(id=payload['reservation_id'], user_id=user_id).first()
    if (not reservation):
        return {
            "message": "The reservation does not exist ",
            "error": "Bad request",
        }, 400
    
    db.session.delete(reservation)
    db.session.commit()

    room_reservations_cancels.inc()
    return {
            "message": "The reservation was canceled ",
        }, 200

@bp_hotel.route("/WanderRooms/updateReservation", methods=['PUT'])
def update():
    payload = request.get_json(silent=True)

    if (not payload) or (not 'reservation_id' in payload):
        return {
            "message": "The reservation was not specified ",
            "error": "Bad request"
        }, 400
    
    user_id = payload["user_id"]
    if (not 'user_id' in payload):
        return {
            "message": "IO_API: Please provide user_id",
            "error": "Bad request"
        }, 400

    reservation = Reservation.query.filter_by(id=payload['reservation_id'], user_id=user_id).first()
    if (not reservation):
        return {
            "message": "The reservation does not exist ",
            "error": "Bad request",
        }, 400
    message = ''
    if 'end_date' in payload:
        reservation.end_date = payload['end_date']
        message = 'End date updated\n'

    if 'start_date' in payload:
        reservation.start_date = payload['start_date']
        message = message + 'Start date updated\n'

    db.session.commit()
    print(message)
    return {
            "message": message,
        }, 200

@bp_hotel.route("/WanderRooms/getHistory", methods=['POST'])
def history():
    payload = request.get_json(silent=True)

    if (not payload):
        return {
            "message": "IO_API: No payload given ",
            "error": "Bad request"
        }, 400

    user_id = payload["user_id"]
    if (not 'user_id' in payload):
        return {
            "message": "IO_API: Please provide user_id",
            "error": "Bad request"
        }, 400

    reservations = Reservation.query.filter_by(user_id=user_id).all()

    if not reservations:
        return {
            "message": "No reservations found for this user",
            "error": "Not Found"
        }, 404
    
    return {
            "data": reservations,
        }, 200
    
