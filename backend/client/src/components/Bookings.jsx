import React, { useEffect, useState } from 'react';
import { useAuth } from '../context/AuthContext';
import api from '../services/api';

const Bookings = () => {
  const [bookings, setBookings] = useState([]);
  const [rooms, setRooms] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { isAuthenticated } = useAuth();

  useEffect(() => {
    const fetchData = async () => {
      if (!isAuthenticated) {
        setLoading(false);
        return;
      }

      try {
        const [bookingsData, roomsData] = await Promise.all([
          api.getBookings(),
          api.getRooms()
        ]);
        setBookings(bookingsData);
        setRooms(roomsData);
      } catch (err) {
        setError('Failed to fetch data. Please try again.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [isAuthenticated]);

  const handleDeleteBooking = async (bookingId) => {
    if (!window.confirm('Are you sure you want to delete this booking?')) {
      return;
    }

    try {
      await api.deleteBooking(bookingId);
      setBookings(bookings.filter(b => b.id !== bookingId));
    } catch (err) {
      setError(err.message);
    }
  };

  const getRoomName = (roomId) => rooms.find((r) => r.id === roomId)?.name ?? `Room ${roomId}`;

  if (!isAuthenticated) {
    return (
      <section className="min-h-[calc(100vh-8rem)] flex items-center justify-center px-4">
        <div className="max-w-2xl w-full bg-white rounded-xl shadow-lg p-8 text-center">
          <h2 className="text-4xl font-bold text-gray-800 mb-4">Login Required</h2>
          <p className="text-lg text-gray-600 mb-6">You need to be logged in to view your bookings.</p>
        </div>
      </section>
    );
  }

  return (
    <section className="min-h-[calc(100vh-8rem)] w-full bg-gray-100 px-4 py-10">
      <h2 className="text-4xl font-bold text-gray-800 mb-8 text-center">Your Bookings</h2>
      {loading ? (
        <div className="h-48 flex items-center justify-center">
          <p className="text-xl text-gray-500">Loading bookings...</p>
        </div>
      ) : error ? (
        <div className="text-center text-red-500 text-xl">{error}</div>
      ) : bookings.length === 0 ? (
        <div className="text-center text-gray-500 text-xl">You have no bookings yet.</div>
      ) : (
        <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {bookings.map((b) => (
            <div key={b.id} className="bg-white rounded-lg shadow-xl p-6 hover:scale-[1.02] transition">
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Booking for {getRoomName(b.room_id)}</h3>
              <p className="text-gray-600">Purpose: {b.purpose}</p>
              <p className="text-gray-600">Status: {b.status}</p>
              <p className="text-gray-600">Start: {new Date(b.start_time).toLocaleString()}</p>
              <p className="text-gray-600">End: {new Date(b.end_time).toLocaleString()}</p>
            </div>
          ))}
        </div>
      )}
    </section>
  );
};

export default Bookings;