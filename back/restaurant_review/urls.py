from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r"restaurants", RestaurantViewSet)
router.register(r"reviews", ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
