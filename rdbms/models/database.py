from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///development.db', echo=True)
connection = engine.connect()
Session = sessionmaker(bind=connection)
session = Session()

Base = declarative_base()
