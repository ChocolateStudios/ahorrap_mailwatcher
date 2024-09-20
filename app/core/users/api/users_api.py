
from app.core.users.resources.authenticated_user_resource import AuthenticatedUserResource
from app.core.users.resources.save_user_resource import SaveUserResource
from app.core.users.resources.user_resource import UserResource
from app.core._shared.api.http_common import http_client


class UsersApi:
    BASE_URL: str = 'users'

    @staticmethod
    async def register_user(data: SaveUserResource) -> AuthenticatedUserResource:
        async with http_client:
            return await http_client.post(f'{UsersApi.BASE_URL}/register', data)

    @staticmethod
    async def login_user(data: SaveUserResource) -> AuthenticatedUserResource:
        async with http_client:
            return await http_client.post(f'{UsersApi.BASE_URL}/login', data)

    @staticmethod
    async def update_user_username(data: SaveUserResource) -> AuthenticatedUserResource:
        async with http_client:
            return await http_client.put(f'{UsersApi.BASE_URL}/update/username', data)

    @staticmethod
    async def update_user_password(data: SaveUserResource) -> UserResource:
        async with http_client:
            return await http_client.put(f'{UsersApi.BASE_URL}/update/password', data)

    @staticmethod
    def set_auth_token(token: str) -> bool:
        http_client.set_auth_token(token)