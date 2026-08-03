from fastapi import FastAPI
from app.api.endpoints import router as contact_router
from app.api.users import router as user_router
app = FastAPI(
    title="contacts management API",
    description="Nowoczesny system do zarządzania kontaktami oparty na FastAPI i MongoDB.",
    version="1.0.0",
)

app.include_router(contact_router)
app.include_router(user_router)