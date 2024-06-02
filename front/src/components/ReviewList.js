// src/components/ReviewList.js
import React, { useState, useEffect } from 'react';
import axios from '../axiosConfig';
import './ReviewList.css';

const ReviewList = ({ restaurantId, onAverageRating }) => {
    const [reviews, setReviews] = useState([]);

    useEffect(() => {
        axios.get(`/api/reviews/?restaurant=${restaurantId}`)
            .then(response => {
                setReviews(response.data);
                const average = response.data.reduce((acc, review) => acc + review.rating, 0) / response.data.length;
                onAverageRating(Math.round(average));
            })
            .catch(error => {
                console.error('There was an error fetching the reviews!', error);
            });
    }, [restaurantId, onAverageRating]);

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
