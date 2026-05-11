from unittest import TestCase

from temperature_checker import*

class TemperatureCheckerTest(TestCase):

    def test_that_celsius_converts_to_fahrenhit_and_returns_message(self):

        fahrenhit_converter = checkTemperature(36,'C')

        expected_temp = '96.8 F'

        expected_threshold_message = 'Heat alert'

        self.assertEqual(fahrenhit_converter,(expected_temp, expected_threshold_message))

    def test_that_fahrenhit_converts_to_celsius_and_returns_message(self):

        celsius_converter = checkTemperature(96.8, 'F')

        expected_temp = '36.0 C'


        expected_threshold_message = 'Heat alert'

        self.assertEqual(celsius_converter, (expected_temp, expected_threshold_message))

    def test_that_when_unit_is_not_provided_it_defaults_to_celcuis(self):

        
        fahrenhit_converter = checkTemperature(36,' ')

        expected_temp = '96.8 F'

        expected_threshold_message = 'Heat alert'

        self.assertEqual(fahrenhit_converter,(expected_temp, expected_threshold_message))

    def test_that_unit_is_invalid(self):

        is_invalid = checkTemperature(36,'a')

        expected_error_message = 'Invalid Unit'

        self.assertEqual(is_invalid,expected_error_message)

        
