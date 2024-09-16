from app.core.profiles.api.profiles_api import ProfilesApi
from app.core.profiles.responses.profile_response import ProfileResponse


class GetProfileUseCase:
    def get_profile(self) -> ProfileResponse:
        try:
            resource = ProfilesApi.get_profile()

            print('Profile obtained:', resource)

            return ProfileResponse(
                profile=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return ProfileResponse(
                alert_error_message='Something was wrong',
            )