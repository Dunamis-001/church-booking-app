from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Room, Booking
from schemas import booking_schema, bookings_schema
from utils.helpers import parse_iso

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/bookings', methods=['GET'])
@jwt_required()
def get_bookings():
    current_user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=current_user_id).all()
    return jsonify(bookings_schema.dump(bookings)), 200

@bookings_bp.route('/bookings', methods=['POST'])
@jwt_required()
def create_booking():
    current_user_id = get_jwt_identity()
    data = request.get_json() or {}
    
    required_fields = ['room_id', 'start_time', 'end_time', 'purpose']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required fields', 'required': required_fields}), 400
    
    try:
        room_id = int(data['room_id'])
        start_time = parse_iso(data['start_time'])
        end_time = parse_iso(data['end_time'])
        purpose = data['purpose']
    except Exception as e:
        return jsonify({'message': 'Invalid payload', 'error': str(e)}), 400

    if end_time <= start_time:
        return jsonify({'message': 'End time must be after start time'}), 400

    room = Room.query.get(room_id)
    if not room:
        return jsonify({'message': 'Room not found'}), 404

    conflict = Booking.query.filter(
        Booking.room_id == room_id,
        ~((Booking.end_time <= start_time) | (Booking.start_time >= end_time))
    ).first()
    if conflict:
        return jsonify({'message': 'Time slot already booked for this room'}), 409

    new_booking = Booking(
        user_id=current_user_id,
        room_id=room_id,
        start_time=start_time,
        end_time=end_time,
        purpose=purpose,
        status=data.get('status', 'pending')
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify(booking_schema.dump(new_booking)), 201

@bookings_bp.route('/bookings/<int:id>', methods=['GET'])
@jwt_required()
def get_booking(id):
    current_user_id = get_jwt_identity()
    booking = Booking.query.get_or_404(id)
    
    if booking.user_id != current_user_id:
        return jsonify({'message': 'Unauthorized'}), 403
    
    return jsonify(booking_schema.dump(booking)), 200

@bookings_bp.route('/bookings/<int:id>', methods=['PATCH'])
@jwt_required()
def update_booking(id):
    current_user_id = get_jwt_identity()
    booking = Booking.query.get_or_404(id)
    
    if booking.user_id != current_user_id:
        return jsonify({'message': 'Unauthorized'}), 403
    
    data = request.get_json() or {}
    
    try:
        if 'room_id' in data:
            room_id = int(data['room_id'])
            room = Room.query.get(room_id)
            if not room:
                return jsonify({'message': 'Room not found'}), 404
            booking.room_id = room_id
        
        if 'start_time' in data:
            booking.start_time = parse_iso(data['start_time'])
        
        if 'end_time' in data:
            booking.end_time = parse_iso(data['end_time'])
        
        if 'purpose' in data:
            booking.purpose = data['purpose']
        
        if 'status' in data:
            booking.status = data['status']
        
        if booking.end_time <= booking.start_time:
            return jsonify({'message': 'End time must be after start time'}), 400
        
        conflict = Booking.query.filter(
            Booking.room_id == booking.room_id,
            Booking.id != id,
            ~((Booking.end_time <= booking.start_time) | (Booking.start_time >= booking.end_time))
        ).first()
        if conflict:
            return jsonify({'message': 'Time slot already booked for this room'}), 409
        
        db.session.commit()
        return jsonify(booking_schema.dump(booking)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Invalid payload', 'error': str(e)}), 400

@bookings_bp.route('/bookings/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_booking(id):
    current_user_id = get_jwt_identity()
    booking = Booking.query.get_or_404(id)
    
    if booking.user_id != current_user_id:
        return jsonify({'message': 'Unauthorized'}), 403
    
    db.session.delete(booking)
    db.session.commit()
    return jsonify({'message': 'Booking deleted successfully'}), 200
