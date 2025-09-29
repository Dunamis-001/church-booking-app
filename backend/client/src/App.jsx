import React, { useState } from 'react';
import { AuthProvider } from './context/AuthContext';
import Nav from './components/Nav';
import Footer from './components/Footer';
import Home from './components/Home';
import Rooms from './components/Rooms';
import Bookings from './components/Bookings';
import Contact from './components/Contact';
import Login from './components/Login';
import Register from './components/Register';
import BookingForm from './components/BookingForm';

function App() {
  const [page, setPage] = useState('home');
  const [selectedRoom, setSelectedRoom] = useState(null);

  const renderPage = () => {
    switch (page) {
      case 'home':
        return <Home setPage={setPage} />;
      case 'rooms':
        return <Rooms setPage={setPage} setSelectedRoom={setSelectedRoom} />;
      case 'bookings':
        return <Bookings />;
      case 'contact':
        return <Contact />;
      case 'bookingForm':
        return <BookingForm selectedRoom={selectedRoom} setPage={setPage} />;
      case 'login':
        return <Login setPage={setPage} />;
      case 'register':
        return <Register setPage={setPage} />;
      default:
        return <Home setPage={setPage} />;
    }
  };

  return (
    <AuthProvider>
      <div className="min-h-screen flex flex-col">
        <Nav setPage={setPage} />
        <main className="flex-1">{renderPage()}</main>
        <Footer />
      </div>
    </AuthProvider>
  );
}

export default App;