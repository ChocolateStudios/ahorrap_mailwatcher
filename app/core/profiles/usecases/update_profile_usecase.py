from app.core.profiles.api.profiles_api import ProfilesApi
from app.core.profiles.resources.save_profile_resource import SaveProfileResource
from app.core.profiles.responses.profile_response import ProfileResponse


class UpdateProfileUseCase:
    def update_profile(self, save_profile_resource: SaveProfileResource) -> ProfileResponse:
        try:
            resource = ProfilesApi.update_profile(save_profile_resource)

            print('Profile updated:', resource)

            return ProfileResponse(
                profile=resource,
                success=True,
            )
        
        except Exception as error:
            print(error)

            return ProfileResponse(
                alert_error_message='Something was wrong',
            )