import ast

from newDir.newnewDir.ConfigManager import ConfigManager


class LocalTest:
    def __init__(self):
        self.configReader = ConfigManager()

    def my_function(self):
        self.configReader.read("foldertest/application.config")
        file_name = self.configReader.get_property_value("log", "log_file_name")
        degug_level = self.configReader.get_property_value("log", "log_level_debug")
        ftp_value = self.configReader.get_property_value("ftp", "ftp_host")
        to_cc_email_is = ast.literal_eval(
            self.configReader.get_property_value('emails', 'to.cc.email.ids.list'))
        print(file_name, degug_level, ftp_value, to_cc_email_is)
        print(len(to_cc_email_is))
        for a in to_cc_email_is:
            print(a)


def xyz():
    test_instance = LocalTest()
    test_instance.my_function()
