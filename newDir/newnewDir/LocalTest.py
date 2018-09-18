import ast

from newDir.newnewDir.ConfigManager import ConfigManager


class LocalTest:
    def __init__(self):
        self.configReader = ConfigManager()

    def myfunction(self):
        self.configReader.read("foldertest/application.config")
        filename = self.configReader.getPropertyValue("log", "log_file_name")
        deguglevel = self.configReader.getPropertyValue("log", "log_level_debug")
        ftp_value = self.configReader.getPropertyValue("ftp", "ftp_host")
        to_cc_email_is = ast.literal_eval(
            self.configReader.getPropertyValue('emails', 'to.cc.email.ids.list'))
        print(filename, deguglevel, ftp_value, to_cc_email_is)
        print(len(to_cc_email_is))
        for a in to_cc_email_is:
            print(a)


def xyz():
    testinstance = LocalTest()
    testinstance.myfunction()
