from app.core.users.resources.user_resource import UserResource


class AuthenticationUserResponse:
    def __init__(self, 
                 authenticated_user: UserResource | None = None,
                 success: bool = False, 
                 username_error_message: str = '',
                 password_error_message: str = '',
                 alert_error_message: str = '', 
                 ):
        
        self.authenticated_user = authenticated_user
        self.success = success
        self.username_error_message = username_error_message
        self.password_error_message = password_error_message
        self.alert_error_message = alert_error_message