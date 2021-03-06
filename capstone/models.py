from sqlalchemy import Column, Integer, String, Sequence, Text, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base, session

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    username = Column(String(128))
    email = Column(String(128))
    # photo
    # bio
    
    def as_dictionary(self):
        user = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email
        }

class Equity(Base):
    __tablename__ =  'equity'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ticker = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    close = Column(Float)

    def as_dictionary(self):
        equity = {
            "id": self.id,
            "ticker": self.ticker,
            "date": self.date,
            "close": self.close
        }
        return equity

                        
