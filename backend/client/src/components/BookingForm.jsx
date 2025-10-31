import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import api from '../services/api';

const BookingForm = ({ selectedRoom, setPage }) => {
  const [purpose, setPurpose] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [bookingError, setBookingError] = useState(null);
  const { isAuthenticated } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setBookingError(null);

    if (!purpose || !startDate || !endDate) {
      setBookingError('All fields are required.');
      setIsSubmitting(false);
      return;
    }

    try {
      const bookingData = {
        room_id: selectedRoom.id,
        purpose,
        status: 'pending',
        start_time: new Date(startDate).toISOString(),
        end_time: new Date(endDate).toISOString(),
      };

      await api.createBooking(bookingData);
      setPage('bookings');
    } catch (err) {
      setBookingError(err.message); 
      console.error('Booking error:', err);
    } finally {
      setIsSubmitting(false);
    }
  };

  if (!isAuthenticated) {
    return (
      <section className="min-h-[calc(100vh-8rem)] flex items-center justify-center px-4">
        <div className="max-w-2xl w-full bg-white rounded-xl shadow-lg p-8 text-center">
          <h2 className="text-4xl font-bold text-gray-800 mb-4">Login Required</h2>
          <p className="text-lg text-gray-600 mb-6">You need to be logged in to book a room.</p>
          <button
            onClick={() => setPage('login')}
            className="px-8 py-3 text-lg font-semibold text-white bg-indigo-600 rounded-full shadow hover:bg-indigo-700 transition"
          >
            Login
          </button>
        </div>
      </section>
    );
  }

  if (!selectedRoom) {
    return (
      <section className="min-h-[calc(100vh-8rem)] flex items-center justify-center px-4">
        <div className="max-w-2xl w-full bg-white rounded-xl shadow-lg p-8 text-center">
          <h2 className="text-4xl font-bold text-gray-800 mb-4">Room Not Found</h2>
          <p className="text-lg text-gray-600 mb-6">Please go back to the rooms page and select a room to book.</p>
          <button
            onClick={() => setPage('rooms')}
            className="px-8 py-3 text-lg font-semibold text-white bg-indigo-600 rounded-full shadow hover:bg-indigo-700 transition"
          >
            Back to Rooms
          </button>
        </div>
      </section>
    );
  }

  return (
    <section className="min-h-[calc(100vh-8rem)] w-full bg-gray-100 px-4 py-10 flex justify-center">
      <div className="w-full max-w-3xl bg-white rounded-lg shadow-xl p-8">
        <h2 className="text-4xl font-bold text-gray-800 mb-8 text-center">Book {selectedRoom.name}</h2>
        {bookingError && <p className="text-red-500 text-center mb-4">{bookingError}</p>}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="purpose" className="block font-semibold text-gray-900 mb-2">
              Purpose
            </label>
            <input
              id="purpose"
              type="text"
              value={purpose}
              onChange={(e) => setPurpose(e.target.value)}
              placeholder="e.g., Sunday Service, Youth Group Meeting"
              className="w-full p-3 border border-gray-300 rounded-md"
            />
          </div>
          <div>
            <label htmlFor="startDate" className="block font-semibold text-gray-900 mb-2">
              Start Date/Time
            </label>
            <input
              id="startDate"
              type="datetime-local"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-md"
            />
          </div>
          <div>
            <label htmlFor="endDate" className="block font-semibold text-gray-900 mb-2">
              End Date/Time
            </label>
            <input
              id="endDate"
              type="datetime-local"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-md"
            />
          </div>
          <button
            type="submit"
            disabled={isSubmitting}
            className="w-full py-3 bg-indigo-600 text-white font-semibold rounded-md hover:bg-indigo-700 transition"
          >
            {isSubmitting ? 'Booking...' : 'Confirm Booking'}
          </button>
        </form>
      </div>
    </section>
  );
};

export default BookingForm;