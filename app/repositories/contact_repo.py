from app.database import collection
from datetime import datetime
from bson import ObjectId

class ContactRepository:
    async def create_contact(self, contact_data):
        contact_dict = contact_data.dict()
        contact_dict["created_at"] = datetime.now()
        result = await collection.insert_one(contact_dict)
        contact_dict["_id"] = str(result.inserted_id)
        return contact_dict

    async def get_contact_by_id(self, contact_id: str):
        contact = await collection.find_one({"_id": ObjectId(contact_id)})
        if contact:
            contact["_id"] = str(contact["_id"])
            return contact
        return None

    async def update_contact(self, contact_id: str, contact_data: dict):
        result = await collection.update_one(
            {"_id": ObjectId(contact_id)},
            {"$set": contact_data}
        )
        if result.modified_count > 0:
            updated_contact = await collection.find_one({"_id": ObjectId(contact_id)})
            updated_contact["_id"] = str(updated_contact["_id"])
            return updated_contact
        return None

    async def delete_contact(self, contact_id: str):
        result = await collection.delete_one({"_id": ObjectId(contact_id)})
        return result.deleted_count > 0