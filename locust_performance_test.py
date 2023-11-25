from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def home_page(self):
        self.client.get("/")

    @task
    def calculator_page(self):
        self.client.get("/calculator")