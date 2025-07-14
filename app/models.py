from sqlalchemy import Column, String, Integer, Date, JSON
from .database import Base

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, index=True)
    inspectionBy = Column(String)
    inspectionDate = Column(Date)
    status = Column(String)
    bogieChecksheet = Column(JSON)
    bmbcChecksheet = Column(JSON)
    bogieDetails = Column(JSON)

class WheelSpecification(Base):
    __tablename__ = "wheel_specification"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, index=True)
    submittedBy = Column(String)
    submittedDate = Column(Date)
    fields = Column(JSON)
    status = Column(String)