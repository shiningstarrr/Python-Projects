"""
This file writes about sqlalchemy complementaion.
"""

# Import the SqlAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Gnaw2011@localhost/fastapi' # Create a database URL for SqlAlchemy: SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>'
#SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL) # Create engine and session for sqlalchemy to connect to postgres database
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

# create dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
Below connect through psycopg2 rather than sqlalchemy
"""
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost',database='fastapi',user='postgres',password='Gnaw2011',cursor_factory=RealDictCursor)
#         cursor = conn.cursor() # A cursor is a database object that allows you to traverse the results of a SQL query one row at a time.
#         print("database connection was successful")
#         break
#     except Exception as error: 
#         print("connecting to dataabse failed")
#         print("error: ", error)
#         time.sleep(2) # retry connecting every 2 seconds