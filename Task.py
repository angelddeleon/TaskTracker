

class Task:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status
        }

    def __str__(self):
        return f"id: {self.id} task: {self.name} status: {self.status}"
