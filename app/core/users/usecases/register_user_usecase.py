from app.core._shared.services.local_storage_service import LocalStorageService
from app.core.users.api.users_api import UsersApi
from app.core.users.resources.save_user_resource import SaveUserResource
from app.core.users.responses.authentication_user_response import AuthenticationUserResponse


class RegisterUserUseCase:
    def __init__(self, local_storage: LocalStorageService):
        self.local_storage = local_storage

    async def register_user(self, save_user_resource: SaveUserResource) -> AuthenticationUserResponse:
        try:
            resource = await UsersApi.register_user(save_user_resource)

            if not resource or not resource['token']:
                return AuthenticationUserResponse(
                    alert_error_message='Something was wrong',
                )

            self.local_storage.setItem('token', resource['token'])

            print('User registered:', resource)

            return AuthenticationUserResponse(
                authenticated_user=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            error_message=''
            _alert_error_message='TODO: identificar posibles errores'

            if error_message.includes('User already exists with username'):
                _alert_error_message='Ya existe un usuario registrado con este correo'

            return AuthenticationUserResponse(
                alert_error_message=_alert_error_message,
            )