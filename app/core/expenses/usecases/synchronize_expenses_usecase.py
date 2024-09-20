from datetime import datetime

import win32com.client
from app.core.expenses.api.expenses_api import ExpensesApi
from app.core.expenses.resources.save_expense_resource import SaveExpenseResource
from app.core.expenses.responses.expenses_response import ExpensesResponse


class SynchronizeExpensesUseCase:
    async def synchronize_expenses(self) -> ExpensesResponse:
        try:
            outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
            inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
            messages = inbox.Items
            now = datetime.now()

            # Filtra los mensajes
            filtered_messages = []
            for message in messages:
                message_subject = message.Subject
                message_date = message.ReceivedTime
                if message_subject == "Realizaste un consumo con tu Tarjeta de Débito BCP - Servicio de Notificaciones BCP" and message_date.month == now.month and message_date.year == now.year:
                    filtered_messages.append(message)
                    
            expenses: list[SaveExpenseResource] = []

            # Imprime los asuntos de los mensajes filtrados
            for msg in filtered_messages:
                index = msg.Body.find("Monto")
                index2 = msg.Body.find("Total del consumo")
                index3 = msg.Body.find("S/")

                if index3 != -1:
                    start_index = index3 + 3  # Skip 'S/'
                    end_index = start_index
                    while end_index < len(msg.Body) and msg.Body[end_index].isdigit() or msg.Body[end_index] == '.':
                        end_index += 1
                    expense = msg.Body[start_index:end_index]
                    expenses.append(SaveExpenseResource(
                        description='hello world',
                        amount=float(expense),
                        dateTime=msg.ReceivedTime.replace(tzinfo=None)
                    ))

            resources = await ExpensesApi.synchronize_expenses(expenses)

            print('Expenses synchronized:', resources)

            return ExpensesResponse(
                expense=resources,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return ExpensesResponse(
                alert_error_message='Something was wrong',
            )