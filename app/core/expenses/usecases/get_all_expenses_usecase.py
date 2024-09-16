from app.core.expenses.api.expenses_api import ExpensesApi
from app.core.expenses.responses.expenses_response import ExpensesResponse


class GetAllExpenseUseCase:
    def get_all_expenses(self) -> ExpensesResponse:
        try:
            resource = ExpensesApi.get_all_expenses()

            print('Expense created:', resource)

            return ExpensesResponse(
                expense=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return ExpensesResponse(
                alert_error_message='Something was wrong',
            )