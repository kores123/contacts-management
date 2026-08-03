from app.repositories.contact_repo import ContactRepository

class ContactService:
    def __init__(self):
        self.repository = ContactRepository()

    async def create_new_contact(self, contact_data):
        return await self.repository.create_contact(contact_data)

    async def get_contact_by_id(self, contact_id: str):
        return await self.repository.get_contact_by_id(contact_id)

    async def update_contact(self, contact_id: str, contact_data):
        return await self.repository.update_contact(contact_id, contact_data.dict())

    async def delete_contact(self, contact_id: str):
        return await self.repository.delete_contact(contact_id)