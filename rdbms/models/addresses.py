from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base


class address_model(Base):
    """Table of address entities with inherited CRUD methods."""
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    street_address = Column(String)
    street_address_two = Column(String)
    city = Column(String)
    state = Column(String(2))
    postal_code = Column(String)
    country = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
