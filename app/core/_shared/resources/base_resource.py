import re
from pydantic import BaseModel

class BaseResource(BaseModel):
    class Config:
        alias_generator = lambda string: re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), string)
        allow_population_by_field_name = True