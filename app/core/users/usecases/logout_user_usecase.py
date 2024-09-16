
from app.core._shared.responses.simple_response import SimpleResponse
from app.core._shared.services.local_storage_service import LocalStorageService


class LogoutUserUseCase:
    def __init__(self, local_storage: LocalStorageService):
        self.local_storage = local_storage

    def logout_user(self) -> SimpleResponse:
        try:
            self.local_storage.removeItem('token')

            return SimpleResponse(
                success=True,
            )
                
        except Exception as error:
            print(error)

            return SimpleResponse(
                alert_error_message='Something was wrong',
            )