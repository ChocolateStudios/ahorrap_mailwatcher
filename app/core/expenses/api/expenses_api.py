from app.core.expenses.resources.expense_resource import ExpenseResource
from app.core.expenses.resources.save_expense_resource import SaveExpenseResource
from app.core._shared.api.http_common import http_client


class ExpensesApi:
    BASE_URL: str = 'expenses'

    @staticmethod
    async def synchronize_expenses(data: list[SaveExpenseResource]) -> ExpenseResource:
        async with http_client:
            return await http_client.post(f'{ExpensesApi.BASE_URL}/sync', data)
    
    @staticmethod
    async def create_expense(data: SaveExpenseResource) -> ExpenseResource:
        async with http_client:
            return await http_client.post(ExpensesApi.BASE_URL, data)

    @staticmethod
    async def update_expense(id: int, data: SaveExpenseResource) -> ExpenseResource:
        async with http_client:
            return await http_client.put(f'{ExpensesApi.BASE_URL}/{id}', data)

    @staticmethod
    async def delete_expense(id: int) -> ExpenseResource:
        async with http_client:
            return await http_client.delete(f'{ExpensesApi.BASE_URL}/{id}')

    @staticmethod
    async def get_all_expenses() -> list[ExpenseResource]:
        async with http_client:
            return await http_client.get(ExpensesApi.BASE_URL)