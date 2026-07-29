from fastapi import FastAPI
import routes
app = FastAPI(
    title="contacts management API",
    description="Nowoczesny system do zarządzania kontaktami oparty na FastAPI i MongoDB.",
    version="1.0.0"
)
app.include_router(routes.router)

