from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    nickname = Column(String)
    results = relationship("Result", back_populates="user")

class Result(Base):
    __tablename__ = "results"
    result_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    total_score = Column(Integer)
    user = relationship("User", back_populates="results")