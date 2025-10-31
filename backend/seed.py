from app import app
from models import User, Room, Booking
from datetime import datetime, timedelta
from extensions import db
import random


def seed_database():
  
    
    with app.app_context():
        # Clear existing data
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create sample users
        print("Creating users...")
        users_data = [
            {'username': 'admin', 'email': 'admin@church.com', 'password': 'admin123'},
            {'username': 'pastor_john', 'email': 'john@church.com', 'password': 'pastor123'},
            {'username': 'mary_smith', 'email': 'mary@church.com', 'password': 'mary123'},
            {'username': 'david_wilson', 'email': 'david@church.com', 'password': 'david123'},
            {'username': 'sarah_jones', 'email': 'sarah@church.com', 'password': 'sarah123'},
        ]
        
        users = []
        for user_data in users_data:
            user = User(
                username=user_data['username'],
                email=user_data['email']
            )
            user.set_password(user_data['password'])
            users.append(user)
            db.session.add(user)
        
        db.session.commit()
        print(f"Created {len(users)} users")
        
        # Create sample rooms with diverse, working image URLs
        print("Creating rooms...")
        rooms_data = [
            {
                'name': 'Main Sanctuary',
                'description': 'Large worship hall with seating for 300 people, perfect for Sunday services and special events.',
                'capacity': 300,
                'location': 'Ground Floor',
                'image_url': 'https://images.unsplash.com/photo-1519494026892-80ce3a83b695?w=800&q=80'
            },
            {
                'name': 'Fellowship Hall',
                'description': 'Multi-purpose room ideal for community gatherings, potlucks, and small events.',
                'capacity': 150,
                'location': 'Ground Floor',
                'image_url': 'https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=800&q=80'
            },
            {
                'name': 'Youth Room',
                'description': 'Modern space designed for youth activities, games, and meetings.',
                'capacity': 50,
                'location': 'Second Floor',
                'image_url': 'https://images.unsplash.com/photo-1531482615713-2afd69097998?w=800&q=80'
            },
            {
                'name': 'Conference Room',
                'description': 'Professional meeting space with presentation equipment and comfortable seating.',
                'capacity': 20,
                'location': 'Second Floor',
                'image_url': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80'
            },
            {
                'name': 'Children\'s Chapel',
                'description': 'Bright and colorful space designed specifically for children\'s services and activities.',
                'capacity': 75,
                'location': 'Ground Floor',
                'image_url': 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=800&q=80'
            },
            {
                'name': 'Prayer Room',
                'description': 'Quiet, peaceful space for individual prayer, meditation, and small group worship.',
                'capacity': 15,
                'location': 'Second Floor',
                'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&q=80'
            },
            {
                'name': 'Kitchen',
                'description': 'Fully equipped kitchen for preparing meals for church events and community outreach.',
                'capacity': 10,
                'location': 'Ground Floor',
                'image_url': 'https://images.unsplash.com/photo-1556910096-6f5e72db6803?w=800&q=80'
            },
            {
                'name': 'Library',
                'description': 'Quiet study space with religious books, resources, and comfortable reading areas.',
                'capacity': 25,
                'location': 'Second Floor',
                'image_url': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800&q=80'
            }
        ]
        
        rooms = []
        for room_data in rooms_data:
            room = Room(**room_data)
            rooms.append(room)
            db.session.add(room)
        
        db.session.commit()
        print(f"Created {len(rooms)} rooms")
        
        # Create sample bookings
        print("Creating bookings...")
        purposes = [
            'Sunday Service',
            'Youth Group Meeting',
            'Bible Study',
            'Prayer Meeting',
            'Community Outreach',
            'Wedding Ceremony',
            'Funeral Service',
            'Church Council Meeting',
            'Children\'s Sunday School',
            'Choir Practice',
            'Men\'s Fellowship',
            'Women\'s Circle',
            'New Member Orientation',
            'Church Picnic Planning',
            'Volunteer Training'
        ]
        
        statuses = ['pending', 'confirmed', 'cancelled']
        
        # Generate bookings for the next 30 days
        bookings = []
        for i in range(50):  # Create 50 sample bookings
            # Random user (excluding admin for some bookings)
            user = random.choice(users[1:] if random.random() > 0.3 else users)
            
            # Random room
            room = random.choice(rooms)
            
            # Random date within next 30 days
            start_date = datetime.now() + timedelta(days=random.randint(0, 30))
            
            # Random time (between 8 AM and 8 PM)
            start_hour = random.randint(8, 20)
            start_minute = random.choice([0, 30])
            start_time = start_date.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
            
            # Duration between 1-4 hours
            duration_hours = random.choice([1, 1.5, 2, 2.5, 3, 3.5, 4])
            end_time = start_time + timedelta(hours=duration_hours)
            
            # Random purpose and status
            purpose = random.choice(purposes)
            status = random.choice(statuses)
            
            # Check for conflicts (simple check)
            conflict = Booking.query.filter(
                Booking.room_id == room.id,
                ~((Booking.end_time <= start_time) | (Booking.start_time >= end_time))
            ).first()
            
            if not conflict:
                booking = Booking(
                    user_id=user.id,
                    room_id=room.id,
                    start_time=start_time,
                    end_time=end_time,
                    purpose=purpose,
                    status=status
                )
                bookings.append(booking)
                db.session.add(booking)
        
        db.session.commit()
        print(f"Created {len(bookings)} bookings")
        
        # Print summary
        print("\n" + "="*50)
        print("SEEDING COMPLETE!")
        print("="*50)
        print(f"Users created: {len(users)}")
        print(f"Rooms created: {len(rooms)}")
        print(f"Bookings created: {len(bookings)}")
        print("\nTest accounts:")
        for user in users:
            user_data_dict = {u['username']: u['password'] for u in users_data}
            print(f"  Username: {user.username} | Password: {user_data_dict.get(user.username, 'N/A')}")
        print("\nYou can now test the application with these accounts!")

if __name__ == '__main__':
    seed_database()