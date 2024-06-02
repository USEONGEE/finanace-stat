from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Restaurant, Review
from .serializers import RestaurantSerializer, ReviewSerializer
from .crowling_main import start_review_processing
from django_filters.rest_framework import DjangoFilterBackend


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["place_id"]

    def perform_create(self, serializer):
        platform = serializer.validated_data.get("platform")
        place_id = serializer.validated_data.get("place_id")
        if Restaurant.objects.filter(platform=platform, place_id=place_id).exists():
            raise ValidationError(
                "Restaurant with this platform and place_id already exists."
            )
        restaurant = serializer.save()
        # 리뷰 처리 스레드 시작
        start_review_processing(restaurant.id)


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["restaurant"]
