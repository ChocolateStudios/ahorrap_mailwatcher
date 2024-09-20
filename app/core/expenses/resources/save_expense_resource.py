from datetime import datetime

from app.core._shared.resources.base_resource import BaseResource

class SaveExpenseResource(BaseResource):
    description: str
    amount: float
    date_time: datetime