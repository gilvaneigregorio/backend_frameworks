import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)