from PyQt5.QtCore import QSettings
import json

class LocalStorageService:
    def __init__(self, organization_name, application_name):
        self.settings = QSettings(organization_name, application_name)

    def setItem(self, key, value):
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        self.settings.setValue(key, value)

    def getItem(self, key, default=None):
        value = self.settings.value(key, default)
        if isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return value

    def removeItem(self, key):
        self.settings.remove(key)

    def clear(self):
        self.settings.clear()

    def keys(self):
        return self.settings.allKeys()