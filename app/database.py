import motor.motor_asyncio
MONGO_URI = "mongodb://localhost:27017"
#MONGO_URI = "mongodb+srv://kubasonf:2222@smrov.id2xxpp.mongodb.net/?appName=smrov"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.file
collection = db.contacts