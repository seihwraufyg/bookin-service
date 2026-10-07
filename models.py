# models.py - модели данных для Bookin Service

class Hotel:
    """Модель отеля"""
    def __init__(self, id, name, address, city, rating):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.rating = rating

class Room:
    """Модель номера"""
    def __init__(self, id, hotel_id, number, room_type, price, capacity):
        self.id = id
        self.hotel_id = hotel_id
        self.number = number
        self.room_type = room_type
        self.price = price
        self.capacity = capacity
        self.is_available = True

class Booking:
    """Модель бронирования"""
    def __init__(self, id, user_id, room_id, check_in, check_out):
        self.id = id
        self.user_id = user_id
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out
        self.status = 'confirmed'

class User:
    """Модель пользователя"""
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
