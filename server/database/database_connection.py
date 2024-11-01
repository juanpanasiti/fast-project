from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker


class DatabaseConnection:
    def __init__(self, str_conn: str):
        self.str_conn: str = str_conn
        self.__engine: Engine = None
        self.__session: Session = None

    @property
    def session(self):
        if self.__session is None:
            Session = sessionmaker(bind=self.engine)
            self.__session = Session()
        return self.__session

    @property
    def engine(self):
        if self.__engine is None:
            self.__engine = create_engine(self.str_conn)
        return self.__engine

    def connect(self) -> bool:
        try:
            self.session.connection()
            print('\033[92m', 'Conexión a la base de datos exitosa', '\033[0m')
            return True
        except Exception as ex:
            print('\033[91m', 'Falló la conexión a la base de datos', '\033[0m')
            print(str(ex))
            return False

    def disconnect(self) -> None:
        if self.session:
            self.session.close()
        # !DELETE PRINT
        print('\033[93m', 'Base de datos desconectada', '\033[0m')