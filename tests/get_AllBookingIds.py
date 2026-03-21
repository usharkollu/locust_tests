from locust import  TaskSet,task,tag

class GetAllBookingIds(TaskSet):
    # Created as taskset instead of HttpUser to avoid wait_time and to be used as a task in locustfile.py
    # No wait_time needed here, it will use the User's wait_time

    @task
    @tag('smoke')
    def get_all_bookings(self):
        # Using 'with' + 'catch_response' is the best practice for custom error handling
        with self.client.get("/booking", catch_response=True) as response:
            if response.status_code == 200:
                try:
                    data = response.json()
                    # Safe list comprehension
                    bookingIds = [item['bookingid'] for item in data if 'bookingid' in item]
                    print(f"Success: Found {len(bookingIds)} bookings")
                    response.success() 
                except Exception as e:
                    response.failure(f"JSON Parsing failed: {str(e)}")
            else:
                # This ensures the status code (e.g., 404, 500) shows up in your HTML report
                response.failure(f"Failed with status code: {response.status_code}")