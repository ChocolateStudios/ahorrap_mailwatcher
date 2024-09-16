from app.core.profiles.api.profiles_api import ProfilesApi
from app.core.profiles.responses.profile_response import ProfileResponse


class DeleteProfileUseCase:
    def delete_profile(self) -> ProfileResponse:
        try:
            resource = ProfilesApi.delete_profile()

            print('Profile deleted:', resource)

            return ProfileResponse(
                profile=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return ProfileResponse(
                alert_error_message='Something was wrong',
            )