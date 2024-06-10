from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Restaurant(models.Model):
    PLATFORM_CHOICES = [
        ("kakaomap", "kakaomap"),
        # 필요에 따라 더 많은 플랫폼 추가
    ]

    name = models.CharField(max_length=255, default="restaurant")
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    place_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    average_rating = models.CharField(
        default="0.0점", max_length=10
    )  # 평균 평점 필드 추가

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # 새로운 레코드를 추가할 때만 중복 체크
        if (
            not self.pk
            and Restaurant.objects.filter(
                platform=self.platform, place_id=self.place_id
            ).exists()
        ):
            raise ValidationError(
                "Restaurant with this platform and place_id already exists."
            )
        super().save(*args, **kwargs)

    def activate_restaurant(self):
        self.is_active = True
        self.save(update_fields=["is_active"])


class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="reviews"
    )
    review_text = models.TextField()
    positive_score = models.FloatField()
    negative_score = models.FloatField()
    neu_score = models.FloatField(default=0.0)
    compound_score = models.FloatField(default=0.0)
    rating = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
