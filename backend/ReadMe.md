# Church Booking App

A web application designed to manage and display a collection of church rooms and user bookings. Users can browse rooms, create bookings, and (with authentication enabled) view their personal bookings.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Deployment Links](#deployment-links)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Backend Setup (Flask)](#backend-setup-flask)
  - [Frontend Setup (React Vite)](#frontend-setup-react-vite)
- [How to Run](#how-to-run)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Support and Contact Details](#support-and-contact-details)
- [License](#license)

## Features

- **Browse Rooms**: View a list of available rooms with capacity, location, and image.
- **Create Bookings**: Submit new bookings by selecting a room and time window.
- **Update Bookings**: Modify existing bookings with PATCH requests.
- **Delete Bookings**: Remove bookings you have created.
- **User Authentication**: Register, login, and manage your profile with JWT tokens.
- **User Bookings**: View your bookings (requires JWT authentication).
- **Booking Conflict Detection**: Prevent overlapping bookings for the same room.
- **Form Validation**: All forms use Formik with Yup validation (email format, password strength, etc.).
- **Responsive Design**: Optimized for mobile, tablet, and desktop use.

## Technologies Used

### Frontend

- **React** (with Vite)
- **Formik** - Form management and validation
- **Yup** - Schema validation for forms
- **Tailwind CSS** - Utility-first styling
- **Context API** - For authentication state management

### Backend

- **Flask** - Python web framework
- **SQLAlchemy** - ORM for database operations
- **Flask-Marshmallow** - Serialization and validation
- **Marshmallow-SQLAlchemy** - Integration between Marshmallow and SQLAlchemy
- **Flask-Migrate** - Database migrations
- **Flask-Bcrypt** - Password hashing
- **Flask-JWT-Extended** - JWT authentication
- **Flask-CORS** - Cross-origin resource sharing
- **SQLite** - Database (can be configured for PostgreSQL)

## Project Structure

```
church-booking-app/
├── backend/
│   ├── app.py                 # Flask app factory + blueprint registration
│   ├── config.py              # Configuration (environment-driven)
│   ├── extensions.py          # Flask extensions (db, ma)
│   ├── schemas.py             # Marshmallow schemas for serialization
│   ├── models.py              # SQLAlchemy models (User, Room, Booking)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py            # /register, /login, /profile routes (GET, POST, PATCH)
│   │   ├── rooms.py           # /rooms routes (GET, POST, PATCH, DELETE)
│   │   └── bookings.py         # /bookings routes (GET, POST, PATCH, DELETE)
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py         # ISO date parsing helper functions
│   ├── migrations/            # Flask-Migrate artifacts
│   ├── seed.py                # Script to seed users, rooms, bookings data
│   ├── requirements.txt       # Backend dependencies
│   ├── .env                   # Local environment variables
│   └── client/                # React frontend app inside backend
│       ├── index.html
│       ├── vite.config.js
│       ├── package.json
│       └── src/
│           ├── App.jsx         # Main app + routing/view switching
│           ├── main.jsx        # React entry point
│           ├── index.css       # Tailwind + base layout styles
│           ├── components/
│           │   ├── Nav.jsx
│           │   ├── Footer.jsx
│           │   ├── Home.jsx
│           │   ├── Rooms.jsx
│           │   ├── Bookings.jsx
│           │   ├── Contact.jsx
│           │   ├── Login.jsx      # Formik form for login
│           │   ├── Register.jsx   # Formik form for registration
│           │   └── BookingForm.jsx # Formik form for booking creation
│           ├── context/
│           │   └── AuthContext.jsx
│           ├── hooks/
│           │   └── useAuth.js
│           └── services/
│               └── api.js
```

## Deployment Links

- **Deployed link**: https://church-booking-app.onrender.com/
- **GitHub repository**: https://github.com/Dunamis-001/church-booking-app.git

## Setup Instructions

### Prerequisites

- **Python 3.9+** (with pip)
- **Node.js** (LTS recommended) and npm
- **Git** (optional, for cloning)

### Backend Setup (Flask)

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment:**

   **Windows:**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - Flask and related packages
   - SQLAlchemy and Flask-SQLAlchemy
   - Flask-Marshmallow and Marshmallow-SQLAlchemy
   - Flask-Migrate
   - Flask-Bcrypt
   - Flask-JWT-Extended
   - Flask-CORS
   - And other dependencies

4. **Set up environment variables:**

   Create a `.env` file in the `backend` directory:
   ```env
   DATABASE_URI=sqlite:///church_booking.db
   JWT_SECRET_KEY=change-me-in-production
   FLASK_ENV=development
   CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
   ```

5. **Initialize the database (first time only):**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Seed sample data (optional):**
   ```bash
   python seed.py
   ```

### Frontend Setup (React Vite)

1. **Navigate to the client directory:**
   ```bash
   cd backend/client
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

   This will install:
   - React and React-DOM
   - Vite
   - Tailwind CSS
   - Formik (for form management)
   - Yup (for validation schemas)
   - And other dependencies

3. **Verify Tailwind configuration:**

   Ensure `tailwind.config.js` includes:
   ```js
   content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"]
   ```

4. **Verify CSS setup:**

   Check that `src/index.css` contains:
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;

   html, body, #root {
     height: 100%;
     margin: 0;
     padding: 0;
   }
   ```

## How to Run

### Start the Backend API

From the `backend` directory:

1. **Activate virtual environment** (if not already activated):
   ```bash
   # Windows
   .venv\\Scripts\\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

   The API will run at `http://localhost:5000`

### Start the Frontend

From the `backend/client` directory:

```bash
npm run dev
```

Vite will run the frontend at `http://localhost:5173`

**Note:** To avoid CORS issues during development, the backend is configured to accept requests from `http://localhost:5173`. If you need to change the frontend port, update `CORS_ORIGINS` in `backend/config.py`.

## API Endpoints

### Authentication

- `POST /register` - Register a new user
- `POST /login` - Login user and receive JWT token
- `GET /profile` - Get user profile (requires authentication)
- `PATCH /profile` - Update user profile (requires authentication)

### Rooms

- `GET /rooms` - List all rooms
- `POST /rooms` - Create a new room (requires authentication)
- `GET /rooms/<id>` - Get room details
- `PATCH /rooms/<id>` - Update room details (requires authentication)
- `DELETE /rooms/<id>` - Delete a room (requires authentication)

### Bookings

- `GET /bookings` - List user's bookings (requires authentication)
- `POST /bookings` - Create a new booking (requires authentication)
- `GET /bookings/<id>` - Get booking details (requires authentication)
- `PATCH /bookings/<id>` - Update booking (requires authentication)
- `DELETE /bookings/<id>` - Delete booking (requires authentication)

**Note:** All routes return JSON responses and use appropriate HTTP status codes (200, 201, 400, 401, 403, 404, 409).

## Usage

1. **Home**: Overview and entry points to rooms and bookings.

2. **Rooms**: Browse all rooms with details like name, description, capacity, location, and image.

3. **Book a Room**: 
   - Select a room
   - Choose start/end times
   - Provide a booking purpose
   - Submit (with Formik validation)

4. **My Bookings**: View your bookings (JWT login required).

5. **Authentication**: 
   - Register a new user (with email and password validation)
   - Log in to get tokens for protected endpoints
   - Update your profile

## Support and Contact Details

- **Email**: alex232nyamai@gmail.com
- **Email**: cheronlilian21@gmail.com

## License

MIT License © 2025 Lilian Cherono, Alex Nyamai

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.