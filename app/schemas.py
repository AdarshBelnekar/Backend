from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import date


class BogieDetails(BaseModel):
    bogieNo: str
    dateOfIOH: str
    deficitComponents: str
    incomingDivAndDate: str
    makerYearBuilt: str

class BogieChecksheetCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieChecksheet: Dict[str, str]
    bmbcChecksheet: Dict[str, str]
    bogieDetails: Dict[str, str]

class BogieChecksheetResponse(BaseModel):
    class Data(BaseModel):
        formNumber: str
        inspectionBy: str
        inspectionDate: date
        status: str

    data: Data
    message: str
    success: bool

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

class WheelSpecificationSubmitResponse(BaseModel):
    class Data(BaseModel):
        formNumber: str
        submittedBy: str
        submittedDate: date
        status: str

    data: Data
    message: str
    success: bool

class WheelSpecificationResponse(BaseModel):
    class Item(BaseModel):
        formNumber: str
        submittedBy: str
        submittedDate: date
        fields: Dict[str, str]

    data: List[Item]
    message: str
    success: bool
