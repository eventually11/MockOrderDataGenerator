# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:56:05 2024

@author: Administrator

This unit test suite verifies the functionality of the MockDFGenerator class.
 It ensures that the the JSON 
 and CSV export functions create the appropriate output files.
"""
import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
parent_directory2 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../MockOrderDataGenerator/main'))
parent_directory3 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../MockOrderDataStructured/main'))
sys.path.insert(0, parent_directory)
sys.path.insert(0, parent_directory2)
sys.path.insert(0, parent_directory3)
import unittest
from mock_df_generator import MockDFGenerator  


class TestMockDFGenerator(unittest.TestCase):
    def setUp(self):
        # Create an instance of the MockDFGenerator
        self.generator = MockDFGenerator()

    def test_save_to_json(self):
        # Generate a small set of orders
        df_orders = self.generator.generate_orders(5)

        # Save to JSON
        json_file = "test_orders.json"
        self.generator.save_to_json(df_orders, json_file)

        # Check if the file was created
        self.assertTrue(os.path.isfile(json_file), f"JSON file '{json_file}' was not created.")

        # Clean up
        if os.path.isfile(json_file):
            os.remove(json_file)

    def test_save_to_csv(self):
        # Generate a small set of orders
        df_orders = self.generator.generate_orders(5)

        # Save to CSV
        csv_file = "test_orders.csv"
        self.generator.save_to_csv(df_orders, csv_file)

        # Check if the file was created
        self.assertTrue(os.path.isfile(csv_file), f"CSV file '{csv_file}' was not created.")

        # Clean up
        if os.path.isfile(csv_file):
            os.remove(csv_file)

if __name__ == '__main__':
    unittest.main()
