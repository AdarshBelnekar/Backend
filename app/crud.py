from sqlalchemy.orm import Session
from . import models, schemas

def create_bogie_form(db: Session, form: schemas.BogieChecksheetCreate):
    db_form = models.BogieChecksheet(
        formNumber=form.formNumber,
        inspectionBy=form.inspectionBy,
        inspectionDate=form.inspectionDate,
        bogieChecksheet=form.bogieChecksheet,
        bmbcChecksheet=form.bmbcChecksheet,
        bogieDetails=form.bogieDetails,
        status="Saved"
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return {
        "formNumber": db_form.formNumber,
        "inspectionBy": db_form.inspectionBy,
        "inspectionDate": db_form.inspectionDate,
        "status": db_form.status
    }

def get_wheel_specifications(db: Session, formNumber=None, submittedBy=None, submittedDate=None):
    query = db.query(models.WheelSpecification)
    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)
    return query.all()


def create_wheel_specification(db: Session, form: schemas.WheelSpecificationCreate):
    db_form = models.WheelSpecification(
        formNumber=form.formNumber,
        submittedBy=form.submittedBy,
        submittedDate=form.submittedDate,
        fields=form.fields,
        status="Saved"
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form