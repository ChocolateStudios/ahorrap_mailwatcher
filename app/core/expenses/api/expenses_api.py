from app.core.expenses.resources.expense_resource import ExpenseResource
from app.core.expenses.resources.save_expense_resource import SaveExpenseResource
from app.core._shared.api.http_common import http_client


class ExpensesApi:
    BASE_URL: str = 'expenses'

    @staticmethod
    def create_expense(data: SaveExpenseResource) -> ExpenseResource:
        return http_client.post(ExpensesApi.BASE_URL, data)

    @staticmethod
    def update_expense(id: int, data: SaveExpenseResource) -> ExpenseResource:
        return http_client.put(f'{ExpensesApi.BASE_URL}/{id}', data)

    @staticmethod
    def delete_expense(id: int) -> ExpenseResource:
        return http_client.delete(f'{ExpensesApi.BASE_URL}/{id}')

    @staticmethod
    def get_all_expenses() -> list[ExpenseResource]:
        return http_client.get(ExpensesApi.BASE_URL)