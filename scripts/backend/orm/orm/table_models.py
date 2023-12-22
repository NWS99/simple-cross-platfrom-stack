"""
This Module is used to create the SQL Table Model
"""

from sqlalchemy import Boolean, Column, ForeignKey, \
    Integer, String, DateTime
from orm.database_connection import Base

class User(Base):
    Name = String()
    