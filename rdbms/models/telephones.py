from sqlalchemy import Column, Integer, ForeignKey, String
from .database import Base


class TelephoneModel(Base):
    """Table of telephone entities with inherited CRUD methods."""
    __tablename__ = 'telephones'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    telephone_number = Column(String)
