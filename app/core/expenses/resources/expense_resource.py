from pydantic import BaseModel
from datetime import datetime

class ExpenseResource(BaseModel):
    id: int
    description: str
    amount: float
    date_time: datetime
    profile_id: int