from locust import HttpUser, TaskSet, task, between

# Définition des tâches de SimpleUser
class SimpleTasks(TaskSet):
    @task(1)
    def home(self):
        self.client.get("/")

    @task(2)
    def fast(self):
        self.client.get("/fast")

    @task(3)
    def medium(self):
        self.client.get("/medium")

    @task(4)
    def heavy(self):
        self.client.get("/heavy")

    @task(1)
    def echo(self):
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload)

# Définition des tâches de HeavyUser
class HeavyTasks(TaskSet):
    @task(1)
    def home(self):
        self.client.get("/")

    @task(2)
    def fast(self):
        self.client.get("/fast")

    @task(3)
    def medium(self):
        self.client.get("/medium")

    @task(4)
    def heavy(self):
        self.client.get("/heavy")

    @task(1)
    def echo(self):
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload)

class SimpleUser(HttpUser):
    tasks = [SimpleTasks]
    wait_time = between(1, 5)  # Temps d'attente entre chaque requête pour SimpleUser
    weight = 2

class HeavyUser(HttpUser):
    tasks = [HeavyTasks]
    wait_time = between(5, 10)  # Temps d'attente entre chaque requête pour HeavyUser
    weight = 98

