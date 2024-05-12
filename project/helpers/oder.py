from typing import List
from ..models import Room, Hotel, Contact

class Order:
    def __init__(self) -> None:
        self.alphabetic = 1
        self.price = 1

    def read_order(self, json):
        if not json:
            return self
        
        if ('alphabetic' in json):
            self.alphabetic = json['alphabetic']
        if ('price' in json):
            self.price = json['price']

    def helper_order(self, room):
        hotel = Hotel.query.filter_by(id=room.hotel_id).first()
        return hotel.name

    def order_rooms(self, rooms: List[Room]) -> List[Room]:
        if self.alphabetic:
            rooms.sort(key=lambda room: self.helper_order(room))
        else:
            rooms.sort(key=lambda room: self.helper_order(room), reverse=True)

        if self.price:
            rooms.sort(key=lambda room: room.price)
        else:
            rooms.sort(key=lambda room: room.price, reverse=True)
        return rooms


