from app.core.profiles.resources.profile_resource import ProfileResource
from app.core.profiles.resources.save_profile_resource import SaveProfileResource
from app.core._shared.api.http_common import http_client


class ProfilesApi:
    BASE_URL: str = 'profiles'

    @staticmethod
    def create_profile(data: SaveProfileResource) -> ProfileResource:
        return http_client.post(ProfilesApi.BASE_URL, data.dict())

    @staticmethod
    def update_profile(data: SaveProfileResource) -> ProfileResource:
        return http_client.post(ProfilesApi.BASE_URL, data.dict())

    @staticmethod
    def delete_profile() -> ProfileResource:
        return http_client.put(ProfilesApi.BASE_URL)

    @staticmethod
    def get_profile() -> ProfileResource:
        return http_client.put(ProfilesApi.BASE_URL)