from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Tag(Base):
    """Table of tag entities with inherited CRUD methods."""
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    body = Column(String(50))
