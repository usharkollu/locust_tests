from locust import between,events
from tests.get_AllBookingIds import GetAllBookingIds
from utils.base import BaseUser
from load_config import LoadTestConfig
import gevent
import os
from datetime import datetime

config = LoadTestConfig.get()
env_name=os.getenv('LOCUST_ENV', 'stg').upper()
timestamp = datetime.now().strftime("%a, %b %d %Y")
print(f"Starting load test in {env_name} with configuration: {config}")


def parse_time(time_str):
    """Converts '15s', '1m', '1h' to seconds."""
    unit = time_str[-1].lower()
    value = int(time_str[:-1])
    if unit == 's': return value
    if unit == 'm': return value * 60
    if unit == 'h': return value * 3600
    return value

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    environment.runner.target_user_count = config['users']
    environment.runner.spawn_rate = config['spawn_rate']
    # Schedule the test to stop automatically based on config['run_time']
    run_time_seconds = parse_time(config['run_time'])

    gevent.spawn_later(run_time_seconds, lambda: environment.runner.quit())

@events.quitting.add_listener
def check_thresholds(environment, **kwargs):

    """Evaluate thresholds and set exit code."""
    stats = environment.stats.total
    thresholds=config['thresholds']

    p95 = stats.get_response_time_percentile(0.95)
    failure_rate = (stats.num_failures / stats.num_requests) * 100 if stats.num_requests > 0 else 0

    passed = True

    print("\n" + "="*50)
    print(f"PERFORMANCE TEST RESULTS on {timestamp} - {env_name}")
    print("="*50)

    if failure_rate > thresholds['failure_rate']:
        print(f"FAIL: Failure rate {failure_rate}% greater than {thresholds['failure_rate']}%")
        print("There are many failed requests. Please check the logs for more details.")
        passed = False
    elif p95 > thresholds['p95_response_time']:
        print(f"FAIL: P95 {p95}ms is greater than {thresholds['p95_response_time']}ms")
        passed = False
    else:
        print(f"PASS: Failure rate {failure_rate}% is less than {thresholds['failure_rate']}%")
        print(f"PASS: 95% of the requests completed within {p95}ms and is less than the threashold of {thresholds['p95_response_time']}ms")


    environment.process_exit_code = 0 if passed else 1
    print("="*50)


class MyTests(BaseUser):

    wait_time = between(1, 5)
    tasks = [GetAllBookingIds]


