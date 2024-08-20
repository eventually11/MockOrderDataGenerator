# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:47:27 2024

@author: Administrator
the tests check whether the generated data can be correctly saved to JSON and CSV formats in the specified output directory. The setup process includes creating necessary directories, and the teardown ensures that temporary test files are cleaned up after each test run.

"""

import unittest
import os
import sys
from MockOrderDataGenerator.mock_df_generator import MockDFGenerator  # Adjust the import path if needed

class TestMockDFGenerator(unittest.TestCase):

    def setUp(self):
        # Create an instance of the MockDFGenerator
        self.generator = MockDFGenerator()
        # Generate orders
        self.df_orders = self.generator.generate_orders(10)
        # Define the output directory and ensure it exists
        self.output_dir =  "../output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # File names for output
        self.json_file = os.path.join(self.output_dir, "test_mock_saas_task_data.json")
        self.csv_file = os.path.join(self.output_dir, "test_mock_saas_task_data.csv")

    def test_save_to_json(self):
        # Save the orders to a JSON file
        self.generator.save_to_json(self.df_orders, self.json_file)
        # Check if the JSON file exists
        self.assertTrue(os.path.exists(self.json_file))

    def test_save_to_csv(self):
        # Save the orders to a CSV file
        self.generator.save_to_csv(self.df_orders, self.csv_file)
        # Check if the CSV file exists
        self.assertTrue(os.path.exists(self.csv_file))

    def tearDown(self):
        # Clean up the files after tests
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

if __name__ == "__main__":
    unittest.main()
