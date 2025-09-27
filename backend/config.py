import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///church_booking.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or 'your-secret-key-change-this'
    CORS_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]