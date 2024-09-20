from pydantic import BaseModel

from app.core.expenses.resources.expense_resource import ExpenseResource

class SynchronizedExpensesResource(BaseModel):
    expenses: list[ExpenseResource]
    errors: list[str]