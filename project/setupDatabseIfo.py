from project import db 
from .models import Contact, Hotel, Room, Reservation, User


CONTACTS = [
    {
        'id': '1',
        'phone': '0765409888',
        'country': 'Romania',
        'city': 'Craiova',
        'street': 'A.I. Cuza',
        'email': 'georgianaA_fr@yahoo.fr'
    },
    {
        'id': '2',
        'phone': '0734567890',
        'country': 'USA',
        'city': 'New York',
        'street': 'Broadway St.',
        'email': 'john_doe@example.com'
    },
    {
        'id': '3',
        'phone': '0212345678',
        'country': 'France',
        'city': 'Paris',
        'street': 'Rue de la Paix',
        'email': 'marie.dupont@example.fr'
    },
    {
        'id': '4',
        'phone': '0441234567',
        'country': 'UK',
        'city': 'London',
        'street': 'Baker Street',
        'email': 'sherlock221b@example.co.uk'
    },
    {
        'id': '5',
        'phone': '0498765432',
        'country': 'Germany',
        'city': 'Berlin',
        'street': 'Unter den Linden',
        'email': 'hans.mueller@example.de'
    },
    {
        'id': '6',
        'phone': '0312345678',
        'country': 'Italy',
        'city': 'Rome',
        'street': 'Via del Corso',
        'email': 'giuseppe.rossi@example.it'
    },
    {
        'id': '7',
        'phone': '0812345678',
        'country': 'Japan',
        'city': 'Tokyo',
        'street': 'Shibuya',
        'email': 'yamada.taro@example.jp'
    },
    {
        'id': '8',
        'phone': '0612345678',
        'country': 'Australia',
        'city': 'Sydney',
        'street': 'George St.',
        'email': 'emma.smith@example.com.au'
    },
    {
        'id': '9',
        'phone': '0551234567',
        'country': 'Canada',
        'city': 'Toronto',
        'street': 'Bay St.',
        'email': 'william.jones@example.ca'
    },
    {
        'id': '10',
        'phone': '0101234567',
        'country': 'China',
        'city': 'Beijing',
        'street': 'Wangfujing St.',
        'email': 'liu.ying@example.cn'
    }
]


HOTELS = [
    {
        'id': '1',
        'name': 'Grand Hotel',
        'contact_id': '1',
        'rating': '9.5'
    },
    {
        'id': '2',
        'name': 'Luxury Resort',
        'contact_id': '2',
        'rating': '8.9'
    },
    {
        'id': '3',
        'name': 'Seaside Inn',
        'contact_id': '3',
        'rating': '8.3'
    },
    {
        'id': '4',
        'name': 'Mountain Lodge',
        'contact_id': '4',
        'rating': '9.1'
    },
    {
        'id': '5',
        'name': 'City Center Hotel',
        'contact_id': '5',
        'rating': '7.5'
    },
    {
        'id': '6',
        'name': 'Rural Retreat',
        'contact_id': '1',
        'rating': '8.7'
    },
    {
        'id': '7',
        'name': 'Beachfront Bungalow',
        'contact_id': '7',
        'rating': '9.2'
    },
    {
        'id': '8',
        'name': 'Skyview Tower',
        'contact_id': '5',
        'rating': '9.8'
    },
    {
        'id': '9',
        'name': 'Lakeview Resort',
        'contact_id': '9',
        'rating': '8.6'
    },
    {
        'id': '10',
        'name': 'Urban Oasis',
        'contact_id': '1',
        'rating': '8.4'
    }
]

ROOMS = [
    {
        'id': '1',
        'hotel_id': '1',
        'price': '150',
        'nr_people': '2'
    },
    {
        'id': '2',
        'hotel_id': '2',
        'price': '250',
        'nr_people': '4'
    },
    {
        'id': '3',
        'hotel_id': '1',
        'price': '120',
        'nr_people': '2'
    },
    {
        'id': '4',
        'hotel_id': '4',
        'price': '200',
        'nr_people': '3'
    },
    {
        'id': '5',
        'hotel_id': '2',
        'price': '100',
        'nr_people': '1'
    },
    {
        'id': '6',
        'hotel_id': '6',
        'price': '180',
        'nr_people': '2'
    },
    {
        'id': '7',
        'hotel_id': '7',
        'price': '300',
        'nr_people': '2'
    },
    {
        'id': '8',
        'hotel_id': '4',
        'price': '400',
        'nr_people': '3'
    },
    {
        'id': '9',
        'hotel_id': '9',
        'price': '220',
        'nr_people': '2'
    },
    {
        'id': '10',
        'hotel_id': '5',
        'price': '150',
        'nr_people': '2'
    }
]

RESERVATIONS = [
    {
        'id': '1',
        'user_id': '1',
        'start_date': '2024-05-15',
        'end_date': '2024-05-20',
        'room_id': '1'
    },
    {
        'id': '2',
        'user_id': '2',
        'start_date': '2024-06-10',
        'end_date': '2024-06-15',
        'room_id': '1'
    },
    {
        'id': '3',
        'user_id': '2',
        'start_date': '2024-07-01',
        'end_date': '2024-07-07',
        'room_id': '1'
    },
    {
        'id': '4',
        'user_id': '1',
        'start_date': '2024-08-20',
        'end_date': '2024-08-25',
        'room_id': '2'
    },
    {
        'id': '5',
        'user_id': '5',
        'start_date': '2024-09-05',
        'end_date': '2024-09-10',
        'room_id': '5'
    },
    {
        'id': '6',
        'user_id': '6',
        'start_date': '2024-10-15',
        'end_date': '2024-10-20',
        'room_id': '6'
    },
    {
        'id': '7',
        'user_id': '7',
        'start_date': '2024-11-10',
        'end_date': '2024-11-15',
        'room_id': '7'
    },
    {
        'id': '8',
        'user_id': '6',
        'start_date': '2024-12-01',
        'end_date': '2024-12-07',
        'room_id': '8'
    },
    {
        'id': '9',
        'user_id': '9',
        'start_date': '2025-01-20',
        'end_date': '2025-01-25',
        'room_id': '9'
    },
    {
        'id': '10',
        'user_id': '5',
        'start_date': '2025-02-05',
        'end_date': '2025-02-10',
        'room_id': '10'
    }
]

USERS = [
    {
        'id': '1',
        'name': 'Alice',
        'password': 'alice123',
        'created_date': '2023-01-10',
        'mail': 'alice@example.com'
    },
    {
        'id': '2',
        'name': 'Bob',
        'password': 'bob456',
        'created_date': '2023-02-15',
        'mail': 'bob@example.com'
    },
    {
        'id': '3',
        'name': 'Charlie',
        'password': 'charlie789',
        'created_date': '2023-03-20',
        'mail': 'charlie@example.com'
    },
    {
        'id': '4',
        'name': 'David',
        'password': 'david123',
        'created_date': '2023-04-25',
        'mail': 'david@example.com'
    },
    {
        'id': '5',
        'name': 'Emma',
        'password': 'emma456',
        'created_date': '2023-05-30',
        'mail': 'emma@example.com'
    },
    {
        'id': '6',
        'name': 'Frank',
        'password': 'frank789',
        'created_date': '2023-06-05',
        'mail': 'frank@example.com'
    },
    {
        'id': '7',
        'name': 'Grace',
        'password': 'grace123',
        'created_date': '2023-07-10',
        'mail': 'grace@example.com'
    },
    {
        'id': '8',
        'name': 'Hannah',
        'password': 'hannah456',
        'created_date': '2023-08-15',
        'mail': 'hannah@example.com'
    },
    {
        'id': '9',
        'name': 'Ian',
        'password': 'ian789',
        'created_date': '2023-09-20',
        'mail': 'ian@example.com'
    },
    {
        'id': '10',
        'name': 'Jessica',
        'password': 'jessica123',
        'created_date': '2023-10-25',
        'mail': 'jessica@example.com'
    }
]

def add_contacts():
    for c in CONTACTS:
        contact = Contact(id = c['id'],
                        phone = c['phone'], 
                        country = c['country'], 
                        city = c['city'], 
                        street = c['street'], 
                        email= c['email'])
        db.session.add(contact)
    return

def add_hotels():
    for h in HOTELS:
        hotel = Hotel(id = h['id'],
                    name = h['name'],
                    contact_id = h['contact_id'],
                    rating = h['rating'])
        db.session.add(hotel)
    return

def add_rooms():
    for r in ROOMS:
        room = Room(id = r['id'],
                    hotel_id = r['hotel_id'],
                    price = r['price'],
                    nr_people = r['nr_people'])
        db.session.add(room)
    return
    
def add_reservation():
    for res in RESERVATIONS:
        reservation = Reservation(
                                user_id = res['user_id'],
                                start_date = res['start_date'],
                                end_date = res['end_date'],
                                room_id = res['room_id'])
        db.session.add(reservation)
    return

def add_user():
    for u in USERS:
        user = User(id = u['id'],
                    name = u['name'],
                    password = u['password'],
                    created_date = u['created_date'],
                    mail = u['mail'])
        db.session.add(user)
    return 

def add_all():
    add_user()
    db.session.commit()

    add_contacts()
    db.session.commit()

    add_hotels()
    db.session.commit()

    add_rooms()
    db.session.commit()

    add_reservation()
    db.session.commit()


    
