import sys
import os
# This must stay at the top
sys.path.append(os.getcwd())

from locust import between  

try:
    from tests.get_AllBookingIds import GetAllBookingIds
    from utils.config_loader import ConfigLoader
    from utils.base import BaseUser # <--- IMPORT YOUR BASE CLASS HERE
except ImportError:
    from get_AllBookingIds import GetAllBookingIds
    from config_loader import ConfigLoader
    from base import BaseUser # <--- FALLBACK FOR FLATTENED FILES

class MyTests(BaseUser):
    wait_time = between(1, 5)
    tasks = [GetAllBookingIds]