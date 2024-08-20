# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:17:19 2024

@author: Administrator

This script contains unit tests for the OSRMRouteCalculator class, which is used to calculate
the driving distance and duration between two geographic coordinates using the OSRM API.

The tests cover the following scenarios:
1. A successful API response, where the distance and duration are returned correctly.
2. A failed API response (e.g., HTTP 404), where the method should return None for both distance and duration.

The test methods use the unittest framework, with the requests.get method mocked to simulate API responses.
This allows for testing the class behavior without making actual HTTP requests.

Instructions:
- Run the script directly to execute the tests. The output will indicate whether each test passed or failed.
- The print statements in the test methods provide additional information during the test execution.
"""
import os
import sys


import unittest
from unittest.mock import patch, MagicMock
from MockOrderDataGenerator.osrm_route_calculator import OSRMRouteCalculator

class TestOSRMRouteCalculator(unittest.TestCase):

    @patch('osrm_route_calculator.requests.get')
    def test_get_route_info_success(self, mock_get):
        """Test the get_route_info method with a successful API response."""
        print("Running test_get_route_info_success...")

        # Mocking a successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'routes': [{
                'distance': 5000,  # 5 km
                'duration': 600    # 10 minutes
            }]
        }
        mock_get.return_value = mock_response

        # Create an instance of the calculator
        calculator = OSRMRouteCalculator(39.9087, 116.3975, 39.9163, 116.3971)
        print(f"Created OSRMRouteCalculator instance with start ({calculator.start_lat}, {calculator.start_lng}) "
              f"and end ({calculator.end_lat}, {calculator.end_lng}) coordinates.")

        # Get the route information
        distance, duration = calculator.get_route_info()
        print(f"Mocked API returned distance: {distance} km, duration: {duration} minutes")

        # Check that the distance and duration are correctly calculated
        self.assertEqual(distance, 5.0, "Expected distance to be 5.0 km")  # Expected 5 km
        self.assertEqual(duration, 10.0, "Expected duration to be 10.0 minutes")  # Expected 10 minutes

        print("test_get_route_info_success passed.\n")

    @patch('osrm_route_calculator.requests.get')
    def test_get_route_info_failure(self, mock_get):
        """Test the get_route_info method with a failed API response."""
        print("Running test_get_route_info_failure...")

        # Mocking a failed API response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Create an instance of the calculator
        calculator = OSRMRouteCalculator(39.9087, 116.3975, 39.9163, 116.3971)
        print(f"Created OSRMRouteCalculator instance with start ({calculator.start_lat}, {calculator.start_lng}) "
              f"and end ({calculator.end_lat}, {calculator.end_lng}) coordinates.")

        # Get the route information
        distance, duration = calculator.get_route_info()
        print(f"Mocked API returned status code 404, expecting None for both distance and duration.")

        # Check that distance and duration are None
        self.assertIsNone(distance, "Expected distance to be None due to failed API call")
        self.assertIsNone(duration, "Expected duration to be None due to failed API call")

        print("test_get_route_info_failure passed.\n")

if __name__ == "__main__":
    print("Starting the test suite...\n")
    unittest.main()
    print("Test suite finished.")
