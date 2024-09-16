from pydantic import BaseModel

class SaveProfileResource(BaseModel):
    firstName: str
    lastName: str
    email: str

    class Config:
        extra = 'forbid'