from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(prefix="/invoice", tags=["Invoice"])

@router.post("/", response_model=schemas.Invoice)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(database.get_db)):
    return crud.create_invoice(db, invoice)

@router.get("/", response_model=list[schemas.Invoice])
def get_invoices(db: Session = Depends(database.get_db)):
    return crud.get_invoices(db)
