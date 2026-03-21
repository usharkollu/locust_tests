from locust import between
from tests.get_AllBookingIds import GetAllBookingIds
from utils.base import BaseUser

class MyTests(BaseUser):
    wait_time = between(1, 5)
    tasks = [GetAllBookingIds]


