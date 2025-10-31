from extensions import ma
from models import User, Room, Booking
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash',)

class RoomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Room
        load_instance = True

class BookingSchema(ma.SQLAlchemyAutoSchema):
    start_time = fields.DateTime()
    end_time = fields.DateTime()
    
    class Meta:
        model = Booking
        load_instance = True
        include_fk = True

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True)
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)
