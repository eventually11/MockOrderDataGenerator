# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:50:23 2024

@author: Administrator

Description:
This script contains unit tests for the `RouteInfoCollector` class. 
The tests ensure that the output DataFrame (`df_route_info`) generated by the class 
contains the expected column names and the correct number of columns after processing.

Test Cases:
1. `test_columns_in_output`: Verifies that the `df_route_info` DataFrame has the expected column names.
2. `test_number_of_columns`: Ensures that the `df_route_info` DataFrame has exactly 5 columns.

The tests use mock data for `df_combined` to simulate the input, focusing on the correctness of the output structure 
without making actual API calls.

Usage:
- Run this script to execute the tests using Python's `unittest` framework.
- Ensure that the `RouteInfoCollector` class is correctly imported from its respective module.
"""

import os
import sys
import unittest
import pandas as pd
from MockOrderDataGenerator.route_info_collector import RouteInfoCollector  # Replace 'your_module' with the actual module name

class TestRouteInfoCollector(unittest.TestCase):
    
    def setUp(self):
        # Create a mock RouteInfoCollector instance with dummy parameters
        self.collector = RouteInfoCollector(["restaurant", "school"], -12.4634, 130.8456, 1)
        
        # Simulate data for df_combined
        data = {
            'name': ['Test Restaurant', 'Test School'],
            'latitude': [-12.4634, -12.4635],
            'longitude': [130.8456, 130.8457]
        }
        self.collector.df_combined = pd.DataFrame(data)
        
        # Call the calculate_routes method to generate df_route_info
        self.collector.calculate_routes()

    def test_columns_in_output(self):
        # Ensure df_route_info is created
        self.assertIsNotNone(self.collector.df_route_info, "df_route_info should not be None")

        # Check that the output DataFrame has the expected columns
        expected_columns = ['name', 'latitude', 'longitude', 'distance_km', 'duration_min']
        actual_columns = list(self.collector.df_route_info.columns)
        self.assertEqual(actual_columns, expected_columns, "Column names in df_route_info do not match the expected names.")

    def test_number_of_columns(self):
        # Check that the DataFrame has exactly 5 columns
        self.assertEqual(len(self.collector.df_route_info.columns), 5, "df_route_info should have exactly 5 columns.")

if __name__ == "__main__":
    unittest.main()
