"""Manager for an application config file

    Reads a config file, stores in a dictionary of dictionary and serves request
"""
from configparser import ConfigParser


class ConfigManager():
    """Reads a config file, stores in a dictionary of dictionary and serves request"""

    def __init__(self):
        self._dictionary = {}

    def read(self, file_name):
        """Reads the config file fileName and stores in a dictionary"""

        config = ConfigParser()
        config.read(file_name)

        for section in config.sections():
            self._dictionary[section] = {}
            for option in config.options(section):
                self._dictionary[section][option] = config.get(section, option)

    def get_property_value(self, section, property_key):
        """Returns a property value if present, None otherwise"""

        property_value = None
        if (section in self._dictionary and property_key in self._dictionary[section]):
            property_value = self._dictionary[section][property_key]
        return property_value
