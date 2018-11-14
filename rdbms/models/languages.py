from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class language_model(Base):
    """Table of language entities with inherited CRUD methods."""
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    language = Column(String)
