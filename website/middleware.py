# middleware.py
import datetime
import os
import logging
from django.utils import timezone
from django.conf import settings

logger = logging.getLogger(__name__)

class FadeOutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            file_path = os.path.join(settings.BASE_DIR, 'start_date.txt')
            with open(file_path, 'r') as file:
                start_date_str = file.read().strip()
                start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
                start_date = timezone.make_aware(start_date, timezone.get_default_timezone())
                now = timezone.now()
                days_passed = (now - start_date).days
                request.days_passed = days_passed
        except FileNotFoundError:
            logger.error("The start_date.txt file does not exist.")
            request.days_passed = 0
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            request.days_passed = 0

        response = self.get_response(request)
        return response
