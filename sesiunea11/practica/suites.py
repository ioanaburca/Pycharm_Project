import unittest
import HtmlTestRunner

from Sesiuni910.practica.alerte import Alerts
from Sesiuni910.practica.context_menu import TestContextMenu


class TestSuite(unittest.TestCase):

    def test_suite(self):

        # stabilim si adaugam intr-o suita testele pe care vrem sa le rulam
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu)
        ])

        # cream un runner
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True, # vrem sa generam un singur raport cu toate testele
            report_title="Test Execution Report",
            report_name="Alerts and Context Menu Test Results"
        )

        runner.run(teste_de_rulat)