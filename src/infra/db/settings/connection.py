from sqlalchemy import create_engine

class DBConnectionHandler:

    def __init__(self):
        self.__connection__string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'root',
            'secret',
            'localhost',
            '3306',
            'clean_database'
        )
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        engine = create_engine(self.__connection__string)
        return engine

    def get_engine(self):
        return self.__engine
    