from ..models import Room, Hotel, Contact



MAX_PRICE = 100000

class Filter:
    def __init__(self) -> None:
        self.city = ''
        self.country = ''
        self.price_min = 0
        self.price_max = MAX_PRICE
        self.size = -1
        self.hotel_id = -1

    def read_filter(self, json):
        if not json:
            return self
        
        if ('city' in json) and (len(json['city']) != 0):
            self.city = json['city']
        if ('country' in json) and (len(json['country']) != 0):
            self.country = json['country']
        if ('price_min' in json) and (json['price_min'] >= 0):
            self.price_min = json['price_min']
        if ('price_max' in json) and (json['price_max'] >= 0):
            self.price_max = json['price_max']
        if ('size' in json) and (json['size'] >= 0):
            self.size = json['size']
        if ('hotel_id' in json) and (json['hotel_id'] >= 0):
            self.hotel_id = json['hotel_id']



def filter_generic(filter, room):
    ok = True
    hotel = Hotel.query.filter_by(id=room.hotel_id).first()
    contact = Contact.query.filter_by(id=hotel.contact_id).first()

    if not filter:
        return ok

    city = contact.city
    if (filter.city != '') and (city != filter.city):
        ok = 0
        return ok
    
    country = contact.country
    if (filter.country != '') and (country != filter.country):
        ok = 0
        return ok
    
    
    if (filter.price_min > room.ptice) or (filter.price_max < room.price):
        ok = 0
        return ok

    if (filter.size != -1) and (filter.size != room.nr_people):
        ok = 0
        return ok
    
    if (filter.city != -1) and (filter.hotel_id != room.hotel_id):
        ok = 0
        return ok

    return ok