from sqlalchemy import Column, Integer, ForeignKey
from .database import Base


class Vital(Base):
    """Table of vital entities with inherited CRUD methods."""
    __tablename__ = 'vitals'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    height = Column(Integer)
    weight = Column(Integer)
