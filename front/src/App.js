// src/App.js
import React, { useState } from 'react';
import RestaurantForm from './components/RestaurantForm';
import ReviewList from './components/ReviewList';
import './App.css';

const App = () => {
  const [selectedRestaurant, setSelectedRestaurant] = useState(null);
  const [averageRating, setAverageRating] = useState(null);

  const handleRestaurantSubmit = (restaurantId) => {
    setSelectedRestaurant(restaurantId);
  };

  const handleAverageRating = (rating) => {
    setAverageRating(rating);
  };

  return (
    <div className="app-container">
      <h1 className="logo">Find your Best restaurant!</h1>
      <RestaurantForm onRestaurantSubmit={handleRestaurantSubmit} />
      {averageRating && (
        <div className="average-rating">
          Average Rating: {Array.from({ length: 5 }, (_, index) => (
            <span key={index} className={`star ${index < averageRating ? 'filled' : ''}`}>&#9733;</span>
          ))}
        </div>
      )}
      {selectedRestaurant && (
        <ReviewList restaurantId={selectedRestaurant} onAverageRating={handleAverageRating} />
      )}
    </div>
  );
};

export default App;
