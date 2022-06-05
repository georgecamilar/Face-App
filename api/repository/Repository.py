import mysql.connector


class Repository:
    def __init__(self):
        self._connection = self.create_connection()

    def create_connection(self):
        return mysql.connector.connect(
            host='localhost',
            user='test',
            port=8889,
            password='test',
            database='licenta'
        )

    def add_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into User values (" + user.get_id() + "," + user.get_username() + "," + user.get_password())
        self._connection.commit()

    def is_user(self, request_username, request_password):
        cursor = self._connection.cursor()
        cursor.execute("select * from User where username=" + request_username)
        self._connection.commit()
        for (id, request_username, password) in cursor:
            if password == request_password:
                return True
        return False
