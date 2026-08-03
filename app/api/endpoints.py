from app.models.contact import ContactCreate, ContactResponse
from app.services.contact_service import ContactService
from fastapi import APIRouter, HTTPException

router = APIRouter()
service = ContactService()

@router.post("/contacts", response_model=ContactResponse)
async def create_contact(contact: ContactCreate):
    return await service.create_new_contact(contact)

@router.get("/contacts/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: str):
    contact = await service.get_contact_by_id(contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Kontakt nie został znaleziony")
    return contact
@router.put("/contacts/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: str, contact: ContactCreate):
    updated_contact = await service.update_contact(contact_id, contact)
    if not updated_contact:
        raise HTTPException(status_code=404, detail="Kontakt nie został znaleziony")
    return updated_contact

@router.delete("/contacts/{contact_id}")
async def delete_contact(contact_id: str):
    deleted = await service.delete_contact(contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Kontakt nie został znaleziony")
    return {"message": "Kontakt usunięty pomyślnie"}