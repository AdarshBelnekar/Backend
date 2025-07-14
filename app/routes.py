from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Post api for the bogie-checksheet  
@router.post("/api/forms/bogie-checksheet", response_model=schemas.BogieChecksheetResponse)
def create_bogie_checksheet(form: schemas.BogieChecksheetCreate, db: Session = Depends(get_db)):
    saved = crud.create_bogie_form(db, form)
    return {
        "data": saved,
        "message": "Bogie checksheet submitted successfully.",
        "success": True
    }
# Get data from wheel-specification
@router.get("/api/forms/wheel-specifications", response_model=schemas.WheelSpecificationResponse)
def get_specs(
    formNumber: str = Query(None),
    submittedBy: str = Query(None),
    submittedDate: str = Query(None),
    db: Session = Depends(get_db),
):
    records = crud.get_wheel_specifications(db, formNumber, submittedBy, submittedDate)
    data = [
        {
            "formNumber": r.formNumber,
            "submittedBy": r.submittedBy,
            "submittedDate": str(r.submittedDate),
            "fields": r.fields,
        }
        for r in records
    ]
    return {
        "data": data,
        "message": "Filtered wheel specification forms fetched successfully.",
        "success": True
    }

#Post the data to wheel-specifications
@router.post("/api/forms/wheel-specifications", response_model=schemas.WheelSpecificationSubmitResponse, status_code=201)
def submit_wheel_specification(form: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)):
    saved_form = crud.create_wheel_specification(db, form)
    return {
        "data": {
            "formNumber": saved_form.formNumber,
            "submittedBy": saved_form.submittedBy,
            "submittedDate": str(saved_form.submittedDate),
            "status": saved_form.status,
        },
        "message": "Wheel specification submitted successfully.",
        "success": True
    }
