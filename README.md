# Church Booking App

A web application designed to manage and display a collection of church rooms and user bookings. Users can browse rooms, create bookings, and (with authentication enabled) view their personal bookings.

## Table of Contents
Features

Technologies Used

Project Structure

Deployment Links

Setup Instructions

Prerequisites

Backend Setup (Flask)

Frontend Setup (React Vite)

How to Run

Usage

Support and Contact details

License

## Features

Browse Rooms: View a list of available rooms with capacity, location, and image.

Create Bookings: Submit new bookings by selecting a room and time window.

User Bookings: View your bookings (requires JWT authentication).

Booking Conflict Detection: Prevent overlapping bookings for the same room.

Responsive Design: Optimized for mobile, tablet, and desktop use.

## Technologies Used

### Frontend
React (with Vite)

Tailwind CSS (utility-first styling)

Context API (for auth state, optional)

### Backend

Flask (Python)

Flask SQLAlchemy, Flask-Migrate

Flask-Bcrypt, Flask-JWT-Extended (authentication)

Flask-CORS

## Project Structure

church-booking/
└── backend/
    ├── app.py                # Flask app factory + blueprint registration
    ├── config.py             # Configuration (environment-driven)
    ├── models/
    │   ├── __init__.py
    │   ├── user.py           # User model with password hashing
    │   ├── room.py           # Room model
    │   └── booking.py        # Booking model
    ├── routes/
    │   ├── __init__.py
    │   ├── auth.py           # /register, /login, /profile routes
    │   ├── rooms.py          # /rooms route
    │   └── bookings.py       # /bookings route with conflict detection
    ├── utils/
    │   ├── __init__.py
    │   └── helpers.py        # ISO date parsing helper functions
    ├── migrations/           # Flask-Migrate artifacts
    ├── seed.py               # Script to seed users, rooms, bookings data
    ├── requirements.txt      # Backend dependencies
    ├── .env                  # Local environment variables
    └── client/               # React frontend app inside backend
        ├── index.html
        ├── vite.config.js
        ├── tailwind.config.js
        └── src/
            ├── App.jsx        # Main app + routing/view switching
            ├── main.jsx       # React entry point
            ├── index.css      # Tailwind + base layout styles
            ├── components/
            │   ├── Nav.jsx
            │   ├── Footer.jsx
            │   ├── Home.jsx
            │   ├── Rooms.jsx
            │   ├── Bookings.jsx
            │   ├── Contact.jsx
            │   ├── Login.jsx
            │   ├── Register.jsx
            │   └── BookingForm.jsx
            ├── context/
            │   └── AuthContext.jsx
            ├── hooks/
            │   └── useAuth.js
            └── services/
                └── api.js
## Links
Deployed link: https://church-booking-app.onrender.com/
Git Hub repository: https://github.com/Dunamis-001/church-booking-app.git



## Setup Instructions

Prerequisites
Python 3.9+ (with pip)

Node.js (LTS recommended) and npm

#### Backend Setup (Flask)

Navigate to the backend and create a virtual environment:

### Windows:

cd backend
python -m venv venv
venv\Scripts\activate
macOS/Linux:


cd backend
python -m venv venv
source venv/bin/activate
Install dependencies:


pip install -r requirements.txt
Setup environment variables in backend/.env:


DATABASE_URI=sqlite:///church_booking.db
JWT_SECRET_KEY=change-me-in-production
FLASK_ENV=development
Initialize the database (first time only):


flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed sample data (optional):


python seed.py

#### Frontend Setup (React Vite)

Navigate to the client inside backend:


cd backend/client
Install dependencies:


npm install
Tailwind configuration:
Ensure tailwind.config.js includes:


content: ["./index.html","./src/**/*.{js,jsx,ts,tsx}"]
Check index.css contains Tailwind directives and full-height styles:


@tailwind base;
@tailwind components;
@tailwind utilities;

html, body, #root { height: 100%; margin: 0; padding: 0; }

# How to Run

Start the Backend API:
From the backend directory:
Activate virtual environment first (see above)
python app.py
API will run at http://localhost:5000

Start the Frontend:

From backend/client directory:
npm run dev
Vite will run the frontend at http://localhost:5173

(Optional) To avoid CORS issues during development, configure a proxy in vite.config.js linking /api calls to http://localhost:5000.

### Usage

Home: Overview and entry points to rooms and bookings.

Rooms: Browse all rooms with details like name, description, capacity, location, and image.

Book a Room: Select a room, choose start/end times, provide a booking purpose, and submit.

My Bookings: View your bookings (JWT login required if auth enabled).

Authentication: Register a new user and log in to get tokens for protected endpoints.

### Support and Contact details

Email: alex232nyamai@gmail.com

Email: cheronlilian21@gmail.com

License
MIT License © 2025 Lilian Cherono, Alex Nyamai

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


This README comprehensively covers the key aspects of your Church Booking App project as per your provided format.
