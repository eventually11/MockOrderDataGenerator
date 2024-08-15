# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:43:48 2024

@author: Administrator
"""
import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
parent_directory2 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataGenerator/main'))
parent_directory3 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataStructured/main'))
sys.path.insert(0, parent_directory)
sys.path.insert(0, parent_directory2)
sys.path.insert(0, parent_directory3)

from saas_task_data_structure import SaasTaskDataStructure

from hypothesis import given
import pandas as pd


class MockDFGenerator:
    def __init__(self):
        # Create an instance of SaasPartnerOrderDataStructure
        self.order_data_structure = SaasTaskDataStructure()
        # Extract the address pool from the instance
        self.address_pool = self.order_data_structure.address_pool
    def collect_order_data(self, order_data):
        """
        Collects generated order data into a DataFrame.

        Parameters
        ----------
        order_data : dict
            A dictionary containing the generated order data.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the generated orders.
        """
        return pd.DataFrame([order_data])
    
    def generate_orders(self, num_orders):
        """
        Generates a specified number of orders and returns them as a Pandas DataFrame.

        Parameters
        ----------
        num_orders : int
            The number of orders to generate.

        Returns
        -------
        DataFrame
            A Pandas DataFrame containing the generated orders.
        """
        orders = []

        @given(self.order_data_structure.saas_task_data(self.address_pool))
        def collect_order(order):
            orders.append(order)

        for _ in range(num_orders):
            collect_order()

        df = pd.DataFrame(orders)
        return df

    def save_to_json(self, df, file_name):
        """
        Saves the DataFrame to a JSON file.

        Parameters
        ----------
        df : pandas.DataFrame
            The DataFrame containing the orders.
        file_name : str
            The name of the JSON file to save.
        """
        df.to_json(file_name, orient='records', lines=True)
        print(f"Data saved to {file_name} (JSON format)")

    def save_to_csv(self, df, file_name):
        """
        Saves the DataFrame to a CSV file.

        Parameters
        ----------
        df : pandas.DataFrame
            The DataFrame containing the orders.
        file_name : str
            The name of the CSV file to save.
        """
        df.to_csv(file_name, index=False)
        print(f"Data saved to {file_name} (CSV format)")

# Usage example
if __name__ == "__main__":

    # Create an instance of the MockDFGenerator
    generator = MockDFGenerator()

    # Generate 10 orders
    df_orders = generator.generate_orders(10)

    # Save the orders to a JSON file
    generator.save_to_json(df_orders, "mock_saas_task_data.json")

    # Save the orders to a CSV file
    generator.save_to_csv(df_orders, "mock_saas_task_data.csv")
