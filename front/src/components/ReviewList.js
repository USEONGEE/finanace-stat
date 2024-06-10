// src/components/ReviewList.js
import React, { useState, useEffect } from 'react';
import axios from '../axiosConfig'
import './ReviewList.css';

const ReviewList = ({ restaurantId, onAverageRating, onPrevAverageRating }) => {
    const [reviews, setReviews] = useState([]);

    const checkIsActive = async (restaurantId) => {
        try {
            const response = await axios.get(`/api/restaurants/${restaurantId}/`);
            if (response.data.is_active) {
                onPrevAverageRating(response.data.average_rating);
            }
            return response.data.is_active;
        } catch (error) {
            console.error('There was an error checking the restaurant status!', error);
            return false;
        }
    };

    useEffect(() => {
        const fetchReviews = async () => {
            try {
                // Check if the restaurant is active and set previous average rating if true
                await checkIsActive(restaurantId);

                // Fetch reviews for the restaurant
                const response = await axios.get(`/api/reviews/?restaurant=${restaurantId}`);
                setReviews(response.data);

                // Calculate the average rating from the fetched reviews
                const average = response.data.reduce((acc, review) => acc + review.rating, 0) / response.data.length;
                onAverageRating(Math.round(average));
            } catch (error) {
                console.error('There was an error fetching the reviews!', error);
            }
        };

        fetchReviews();
    }, [restaurantId, onAverageRating, onPrevAverageRating]);

    return (
        <div className="review-list">
            <h2>Reviews</h2>
            <table>
                <thead>
                    <tr>
                        <th>Review Text</th>
                        <th>Rating</th>
                    </tr>
                </thead>
                <tbody>
                    {reviews.map(review => (
                        <tr key={review.id}>
                            <td>{review.review_text}</td>
                            <td>{review.rating}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ReviewList;
