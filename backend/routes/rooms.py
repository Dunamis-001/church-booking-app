from flask import Blueprint, request, jsonify
from models import Room
from extensions import db
from schemas import room_schema, rooms_schema
from flask_jwt_extended import jwt_required

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    return jsonify(rooms_schema.dump(rooms)), 200

@rooms_bp.route('/rooms', methods=['POST'])
@jwt_required()
def create_room():
    data = request.get_json() or {}
    
    errors = room_schema.validate(data)
    if errors:
        return jsonify({'message': 'Validation error', 'errors': errors}), 400
    
    new_room = room_schema.load(data)
    db.session.add(new_room)
    db.session.commit()
    return jsonify(room_schema.dump(new_room)), 201

@rooms_bp.route('/rooms/<int:id>', methods=['GET'])
def get_room(id):
    room = Room.query.get_or_404(id)
    return jsonify(room_schema.dump(room)), 200

@rooms_bp.route('/rooms/<int:id>', methods=['PATCH'])
@jwt_required()
def update_room(id):
    room = Room.query.get_or_404(id)
    data = request.get_json() or {}
    
    errors = room_schema.validate(data, partial=True)
    if errors:
        return jsonify({'message': 'Validation error', 'errors': errors}), 400
    
    if 'name' in data:
        room.name = data['name']
    if 'description' in data:
        room.description = data.get('description')
    if 'capacity' in data:
        room.capacity = data.get('capacity')
    if 'location' in data:
        room.location = data.get('location')
    if 'image_url' in data:
        room.image_url = data.get('image_url')
    
    db.session.commit()
    return jsonify(room_schema.dump(room)), 200

@rooms_bp.route('/rooms/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_room(id):
    room = Room.query.get_or_404(id)
    db.session.delete(room)
    db.session.commit()
    return jsonify({'message': 'Room deleted successfully'}), 200
