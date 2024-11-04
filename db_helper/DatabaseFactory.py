from db_helper.MySQLDatabase import MySQLDatabase
from db_helper.PostgreSQLDatabase import PostgreSQLDatabase


# Factory pattern used to create return database according to type
class DatabaseFactory:
    @staticmethod
    def create_database(db_type):
        if db_type == 'mysql':
            return MySQLDatabase()
        elif db_type == 'postgres':
            return PostgreSQLDatabase()
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
