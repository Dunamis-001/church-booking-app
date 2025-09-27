import React from 'react';

const Contact = () => (
  <section className="min-h-[calc(100vh-8rem)] flex items-center justify-center px-4">
    <div className="max-w-2xl w-full bg-white rounded-xl shadow-lg p-8">
      <h2 className="text-4xl font-bold text-gray-800 mb-4">Contact Us</h2>
      <div className="space-y-3 text-lg">
        <p><span className="font-semibold text-gray-700">Email:</span> contact@church.com</p>
        <p><span className="font-semibold text-gray-700">Phone:</span> (555) 123-4567</p>
        <p><span className="font-semibold text-gray-700">Address:</span> 123 Church Street, City, State 12345</p>
      </div>
    </div>
  </section>
);

export default Contact;