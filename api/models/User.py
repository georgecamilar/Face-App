class User:
    def __init__(self, user_id, username, password):
        self._id = user_id
        self._username = username
        self._password = password

    def get_id(self):
        return self._id

    def get_password(self):
        return self._password

    def get_username(self):
        return self._username

    def set_username(self, value):
        self._username = value

    def set_password(self, value):
        self._password = value
