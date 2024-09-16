
from app.core.expenses.api.expenses_api import ExpensesApi
from app.core.expenses.resources.save_expense_resource import SaveExpenseResource
from app.core.expenses.responses.single_expense_response import SingleExpenseResponse


class CreateExpenseUseCase:
    def create_expense(self, save_expense_resource: SaveExpenseResource) -> SingleExpenseResponse:
        try:
            resource = ExpensesApi.create_expense(save_expense_resource)

            print('Expense created:', resource)

            return SingleExpenseResponse(
                expense=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return SingleExpenseResponse(
                alert_error_message='Something was wrong',
            )