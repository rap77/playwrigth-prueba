# config/database.py
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables de entorno [[1]]

Base = declarative_base()

class PostgresAdapter:
    def __init__(self):
        self.engine = create_engine(
            os.getenv("POSTGRES_URL"),
            pool_size=5,           # Configuración de pool [[8]]
            max_overflow=10,
            pool_timeout=30,connect_args={"sslmode": "disable"}
        )

class SQLiteAdapter:
    def __init__(self):
        self.engine = create_engine(
            os.getenv("SQLITE_URL"),
            connect_args={"check_same_thread": False}  # Configuración multithread [[8]]
        )

class Database:
    def __init__(self, db_type: str):
        if db_type == "sqlite":
            adapter = SQLiteAdapter()
        elif db_type == "postgresql":
            adapter = PostgresAdapter()
        else:
            raise ValueError("Base de datos no soportada")
        
        self.engine = adapter.engine
        self.Session = sessionmaker(bind=self.engine)
        self.create_tables()  # Crea tablas automáticamente [[1]]

    def create_tables(self):
        inspector = inspect(self.engine)
        if not inspector.has_table("listings"):  # Verifica tabla [[1]]
            Base.metadata.create_all(self.engine)

    def save_results(self, results: list):
        session = self.Session()
        try:
            session.add_all(results)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e  # Propaga el error tras rollback [[9]]
        finally:
            session.close()