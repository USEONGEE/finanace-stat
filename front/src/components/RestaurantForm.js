import React, { useState } from 'react';
import axios from '../axiosConfig';
import './RestaurantForm.css';

const RestaurantForm = ({ onRestaurantSubmit }) => {
    const [placeId, setPlaceId] = useState('');
    const [loading, setLoading] = useState(false);
    const [dots, setDots] = useState(1);

    const checkIsActive = async (restaurantId) => {
        try {
            const response = await axios.get(`/api/restaurants/${restaurantId}/`);
            return response.data.is_active;
        } catch (error) {
            console.error('There was an error checking the restaurant status!', error);
            return false;
        }
    };

    const fetchReviews = async (restaurantId) => {
        const isActive = await checkIsActive(restaurantId);
        if (isActive) {
            setLoading(false);
            onRestaurantSubmit(restaurantId);
        } else {
            setTimeout(() => fetchReviews(restaurantId), 5000);
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setDots(1);

        try {
            const existingRestaurantResponse = await axios.get(`/api/restaurants/?place_id=${placeId}`);
            if (existingRestaurantResponse.data.length > 0) {
                const restaurant = existingRestaurantResponse.data[0];
                if (restaurant.is_active) {
                    setLoading(false);
                    onRestaurantSubmit(restaurant.id);
                } else {
                    fetchReviews(restaurant.id);
                }
            } else {
                const response = await axios.post('/api/restaurants/', {
                    place_id: placeId,
                    platform: 'kakaomap',
                });
                fetchReviews(response.data.id);
            }
        } catch (error) {
            if (error.response && error.response.status === 404) {
                // 식당이 없는 경우, 새로운 식당 생성
                try {
                    const response = await axios.post('/api/restaurants/', {
                        place_id: placeId,
                        platform: 'kakaomap',
                    });
                    fetchReviews(response.data.id);
                } catch (postError) {
                    console.error('There was an error creating the restaurant!', postError);
                    setLoading(false);
                }
            } else {
                console.error('There was an error creating or checking the restaurant!', error);
                setLoading(false);
            }
        }
    };

    React.useEffect(() => {
        if (loading) {
            const interval = setInterval(() => {
                setDots(prevDots => (prevDots % 3) + 1);
            }, 500);
            return () => clearInterval(interval);
        }
    }, [loading]);

    return (
        <div>
            <form className="restaurant-form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={placeId}
                    onChange={(e) => setPlaceId(e.target.value)}
                    placeholder="Enter Restaurant ID"
                    className="input-field"
                />
                <button type="submit" className="submit-button">Submit</button>
            </form>
            {loading && <div>Analysis in progress{'.'.repeat(dots)}</div>}
        </div>
    );
};

export default RestaurantForm;
