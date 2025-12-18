from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(prefix="/item", tags=["Item"])

@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db, item)

@router.get("/", response_model=list[schemas.Item])
def get_items(db: Session = Depends(database.get_db)):
    return crud.get_items(db)
