from app.core.profiles.resources.profile_resource import ProfileResource


class ProfileResponse:
    def __init__(self, 
                 profile: ProfileResource | None = None,
                 success: bool = False, 
                 first_name_error_message: str = '',
                 last_name_error_message: str = '',
                 email_error_message: str = '',
                 alert_error_message: str = '', 
                 ):
        
        self.profile = profile
        self.success = success
        self.first_name_error_message = first_name_error_message
        self.last_name_error_message = last_name_error_message
        self.email_error_message = email_error_message
        self.alert_error_message = alert_error_message