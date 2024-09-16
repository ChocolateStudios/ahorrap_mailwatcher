from pydantic import BaseModel
import datetime

class ExpenseResource(BaseModel):
    id: int
    description: str
    amount: str
    datetime: datetime
    profile_id: int