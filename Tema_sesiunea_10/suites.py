import unittest
import HtmlTestRunner


from tema_9 import Login
from auth import Authentication
from context_menu import ContextMenu


class TestSuite(unittest.TestCase):

    # numele metodei este predefinit si NU trebuie schimbat
    def test_suite(self):
        # am creat un obiect al clasei TestSuite
        # prin obiectul creat tests_to_run vom accesa metoda addTests
        test_to_run = unittest.TestSuite()

        # metoda addTests primeste ca parametru o lista de teste care se doreste a fi executate
        test_to_run.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(Login))
        test_to_run.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication))
        test_to_run.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu)
        )

        # Facem un test runner HTML care va genera pentru noi niste rapoarte
        # Raportul este human-friendly si poate fi inteles si de catre persoane care nu au scris/cunosc codul testelor
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='My Report Name',
            report_title='My First Report Title'
        )

        runner.run(test_to_run)
