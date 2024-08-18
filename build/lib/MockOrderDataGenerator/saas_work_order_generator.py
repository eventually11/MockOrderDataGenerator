# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:43:48 2024

@author: Administrator
"""
import os
import sys


from MockOrderDataStructured.saas_work_order_structure import SaasWorkOrderStructure

from hypothesis import given
import pandas as pd


class MockDFGenerator:
    def __init__(self):
        # Create an instance of SaasPartnerOrderDataStructure
        self.order_data_structure = SaasWorkOrderStructure()
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

        @given(self.order_data_structure.saas_work_order(self.address_pool))
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
    generator.save_to_json(df_orders, "../../output/mock_saas_work_order.json")

    # Save the orders to a CSV file
    generator.save_to_csv(df_orders, "../../output/mock_saas_work_order.csv")
