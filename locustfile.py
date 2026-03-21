import sys
import os

# This line is mandatory for Azure to 'see' the uploaded files
sys.path.append(os.getcwd())

try:
    # 1. Try importing via the folder (Standard way)
    from tests.get_AllBookingIds import GetAllBookingIds
    from utils.config_loader import ConfigLoader
except ImportError:
    # 2. Try importing directly (The 'Flattened' way Azure often uses)
    from get_AllBookingIds import GetAllBookingIds
    from config_loader import ConfigLoader

class MyTests(BaseUser):
    wait_time = between(1, 5)
    tasks = [GetAllBookingIds]


