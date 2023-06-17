from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, Hotel, Room
from uuid import UUID

app = FastAPI()


db: List[User] = [
    User(
        id=UUID("68bddf1a-a542-4842-a59d-8967922ad9a8"), 
        first_name="Henrique", 
        last_name="Corte", 
        gender=Gender.male,
        roles=[Role.admin, Role.student]
    ),
    User(
        id=UUID("49e33899-5cb7-4eb5-8a2a-3801007319d0"), 
        first_name="Tais", 
        last_name="Oliveira", 
        gender=Gender.female,
        roles=[Role.user]
    )
]


db_hotels: List[Hotel] = [
    Hotel(
        hotel_id=UUID("68bddf1a-a542-4842-a59d-8967922ad9a8"),
        name="Hotel A",
        grounds="Grounds A",
        address="Address A",
        city="City A",
        region="Region A",
        latitude=123.456,
        longitude=789.012,
        phone="1234567890",
        email="hotelA@example.com",
        website="www.hotelA.com",
        description="Hotel A description",
        stars=5,
        price_range={"min": 100, "max": 500},
        services="Services A",
        map_url="www.mapA.com",
        photos=["photo1.jpg", "photo2.jpg"],
        rooms=[
            Room(room_id=UUID("a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"), hotel_id=UUID("68bddf1a-a542-4842-a59d-8967922ad9a8"), name="Room 1", description="Room 1 description", price=200, beds=2),
            Room(room_id=UUID("b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2"), hotel_id=UUID("68bddf1a-a542-4842-a59d-8967922ad9a8"), name="Room 2", description="Room 2 description", price=300, beds=3),
        ]
    ),
    Hotel(
        hotel_id=UUID("49e33899-5cb7-4eb5-8a2a-3801007319d0"),
        name="Hotel B",
        grounds="Grounds B",
        address="Address B",
        city="City B",
        region="Region B",
        latitude=987.654,
        longitude=210.987,
        phone="0987654321",
        email="hotelB@example.com",
        website="www.hotelB.com",
        description="Hotel B description",
        stars=4,
        price_range={"min": 50, "max": 300},
        services="Services B",
        map_url="www.mapB.com",
        photos=["photo3.jpg", "photo4.jpg"],
        rooms=[
            Room(room_id=UUID("c3c3c3c3-c3c3-c3c3-c3c3-c3c3c3c3c3c3"), hotel_id=UUID("49e33899-5cb7-4eb5-8a2a-3801007319d0"), name="Room 3", description="Room 3 description", price=150, beds=1),
            Room(room_id=UUID("d4d4d4d4-d4d4-d4d4-d4d4-d4d4d4d4d4d4"), hotel_id=UUID("49e33899-5cb7-4eb5-8a2a-3801007319d0"), name="Room 4", description="Room 4 description", price=250, beds=2),
        ]
    )
]



@app.get("/")
async def root():
    # await foo()
    return {"Api": "Users"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.get("/api/v1/user/{user_id}")
async def fetch_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )


@app.post("/api/v1/user")
async def register_user(user: User):
    db.append(user)
    return {"New user id": user.id}


@app.put("/api/v1/user/{user_id}")
async def update_user(user_id: UUID, updated_user: User):
    for user in db:
        if user.id == user_id:
            if updated_user.first_name:
                user.first_name = updated_user.first_name
            if updated_user.last_name:
                user.last_name = updated_user.last_name
            if updated_user.gender:
                user.gender = updated_user.gender
            if updated_user.roles:
                user.roles = updated_user.roles
            return "Updated User"

    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exist"
    )



@app.delete("/api/v1/user/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return "Deleted User!"

    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )
    
    
    
@app.get("/api/v1/hotels")
async def fetch_hotels():
    return db_hotels


@app.get("/api/v1/hotel/{hotel_id}")
async def fetch_hotel(hotel_id: UUID):
    for hotel in db_hotels:
        if hotel.hotel_id == hotel_id:
            return hotel

    raise HTTPException(
        status_code=404,
        detail=f"Hotel with id: {hotel_id} does not exist"
    )


@app.get("/api/v1/hotel/{hotel_id}/rooms")
async def fetch_rooms_by_hotel(hotel_id: UUID):
    for hotel in db_hotels:
        if hotel.hotel_id == hotel_id:
            return hotel.rooms

    raise HTTPException(
        status_code=404,
        detail=f"Hotel with id: {hotel_id} does not exist"
    )


@app.post("/api/v1/hotel")
async def create_hotel(hotel: Hotel):
    db_hotels.append(hotel)
    return {"New hotel id": hotel.hotel_id}


@app.put("/api/v1/hotel/{hotel_id}")
async def update_hotel(hotel_id: UUID, updated_hotel: Hotel):
    for hotel in db_hotels:
        if hotel.hotel_id == hotel_id:
            if updated_hotel.name:
                hotel.name = updated_hotel.name
            if updated_hotel.grounds:
                hotel.grounds = updated_hotel.grounds
            if updated_hotel.address:
                hotel.address = updated_hotel.address
            # Update other fields as needed
            return "Updated Hotel"

    raise HTTPException(
        status_code=404,
        detail=f"Hotel with id: {hotel_id} does not exist"
    )


@app.delete("/api/v1/hotel/{hotel_id}")
async def delete_hotel(hotel_id: UUID):
    for hotel in db_hotels:
        if hotel.hotel_id == hotel_id:
            db_hotels.remove(hotel)
            return "Deleted Hotel!"

    raise HTTPException(
        status_code=404,
        detail=f"Hotel with id: {hotel_id} does not exist"
    )
    
    
@app.get("/api/v1/hotel/{hotel_id}/room/{room_id}")
async def get_room(hotel_id: UUID, room_id: UUID):
    for hotel in db_hotels:
        if hotel.hotel_id == hotel_id:
            for room in hotel.rooms:
                if room.room_id == room_id:
                    return room

    raise HTTPException(
        status_code=404,
        detail=f"Hotel or room with the provided ids does not exist"
    )


@app.post("/api/v1/hotel/{hotel_id}/room")
async def add_room_to_hotel(hotel_id: UUID, room: Room):
    for hotel in db_hotels:
        if hotel.hotel_id == hotel_id:
            room.room_id = uuid4()
            room.hotel_id = hotel_id
            hotel.rooms.append(room)
            return {"New room id": room.room_id}
    
    raise HTTPException(
        status_code=404,
        detail=f"Hotel with id: {hotel_id} does not exist"
    )


@app.delete("/api/v1/hotel/{hotel_id}/room/{room_id}")
async def remove_room_from_hotel(hotel_id: UUID, room_id: UUID):
    for hotel in db_hotels:
        if hotel.hotel_id == hotel_id:
            for room in hotel.rooms:
                if room.room_id == room_id:
                    hotel.rooms.remove(room)
                    return "Room deleted"

    raise HTTPException(
        status_code=404,
        detail=f"Hotel or room with the provided ids does not exist"
    )


@app.put("/api/v1/hotel/{hotel_id}/room/{room_id}")
async def update_room(hotel_id: UUID, room_id: UUID, updated_room: Room):
    for hotel in db_hotels:
        if hotel.hotel_id == hotel_id:
            for room in hotel.rooms:
                if room.room_id == room_id:
                    if updated_room.name:
                        room.name = updated_room.name
                    if updated_room.description:
                        room.description = updated_room.description
                    if updated_room.price:
                        room.price = updated_room.price
                    if updated_room.beds:
                        room.beds = updated_room.beds
                    return "Room updated"

    raise HTTPException(
        status_code=404,
        detail=f"Hotel or room with the provided ids does not exist"
    )
