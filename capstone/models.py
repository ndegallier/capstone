from sqlalchemy import Column, Integer, String, Sequence

from .database import Base

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
