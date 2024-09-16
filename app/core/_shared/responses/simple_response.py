class SimpleResponse:
    def __init__(self,
                 success: bool = False,
                 alert_error_message: str = '', 
                 ):
        
        self.success = success
        self.alert_error_message = alert_error_message