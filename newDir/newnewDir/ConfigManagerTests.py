import ast
import os
import unittest

from newDir.newnewDir.ConfigManager import ConfigManager


class ConfigManagerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Runs once for this class"""

        cwd = os.getcwd()
        print('!!!!!')
        print(cwd)
        print('!!!!')
        print("Testing ConfigManager")

    def setUp(self):
        """Runs before every test case"""

        self.configManager = ConfigManager()
        self.configManager.read("../../foldertest/application.config")

    def tearDown(self):
        """Runs after every test case"""

        self.configManager = None

    def test_if_config_file_has_content(self):
        self.assertNotEqual(len(self.configManager._dictionary), 0, "Config file content could not be loaded")

    def test_if_value_is_returned_for_an_existing_property(self):
        self.assertEqual(self.configManager.get_property_value("log", "log_file_name"), "application.log")

    def test_if_None_is_returned_for_a_non_existing_property(self):
        self.assertEqual(self.configManager.get_property_value("log", "non_existing_key"), None)

    def test_if_None_is_returned_for_a_non_existing_section(self):
        self.assertEqual(self.configManager.get_property_value("non_existing_section", "log_file_name"), None)

    def test_if_None_is_returned_for_a_non_existing_section_and_property(self):
        self.assertEqual(self.configManager.get_property_value("non_existing_section", "non_existing_key"), None)

    def test_if_list_is_returned_for_a_property(self):
        to_email_ids = ast.literal_eval(self.configManager.get_property_value('emails', 'to.email.ids.list'))
        to_cc_email_ids = ast.literal_eval(
            self.configManager.get_property_value('emails', 'to.cc.email.ids.list'))  # CC Email Ids

        self.assertEqual(len(to_email_ids), 2)
        self.assertEqual(len(to_cc_email_ids), 3)


# Detect and Run all test cases
suite = unittest.TestLoader().loadTestsFromTestCase(ConfigManagerTests)
unittest.TextTestRunner(verbosity=2).run(suite)