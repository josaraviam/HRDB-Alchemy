from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Region(Base):
    __tablename__ = 'regions'

    region_id = Column(Integer, primary_key=True)
    region_name = Column(String(25))

    countries = relationship("Country", back_populates="region")
