from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)

bookings = []
booking_id_counter = 1

@app.route('/')
def home():
    return jsonify({
        'service': 'Bookin Service',
        'version': '1.0.0',
        'status': 'running'
    })

@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    hotels = [
        {'id': 1, 'name': 'Grand Hotel', 'city': 'Москва', 'rating': 4.8},
        {'id': 2, 'name': 'Seaside Resort', 'city': 'Сочи', 'rating': 4.5}
    ]
    return jsonify({'hotels': hotels})

@app.route('/api/hotels/<int:hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    hotels = {
        1: {'id': 1, 'name': 'Grand Hotel', 'city': 'Москва', 'address': 'ул. Тверская, 1'},
        2: {'id': 2, 'name': 'Seaside Resort', 'city': 'Сочи', 'address': 'ул. Морская, 5'}
    }
    if hotel_id not in hotels:
        abort(404, 'Hotel not found')
    return jsonify(hotels[hotel_id])

@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    rooms = [
        {'id': 1, 'hotel_id': 1, 'number': '101', 'type': 'suite', 'price': 15000},
        {'id': 2, 'hotel_id': 1, 'number': '102', 'type': 'double', 'price': 8000},
        {'id': 3, 'hotel_id': 2, 'number': '201', 'type': 'single', 'price': 5000}
    ]
    return jsonify({'rooms': rooms})

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    global booking_id_counter
    data = request.get_json()
    if not data:
        abort(400, 'No data provided')
    booking = {
        'id': booking_id_counter,
        'room_id': data.get('room_id'),
        'user_id': data.get('user_id'),
        'check_in': data.get('check_in'),
        'check_out': data.get('check_out'),
        'status': 'confirmed',
        'created_at': datetime.now().isoformat()
    }
    bookings.append(booking)
    booking_id_counter += 1
    return jsonify({
        'id': booking['id'],
        'status': booking['status'],
        'message': 'Бронирование подтверждено'
    }), 201

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    return jsonify({'bookings': bookings})

@app.route('/api/bookings/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    for booking in bookings:
        if booking['id'] == booking_id:
            booking['status'] = 'cancelled'
            return jsonify({
                'message': 'Бронирование отменено',
                'id': booking_id,
                'status': 'cancelled'
            }), 200
    abort(404, 'Booking not found')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
