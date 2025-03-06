import random
import string
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone


# def get_random_string(length):
#     characters = string.ascii_letters + string.digits
#     return "".join(random.choice(characters) for _ in range(length))


# def get_random_date(start_date=datetime(2000, 1, 1), end_date=datetime(2024, 6, 30)):
#     delta = end_date - start_date
#     random_days = random.randint(0, delta.days)
#     random_date = start_date + timedelta(days=random_days)
#     return random_date


# def get_random_datetime(
#     start=datetime(2020, 1, 1, 0, 0, 0), end=datetime(2023, 12, 31, 23, 59, 59)
# ):
#     delta = end - start
#     int_delta = int(delta.total_seconds())
#     random_second = random.randint(0, int_delta)
#     random_datetime = start + timedelta(seconds=random_second)
#     return timezone.make_aware(random_datetime, timezone.get_current_timezone())


# def get_random_int(start, end):
#     return random.randint(start, end)


# def get_random_decimal(start, end, rounding=2):
#     return round(random.uniform(start, end), rounding)


# def get_random_country():
#     return random.choice(list(countries))[0]


class Command(BaseCommand):
    help = "Add default data"

    def handle(self, *args, **kwargs):
        print("Hello, world!")
