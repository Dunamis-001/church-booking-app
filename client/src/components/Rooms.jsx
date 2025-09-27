import React, { useEffect, useState } from 'react';
import api from '../services/api';

const Rooms = ({ setPage, setSelectedRoom }) => {
  const [rooms, setRooms] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRooms = async () => {
      try {
        const data = await api.getRooms();
        setRooms(data);
      } catch (err) {
        setError('Failed to fetch rooms. Ensure the Flask server is running.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchRooms();
  }, []);

  return (
    <section className="min-h-[calc(100vh-8rem)] w-full bg-gray-100 px-4 py-10">
      <h2 className="text-4xl font-bold text-gray-800 mb-8 text-center">Available Rooms</h2>
      {loading ? (
        <div className="h-48 flex items-center justify-center">
          <p className="text-xl text-gray-500">Loading rooms...</p>
        </div>
      ) : error ? (
        <div className="text-center text-red-500 text-xl">{error}</div>
      ) : (
        <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {rooms.map((room) => (
            <div key={room.id} className="bg-white rounded-lg shadow-xl overflow-hidden hover:scale-[1.02] transition">
              {room.image_url && (
                <img src={room.image_url} alt={room.name} className="w-full h-48 object-cover" />
              )}
              <div className="p-6">
                <h3 className="text-2xl font-semibold text-gray-900 mb-2">{room.name}</h3>
                <p className="text-gray-600 mb-4">{room.description}</p>
                <div className="flex items-center justify-between text-gray-500">
                  <span>Capacity: {room.capacity}</span>
                  <span>Location: {room.location}</span>
                </div>
                <button
                  onClick={() => { setSelectedRoom(room); setPage('bookingForm'); }}
                  className="mt-4 w-full py-2 bg-indigo-600 text-white font-semibold rounded hover:bg-indigo-700 transition"
                >
                  Book this Room
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </section>
  );
};

export default Rooms;