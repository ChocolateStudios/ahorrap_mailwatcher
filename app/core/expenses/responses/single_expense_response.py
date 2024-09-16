from app.core.expenses.resources.expense_resource import ExpenseResource


class SingleExpenseResponse:
    def __init__(self, 
                 expense: ExpenseResource | None = None,
                 success: bool = False, 
                 description_error_message: str = '',
                 amount_error_message: str = '',
                 datetime_error_message: str = '',
                 alert_error_message: str = '', 
                 ):
        
        self.expense = expense
        self.success = success
        self.description_error_message = description_error_message
        self.amount_error_message = amount_error_message
        self.datetime_error_message = datetime_error_message
        self.alert_error_message = alert_error_message