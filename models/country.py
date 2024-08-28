from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Country(Base):
    __tablename__ = 'countries'

    country_id = Column(String(2), primary_key=True)
    country_name = Column(String(40))
    region_id = Column(Integer, ForeignKey('regions.region_id'))

    region = relationship("Region", back_populates="countries")
