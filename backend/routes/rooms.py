from flask import Blueprint, request, jsonify
from models import Room
from extensions import db

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/rooms', methods=['GET', 'POST'])
def handle_rooms():
    if request.method == 'GET':
        rooms = Room.query.all()
        return jsonify([r.to_dict() for r in rooms])
    
    data = request.get_json() or {}
    new_room = Room(
        name=data['name'],
        description=data.get('description'),
        capacity=data.get('capacity'),
        location=data.get('location'),
        image_url=data.get('image_url')
    )
    db.session.add(new_room)
    db.session.commit()
    return jsonify(new_room.to_dict()), 201