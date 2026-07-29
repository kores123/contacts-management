from fastapi import APIRouter, HTTPException
from models import Contact
from database import collection
from pymongo.errors import DuplicateKeyError
router = APIRouter(tags=["contacts management"])
@router.get("/")
async def welcome():
    return {"message": "Witaj w kartotece kontaktów!"}
@router.get("/contacts")
async def list_contacts():
    contacts = await collection.find({}, {"_id": 0}).to_list(length=100)
    return {"contacts": contacts}

@router.post("/contacts")
async def add_contacts(new_contact: Contact):
    try:
        await collection.insert_one(new_contact.model_dump())
        return {"message": "Contact received"}
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Contact already exists")
@router.get("/contacts/{contact_id}")
async def get_contact(contact_id: int):
    contact = await collection.find_one({"id": contact_id}, {"_id": 0})
    if contact:
            return contact
    raise HTTPException(status_code=404, detail="Contact not found")

@router.delete("/contacts/{contact_id}")
async def delete_contact(contact_id: int):
    result = await collection.delete_one({"id": contact_id})
    if result.deleted_count == 1:
            return {"message": "Contact deleted"}
    raise HTTPException(status_code=404, detail="Contact not found")

@router.put("/contacts/{contact_id}")
async def update_contact(contact_id: int, new_contact: Contact):
    result = await collection.update_one(
        {"id": contact_id},
        {"$set": new_contact.model_dump()}
    )
    if result.matched_count == 1:
        return {"message": "Contact updated"}
    raise HTTPException(status_code=404, detail="Contact not found")