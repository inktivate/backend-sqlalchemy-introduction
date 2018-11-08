from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Post(Base):
    """Table of post entities with inherited CRUD methods."""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    title = Column(String(255))
    body = Column(String)
