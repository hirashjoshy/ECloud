import uuid
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from database import get_conn

Base = declarative_base()
engine = get_conn()

def generate_uuid():
    """
    Generate a new UUID and return it as a string.
    """
    return str(uuid.uuid4())

class Users(Base):
    __tablename__ = "Users"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    status = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.status = "Active"
        

    