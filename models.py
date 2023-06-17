from uuid import uuid4, UUID
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class Photo(BaseModel):
    url: str
    caption: Optional[str]

class Room(BaseModel):
    room_id: Optional[UUID] = uuid4()
    hotel_id: Optional[UUID]
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    beds: Optional[int]
    photos: Optional[List[Photo]]

class Hotel(BaseModel):
    hotel_id: Optional[UUID] = uuid4()
    name: Optional[str]
    grounds: Optional[str]
    address: Optional[str]
    city: Optional[str]
    region: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    phone: Optional[str]
    email: Optional[str]
    website: Optional[str]
    description: Optional[str]
    stars: Optional[int]
    price_range: Optional[dict]
    services: Optional[str]
    map_url: Optional[str]
    photos: Optional[List]
    rooms: Optional[List[Room]]
