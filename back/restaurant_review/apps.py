# apps.py
from django.apps import AppConfig
import schedule
import time
from datetime import datetime, timedelta
import threading
import sys


class RestaurantReviewConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "restaurant_review"

    def ready(self):
        if not "runserver" not in sys.argv:
            return

        from .models import Restaurant
        from django.utils import timezone

        def delete_inactive_restaurants():
            five_minutes_ago = timezone.now() - timedelta(minutes=5)
            inactive_restaurants = Restaurant.objects.filter(
                is_active=False, created_at__lt=five_minutes_ago
            )
            count = inactive_restaurants.count()
            inactive_restaurants.delete()
            print(f"Deleted {count} inactive restaurants")

        schedule.every(5).minutes.do(delete_inactive_restaurants)

        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(1)

        # 스케줄러를 백그라운드 스레드에서 실행
        scheduler_thread = threading.Thread(target=run_scheduler)
        scheduler_thread.daemon = True
        scheduler_thread.start()
