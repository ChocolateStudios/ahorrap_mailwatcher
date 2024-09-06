import requests
from requests.exceptions import RequestException
from typing import Dict, Any, Optional
from configs import settings  # Asumiendo que tienes un módulo de configuración

class HTTPClient:
    def __init__(self):
        self.base_url = settings.API_URL
        # self.timeout = settings.API_TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def set_auth_token(self, token: str):
        self.session.headers["Authorization"] = f"Bearer {token}"

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        try:
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            # Log the error here if needed
            raise APIError(str(e), response.status_code)

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            return self._handle_response(response)
        except RequestException as e:
            raise APIError(f"GET request failed: {str(e)}")

    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.post(url, json=data, timeout=self.timeout)
            return self._handle_response(response)
        except RequestException as e:
            raise APIError(f"POST request failed: {str(e)}")

    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.put(url, json=data, timeout=self.timeout)
            return self._handle_response(response)
        except RequestException as e:
            raise APIError(f"PUT request failed: {str(e)}")

    def delete(self, endpoint: str) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.delete(url, timeout=self.timeout)
            return self._handle_response(response)
        except RequestException as e:
            raise APIError(f"DELETE request failed: {str(e)}")

class APIError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


def get_http_client() -> HTTPClient:
    return HTTPClient()