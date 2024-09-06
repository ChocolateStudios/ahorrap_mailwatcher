import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        self.load_environment()

    def load_environment(self):
        env = os.getenv('APP_ENV', 'pro')
        env_file = f'.env.{env}'

        if os.path.exists(env_file):
            load_dotenv(env_file)
            
        elif os.path.exists('.env'):
            load_dotenv('.env')
            
        self.API_URL = os.getenv('API_URL')