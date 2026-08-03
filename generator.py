import asyncio
import random
from app.database import db

IMIONA = ["Jan", "Anna", "Piotr", "Marta", "Krzysztof", "Ewa", "Michal", "Kasia", "Tomasz", "Mateusz"]
NAZWISKA = ["Kowalski", "Nowak", "Wisniewski", "Wojcik", "Kowalczyk", "Kaminski", "Lewandowski", "Zielinski"]
DOMENY = ["gmail.com", "yahoo.com", "wp.pl", "onet.pl", "pwr.edu.pl"]

async def generuj_kontakty(ilosc: int = 5000):
    print(f"⏳ Generuję {ilosc} kontaktów...")
    kontakty = []

    for _ in range(ilosc):
        imie = random.choice(IMIONA)
        nazwisko = random.choice(NAZWISKA)
        email = f"{imie.lower()}.{nazwisko.lower()}{random.randint(1, 999)}@{random.choice(DOMENY)}"
        telefon = f"{random.randint(500, 888)}{random.randint(100, 999)}{random.randint(100, 999)}"

        kontakty.append({
            "name": f"{imie} {nazwisko}",
            "phone": telefon,
            "email": email
        })

    result = await db.contacts.insert_many(kontakty)
    print(f" Pomyślnie dodano {len(result.inserted_ids)} kontaktów do bazy!")

if __name__ == "__main__":
    asyncio.run(generuj_kontakty(5000))