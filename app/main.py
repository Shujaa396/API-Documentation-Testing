from fastapi import FastAPI
from app.routers import invoice, item, user, reports
from app.database import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nexus POS Week 8")

# Routers
app.include_router(invoice.router)
app.include_router(item.router)
app.include_router(user.router)
app.include_router(reports.router)

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Backend running"}
