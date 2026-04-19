class UserController:
    def __init__(self):
        self.database = {}  # Simulate database

    def add_user(self, username, email):
        if username in self.database:
            raise ValueError("User already exists")
        self.database[username] = email
        return True

    def get_user(self, username):
        return self.database.get(username, None)

    def delete_user(self, username):
        if username in self.database:
            del self.database[username]


class GetSpeed:
    def get_speed(self,speed):
        if speed > 100:
            return "high"
        if speed < 50:
            return "low"
        else:
            return "medium"
