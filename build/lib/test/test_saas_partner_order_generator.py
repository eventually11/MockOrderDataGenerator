# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:35:38 2024

@author: Administrator
"""

import unittest
import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
parent_directory2 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataGenerator/main'))
parent_directory3 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataStructured/main'))
sys.path.insert(0, parent_directory)
sys.path.insert(0, parent_directory2)
sys.path.insert(0, parent_directory3)
import pandas as pd
from saas_partner_order_structure import SaasPartnerOrderDataStructure
from mock_df_generator import MockDFGenerator  # Assuming you saved your class as mock_df_generator.py

class TestMockDFGenerator(unittest.TestCase):

    def setUp(self):
        # Create an instance of the MockDFGenerator
        self.generator = MockDFGenerator()

        # Generate orders
        self.df_orders = self.generator.generate_orders(10)

        # File names for the output
        self.json_file = "test_mock_partner_order.json"
        self.csv_file = "test_mock_partner_order.csv"

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
