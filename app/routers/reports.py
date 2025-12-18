from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models
from datetime import datetime

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/")
def get_reports(user_id: int = None, date: str = None, db: Session = Depends(database.get_db)):
    query = db.query(models.Invoice)

    if user_id:
        query = query.filter(models.Invoice.user_id == user_id)
    if date:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        query = query.filter(models.Invoice.created_at >= date_obj)

    return query.all()
