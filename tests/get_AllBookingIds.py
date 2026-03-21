from locust import  TaskSet,task,tag

class GetAllBookingIds(TaskSet):
    # Created as taskset instead of HttpUser to avoid wait_time and to be used as a task in locustfile.py
    # No wait_time needed here, it will use the User's wait_time

    @task
    @tag('smoke')
    def get_all_bookings(self):
        response = self.client.get("/booking",catch_response=True)
        print(response.status_code)
        #print(response)
        value=response.json()
        bookingIds=[value['bookingid'] for value in value]
        print(bookingIds)