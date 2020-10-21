import yaml
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


class Database:
    def __init__(self, app):
        # Configure db
        self.engine = None
        self.db_session = None
        self.create_engine()
        self.Base = declarative_base()
        self.Base.query = self.db_session.query_property()

    def init_tables(self):
        self.Base.metadata.create_all(bind=self.engine)

    def create_engine(self):
        self.engine = create_engine(Database.get_connection())
        self.db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))

    @staticmethod
    def get_connection_string(self):
        config = yaml.load(open('db.yaml'))
        host = config['mysql_host']
        user = config['mysql_user']
        password = config['mysql_password']
        database = config['mysql_db']
        connection_string = f"mysql://{user}:{password}@{host}/{database}"


    def get_connection(self):        
        return self.db.connection;