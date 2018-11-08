from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Comment(Base):
    """Table of comment entities with inherited CRUD methods."""
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    body = Column(String)
