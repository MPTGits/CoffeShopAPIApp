from app.configuration.database_connection import DatabaseConnection


class BaseGateway:
    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn