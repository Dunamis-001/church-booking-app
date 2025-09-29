import React from 'react';

const Home = ({ setPage }) => (
  <section className="min-h-[calc(100vh-8rem)] flex items-center justify-center px-4">
    <div className="max-w-4xl w-full text-center bg-white rounded-xl shadow-lg p-8">
      <h1 className="text-5xl md:text-6xl font-extrabold text-indigo-700 mb-4">Welcome to Church Booking</h1>
      <p className="text-xl text-gray-600 mb-8">
        Easily book and manage church facilities for your events and gatherings.
      </p>
      <button
        onClick={() => setPage('rooms')}
        className="px-8 py-3 text-lg font-semibold text-white bg-indigo-600 rounded-full shadow hover:bg-indigo-700 transition"
      >
        Explore Rooms
      </button>
    </div>
  </section>
);

export default Home;