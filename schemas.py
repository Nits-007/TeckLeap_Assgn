from pydantic import BaseModel, EmailStr

VALID_STATUSES = {"applied", "interview", "selected", "rejected"}

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    skill: str
    status: str

class CandidateUpdateStatus(BaseModel):
    status: str

class CandidateResponse(BaseModel):
    id: int
    name: str
    email: str
    skill: str
    status: str

    class Config:
        orm_mode = True