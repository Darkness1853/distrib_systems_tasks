from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Profile')

profiles = []
next_id = 1

class ProfileCreate(BaseModel):
    name: str
    email: str
    phone: str

class Profile(BaseModel):
    id: int
    name: str
    email: str
    phone: str

@app.get("/api/profiles/")
def get_profiles():
    return profiles

@app.post("/api/profiles/")
def create_profile(profile_data: ProfileCreate):
    global next_id
    new_profile = Profile(
        id=next_id,
        name=profile_data.name,
        email=profile_data.email,
        phone=profile_data.phone
    )
    profiles.append(new_profile)
    next_id = next_id + 1
    return new_profile