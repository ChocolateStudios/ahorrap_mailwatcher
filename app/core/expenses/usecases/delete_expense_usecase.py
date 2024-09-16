from app.core.expenses.api.expenses_api import ExpensesApi
from app.core.expenses.responses.single_expense_response import SingleExpenseResponse


class DeleteExpenseUseCase:
    def delete_expense(self, expense_id: int) -> SingleExpenseResponse:
        try:
            resource = ExpensesApi.delete_expense(expense_id)

            print('Expense deleted:', resource)

            return SingleExpenseResponse(
                expense=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return SingleExpenseResponse(
                alert_error_message='Something was wrong',
            )