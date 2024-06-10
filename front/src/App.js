import React, { useState } from 'react';
import RestaurantForm from './components/RestaurantForm';
import ReviewList from './components/ReviewList';
import Modal from './components/Modal';
import Info from './info';
import './App.css';

const App = () => {
  const [selectedRestaurant, setSelectedRestaurant] = useState(null);
  const [averageRating, setAverageRating] = useState(null);
  const [prevAverageRating, setPrevAverageRating] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleRestaurantSubmit = (restaurantId) => {
    setSelectedRestaurant(restaurantId);
  };

  const handleAverageRating = (rating) => {
    setAverageRating(rating);
  };

  const handlePrevAverageRating = (rating) => {
    setPrevAverageRating(rating);
  };

  const toggleModal = () => {
    setIsModalOpen(!isModalOpen);
  };

  return (
    <div className="app-container">
      <h1 className="logo">Find your Best restaurant!</h1>
      <button className="info-button" onClick={toggleModal}>?</button>
      <RestaurantForm onRestaurantSubmit={handleRestaurantSubmit} />
      {prevAverageRating && (
        <div className="prev-average-rating">
          실제 평점: {prevAverageRating}
        </div>
      )}
      {averageRating && (
        <div className="average-rating">
          평균 평점: {averageRating.toFixed(1)}
          {Array.from({ length: 5 }, (_, index) => (
            <span key={index} className={`star ${index < averageRating ? 'filled' : ''}`}>&#9733;</span>
          ))}
        </div>
      )}
      {selectedRestaurant ? (
        <ReviewList
          restaurantId={selectedRestaurant}
          onAverageRating={handleAverageRating}
          onPrevAverageRating={handlePrevAverageRating}
        />
      ) : (
        <div className="no-restaurant">Search your best restaurant!</div>
      )}
      <Modal show={isModalOpen} onClose={toggleModal}>
        <Info />
      </Modal>
    </div>
  );
};

export default App;
