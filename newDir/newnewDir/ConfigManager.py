"""Manager for an application config file

    Reads a config file, stores in a dictionary of dictionary and serves request
"""
from configparser import SafeConfigParser


class ConfigManager():
    """Reads a config file, stores in a dictionary of dictionary and serves request"""

    def __init__(self):
        self._dictionary = {}

    def read(self, fileName):
        """Reads the config file fileName and stores in a dictionary"""

        config = SafeConfigParser()
        config.read(fileName)

        for section in config.sections():
            self._dictionary[section] = {}
            for option in config.options(section):
                self._dictionary[section][option] = config.get(section, option)

    def getPropertyValue(self, section, propertyKey):
        """Returns a property value if present, None otherwise"""

        propertyValue = None
        if (section in self._dictionary and propertyKey in self._dictionary[section]):
            propertyValue = self._dictionary[section][propertyKey]
        return propertyValue
