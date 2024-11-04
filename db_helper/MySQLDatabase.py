import mysql.connector

from db_helper.DatabaseInterface import DatabaseInterface


class MySQLDatabase(DatabaseInterface):
    _instance = None

    def __init__(self):
        self._connection = None

    def __new__(cls):
        # Singleton pattern used for connection to db
        if cls._instance is None:
            cls._instance = super(MySQLDatabase, cls).__new__(cls)
            cls._connection = None
        return cls._instance

    def connect(self):
        if self._connection is None:
            self._connection = mysql.connector.connect(
                host="localhost",
                user="user",
                password="secret",
                database="testdb"
            )
        return self._connection
