# from pydantic import BaseModel
# import requests
# from requests.exceptions import RequestException
# from typing import Dict, Any, Optional, Union
# from app.configs.settings import settings

# class HTTPClient:
#     def __init__(self):
#         self.base_url = f'{settings.API_URL}/api/v1'
#         self.session = requests.Session()
#         self.session.headers.update({
#             "Content-Type": "application/json",
#             "Accept": "application/json"
#         })

#     def set_auth_token(self, token: str):
#         self.session.headers["Authorization"] = f"Bearer {token}"

#     def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
#         try:
#             response.raise_for_status()
#             return response.json()
#         except RequestException as e:
#             print(e)
#             raise APIError(str(e), response.status_code)

#     def _prepare_data(self, data: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
#         if isinstance(data, BaseModel):
#             return data.model_dump()
#         return data

        
#     def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
#         url = f"{self.base_url}/{endpoint}"
#         try:
#             response = self.session.get(url, params=params)
#             return self._handle_response(response)
#         except RequestException as e:
#             raise APIError(f"GET request failed: {str(e)}")
        
#     def post(self, endpoint: str, data: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
#         url = f"{self.base_url}/{endpoint}"
#         try:
#             prepared_data = self._prepare_data(data)
#             response = self.session.post(url, json=prepared_data)
#             return self._handle_response(response)
#         except RequestException as e:
#             raise APIError(f"POST request failed: {str(e)}")

#     def put(self, endpoint: str, data: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
#         url = f"{self.base_url}/{endpoint}"
#         try:
#             prepared_data = self._prepare_data(data)
#             response = self.session.put(url, json=prepared_data)
#             return self._handle_response(response)
#         except RequestException as e:
#             raise APIError(f"PUT request failed: {str(e)}")

#     def delete(self, endpoint: str) -> Dict[str, Any]:
#         url = f"{self.base_url}/{endpoint}"
#         try:
#             response = self.session.delete(url)
#             return self._handle_response(response)
#         except RequestException as e:
#             raise APIError(f"DELETE request failed: {str(e)}")
        

# class APIError(Exception):
#     def __init__(self, message: str, status_code: Optional[int] = None):
#         self.message = message
#         self.status_code = status_code
#         super().__init__(self.message)


# http_client = HTTPClient()




import aiohttp
from aiohttp import ClientResponseError
from pydantic import BaseModel
from typing import Dict, Any, Optional, Union
from app.configs.settings import settings

class HTTPClient:
    def __init__(self):
        self.base_url = f'{settings.API_URL}/api/v1'
        self.session = None
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    def set_auth_token(self, token: str):
        self.headers["Authorization"] = f"Bearer {token}"

    async def _handle_response(self, response: aiohttp.ClientResponse) -> Dict[str, Any]:
        try:
            response.raise_for_status()
            return await response.json()
        except ClientResponseError as e:
            print(e)
            raise APIError(str(e), e.status)

    def _prepare_data(self, data: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
        if isinstance(data, BaseModel):
            return data.model_dump()
        return data

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        async with self.session.get(url, params=params) as response:
            return await self._handle_response(response)

    async def post(self, endpoint: str, data: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        prepared_data = self._prepare_data(data)
        async with self.session.post(url, json=prepared_data) as response:
            return await self._handle_response(response)

    async def put(self, endpoint: str, data: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        prepared_data = self._prepare_data(data)
        async with self.session.put(url, json=prepared_data) as response:
            return await self._handle_response(response)

    async def delete(self, endpoint: str) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        async with self.session.delete(url) as response:
            return await self._handle_response(response)

class APIError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

http_client = HTTPClient()