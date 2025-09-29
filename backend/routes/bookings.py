from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Room, Booking
from utils.helpers import parse_iso

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/bookings', methods=['GET', 'POST'])
@jwt_required()
def handle_bookings():
    current_user_id = get_jwt_identity()
    
    if request.method == 'GET':
        bookings = Booking.query.filter_by(user_id=current_user_id).all()
        return jsonify([b.to_dict() for b in bookings])

    data = request.get_json() or {}
    if not {'room_id', 'start_time', 'end_time', 'purpose'} <= set(data):
        return jsonify({'message': 'Invalid payload'}), 400

    try:
        room_id = int(data['room_id'])
        start_time = parse_iso(data['start_time'])
        end_time = parse_iso(data['end_time'])
        purpose = data['purpose']
    except Exception:
        return jsonify({'message': 'Invalid payload'}), 400

    if end_time <= start_time:
        return jsonify({'message': 'End time must be after start time'}), 400

    # Check if room exists
    room = Room.query.get(room_id)
    if not room:
        return jsonify({'message': 'Room not found'}), 404

    # Conflict detection
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
    return jsonify(new_booking.to_dict()), 201