from rest_framework import serializers
from .models import Restaurant, Review


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "platform", "place_id", "is_active"]
        read_only_fields = ["id", "is_active"]
        extra_kwargs = {
            "name": {"required": False},
            "platform": {"required": False},
        }


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "restaurant",
            "review_text",
            "positive_score",
            "negative_score",
            "neu_score",
            "compound_score",
            "rating",
        ]
