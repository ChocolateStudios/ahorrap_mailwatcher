from app.core.users.api.users_api import UsersApi
from app.core.users.resources.save_user_resource import SaveUserResource
from app.core.users.responses.authentication_user_response import AuthenticationUserResponse
from app.core._shared.services.local_storage_service import LocalStorageService


class LoginUserUseCase:
    def __init__(self, local_storage: LocalStorageService):
        self.local_storage = local_storage

    async def login_user(self, save_user_resource: SaveUserResource) -> AuthenticationUserResponse:
        try:
            resource = await UsersApi.login_user(save_user_resource)

            if not resource or not resource['token']:
                return AuthenticationUserResponse(
                    alert_error_message='Something was wrong',
                )

            self.local_storage.setItem('token', resource['token'])

            print('User logged:', resource)

            return AuthenticationUserResponse(
                authenticated_user=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return AuthenticationUserResponse(
                alert_error_message='Invalid credentials',
            )