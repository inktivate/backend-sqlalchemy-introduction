from sqlalchemy import Column, Integer, ForeignKey, Float
from .database import Base


class VitalModel(Base):
    """Table of vital entities with inherited CRUD methods."""
    __tablename__ = 'vitals'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    height = Column(Float)
    weight = Column(Float)
