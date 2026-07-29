import motor.motor_asyncio
MONGO_URI = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
DB = client.file
collection = DB.contact