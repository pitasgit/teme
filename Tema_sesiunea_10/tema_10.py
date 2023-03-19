import unittest
import HtmlTestRunner


from tema_9 import Login
from auth import Authentication
from alerts import Alerts
from context_menu import ContextMenu
from key_press import Keyboard
from tema_10_2 import Keyboard


class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_to_run = unittest.TestSuite()

        test_to_run.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(Login))
        test_to_run.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication))
        test_to_run.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts))
        test_to_run.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu))
        test_to_run.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)
        )

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='My Report Name',
            report_title='My First Report Title'
        )

        runner.run(test_to_run)
