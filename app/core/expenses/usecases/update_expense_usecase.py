from app.core.expenses.api.expenses_api import ExpensesApi
from app.core.expenses.resources.save_expense_resource import SaveExpenseResource
from app.core.expenses.responses.single_expense_response import SingleExpenseResponse


class UpdateExpenseUseCase:
    def update_expense(self, expense_id: int, save_expense_resource: SaveExpenseResource) -> SingleExpenseResponse:
        try:
            resource = ExpensesApi.update_expense(expense_id, save_expense_resource)

            print('Expense updated:', resource)

            return SingleExpenseResponse(
                expense=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return SingleExpenseResponse(
                alert_error_message='Something was wrong',
            )