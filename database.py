from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker 

DB_URL="sqlite:///./students.db"
engine=create_engine(DB_URL)

Base=declarative_base()

sessionLocal=sessionmaker(autocommit=False,bind=engine)