from sqlalchemy import Column, Integer, String
from .database import Base


class UserModel(Base):
    """Table of user entities with inherited CRUD methods."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String)
    email = Column(String)
