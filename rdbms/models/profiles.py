from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class profile_model(Base):
    """Table of profile entities with inherited CRUD methods."""
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    nationality = Column(String)
