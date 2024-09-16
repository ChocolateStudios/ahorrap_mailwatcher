import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        self.load_environment()
        self.set_attributes()

    def load_environment(self):
        if os.path.exists('.env'):
            load_dotenv('.env')

        env = os.getenv('APP_ENV', 'dev')
        env_file = f'.env.{env}'

        if os.path.exists(env_file):
            load_dotenv(env_file, override=True)

    def set_attributes(self):
        self.APP_ENV = os.getenv('APP_ENV')
        self.API_URL = os.getenv('API_URL')


settings = Settings()