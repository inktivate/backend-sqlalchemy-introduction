from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from .database import Base


class Education(Base):
    """Table of education entities with inherited CRUD methods."""
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    school = Column(String)
    school = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    graduated = Column(String)
    gpa = Column(Float)
