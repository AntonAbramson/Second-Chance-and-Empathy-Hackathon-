from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

Base = declarative_base()
class Case(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    case_number = Column(String, unique=True, nullable=False)
    case_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    filing_date = Column(String, nullable=False)
    status_date = Column(String, nullable=False)

    def __repr__(self):
            return "lol"
