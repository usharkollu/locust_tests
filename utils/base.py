from utils.config_loader import load_config
import os
from locust import HttpUser

env_file = os.environ.get('LOCUST_ENV', 'prod')
config = load_config(env_file)
print("Debug: Loaded configuration:", {config.get('host'), config.get('user_name')})

class BaseUser(HttpUser):
    abstract = True
    host = config.get('host')