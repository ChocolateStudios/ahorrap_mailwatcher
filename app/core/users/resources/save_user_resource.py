from pydantic import BaseModel

class SaveUserResource(BaseModel):
    username: str
    password: str

    class Config:
        extra = 'forbid'