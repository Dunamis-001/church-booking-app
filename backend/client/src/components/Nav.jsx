import React from 'react';
import { useAuth } from '../context/AuthContext';

const Nav = ({ setPage }) => {
  const { user, isAuthenticated, logout } = useAuth();

  return (
    <nav className="bg-white shadow sticky top-0 z-50 w-full">
      <div className="max-w-7xl mx-auto px-4 md:px-8 h-16 flex items-center justify-between">
        <button onClick={() => setPage('home')} className="text-2xl font-bold text-indigo-600">
          Church Booking
        </button>
        <div className="flex gap-4 items-center">
          <button onClick={() => setPage('home')} className="text-gray-600 hover:text-indigo-600">
            Home
          </button>
          <button onClick={() => setPage('rooms')} className="text-gray-600 hover:text-indigo-600">
            Rooms
          </button>
          {isAuthenticated && (
            <button onClick={() => setPage('bookings')} className="text-gray-600 hover:text-indigo-600">
              My Bookings
            </button>
          )}
          <button onClick={() => setPage('contact')} className="text-gray-600 hover:text-indigo-600">
            Contact
          </button>
          {isAuthenticated ? (
            <div className="flex items-center gap-4">
              <span className="text-gray-600">Welcome, {user?.username}</span>
              <button
                onClick={logout}
                className="px-4 py-2 text-white bg-red-600 rounded hover:bg-red-700 transition"
              >
                Logout
              </button>
            </div>
          ) : (
            <div className="flex gap-2">
              <button
                onClick={() => setPage('login')}
                className="px-4 py-2 text-indigo-600 border border-indigo-600 rounded hover:bg-indigo-50 transition"
              >
                Login
              </button>
              <button
                onClick={() => setPage('register')}
                className="px-4 py-2 text-white bg-indigo-600 rounded hover:bg-indigo-700 transition"
              >
                Register
              </button>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Nav;