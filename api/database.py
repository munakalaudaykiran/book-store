from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,session,declarative_base


DATABASE_URL = "postgresql://postgres:uday%4012345@localhost:5432/fastapi"


engine=create_engine(DATABASE_URL)
SessioLocal = sessionmaker(autocommit = False,autoflush= False, bind= engine)
Base = declarative_base()

def get_db():
    db = SessioLocal()
    try:
        yield db
    finally:
        db.close()