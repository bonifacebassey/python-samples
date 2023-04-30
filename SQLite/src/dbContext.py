import sqlite3


class DbContext:
    __DB_LOCATION = "../sql.db"

    def __init__(self, db=None):
        self.__db_location = db if db is not None else self.__DB_LOCATION
        self.__db_connection = sqlite3.connect(self.__DB_LOCATION)
        self.__cursor = self.__db_connection.cursor()

    def execute(self, statement):
        return self.__cursor.execute(statement)

    def executemany(self, statement, values):
        return self.__cursor.executemany(statement, values)

    def fetchall(self):
        return self.__cursor.fetchall()

    def fetchmany(self, n):
        return self.__cursor.fetchmany(n)

    def fetchone(self):
        return self.__cursor.fetchone()

    def commit(self):
        self.__db_connection.commit()

    def __del__(self):
        self.__db_connection.close()
