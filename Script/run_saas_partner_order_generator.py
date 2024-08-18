# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:31:44 2024

@author: Administrator
"""

import yaml
from MockOrderDataGenerator.saas_partner_order_generator import MockDFGenerator

def load_config(config_file):
    """
    Loads the configuration from a YAML file.

    Parameters
    ----------
    config_file : str
        The path to the configuration file.

    Returns
    -------
    dict
        The loaded configuration settings.
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    # Load configuration settings
    config = load_config('../config/config.yaml')
    
    # Create an instance of MockDFGenerator
    generator = MockDFGenerator()

    # Generate orders based on the configuration
    num_orders = config.get('num_orders', 10)  # Default to 10 if not specified
    df_orders = generator.generate_orders(num_orders)

    # Save the orders to a JSON file
    generator.save_to_json(df_orders, "../output/mock_partner_order.json")

    # Save the orders to a CSV file
    generator.save_to_csv(df_orders, "../output/mock_partner_order.csv")

if __name__ == "__main__":
    main()
