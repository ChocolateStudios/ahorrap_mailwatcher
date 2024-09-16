from pydantic import BaseModel
import datetime

class SaveExpenseResource(BaseModel):
    description: str
    amount: str
    datetime: datetime

    class Config:
        extra = 'forbid'