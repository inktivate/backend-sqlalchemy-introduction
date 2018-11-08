from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv('./.env')

engine = create_engine(os.environ['DATABASE'], echo=True)
connection = engine.connect()
Session = sessionmaker(bind=connection)
session = Session()

Base = declarative_base()
