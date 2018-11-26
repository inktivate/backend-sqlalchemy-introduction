from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class AccountModel(Base):
    """Table of account entities with inherited CRUD methods."""
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    social_media_url = Column(String)
