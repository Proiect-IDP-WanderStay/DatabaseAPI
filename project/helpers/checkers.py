from ..models import Hotel, Contact, Reservation
from datetime import datetime, timezone

def check_if_free(start_date, end_date, room_id):
    resv = Reservation.query.filter(Reservation.start_date <= end_date, 
        Reservation.end_date >= start_date, 
        Reservation.room_id == room_id).first()
    
    return resv is None