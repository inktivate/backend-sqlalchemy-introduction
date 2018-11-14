from sqlalchemy import Column, Integer, ForeignKey
from .database import Base


class telephone_model(Base):
    """Table of telephone entities with inherited CRUD methods."""
    __tablename__ = 'telephones'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    telephone_number = Column(Integer)
