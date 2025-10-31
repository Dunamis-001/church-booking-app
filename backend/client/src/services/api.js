const API_BASE_URL = 'http://localhost:5000';

class ApiService {
  constructor() {
    this.token = localStorage.getItem('token');
  }

  setToken(token) {
    this.token = token;
    if (token) {
      localStorage.setItem('token', token);
    } else {
      localStorage.removeItem('token');
    }
  }

  async request(endpoint, options = {}) {
    const url = `${endpoint}`;
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    };

    if (this.token) {
      headers['Authorization'] = `Bearer ${this.token}`;
    }

    const response = await fetch(url, {
      ...options,
      headers,
    });

    if (!response.ok) {
      if (response.status === 401) {
        this.setToken(null);
        throw new Error('Please log in again');
      }
      const error = await response.json();
      throw new Error(error.message || 'Request failed');
    }

    return response.json();
  }

  // Auth methods (unchanged)
  async login(username, password) {
    return this.request('/login', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
    });
  }

  async register(username, email, password) {
    return this.request('/register', {
      method: 'POST',
      body: JSON.stringify({ username, email, password }),
    });
  }

  async getProfile() {
    return this.request('/profile');
  }

  // Rooms methods (updated for new structure)
  async getRooms() {
    return this.request('/rooms');
  }

  async getRoom(id) {
    return this.request(`/rooms/${id}`);
  }

  async createRoom(roomData) {
    return this.request('/rooms', {
      method: 'POST',
      body: JSON.stringify(roomData),
    });
  }

  async updateRoom(id, roomData) {
    return this.request(`/rooms/${id}`, {
      method: 'PATCH',
      body: JSON.stringify(roomData),
    });
  }

  async deleteRoom(id) {
    return this.request(`/rooms/${id}`, {
      method: 'DELETE',
    });
  }

  // Bookings methods (updated for new structure)
  async getBookings() {
    return this.request('/bookings');
  }

  async getBooking(id) {
    return this.request(`/bookings/${id}`);
  }

  async createBooking(bookingData) {
    return this.request('/bookings', {
      method: 'POST',
      body: JSON.stringify(bookingData),
    });
  }

  async updateBooking(id, bookingData) {
    return this.request(`/bookings/${id}`, {
      method: 'PATCH',
      body: JSON.stringify(bookingData),
    });
  }

  async deleteBooking(id) {
    return this.request(`/bookings/${id}`, {
      method: 'DELETE',
    });
  }
}

export default new ApiService();