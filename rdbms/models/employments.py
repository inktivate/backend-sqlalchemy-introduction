from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base


class employment_model(Base):
    """Table of employment entities with inherited CRUD methods."""
    __tablename__ = 'employments'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    company = Column(String)
    occupation = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
