from app.core.expenses.resources.expense_resource import ExpenseResource


class ExpensesResponse:
    def __init__(self, 
                 expenses: list[ExpenseResource] | None = None,
                 success: bool = False, 
                 alert_error_message: str = '', 
                 ):
        
        self.expenses = expenses
        self.success = success
        self.alert_error_message = alert_error_message