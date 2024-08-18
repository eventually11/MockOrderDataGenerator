# Overview

This repository contains scripts and tools for generating and processing test data, particularly focusing on geographical data and route calculations. It includes utilities for searching locations using the OpenStreetMap API and calculating distances and durations using the OSRM API.
Features

    OpenStreetMap API Integration: Search for places (e.g., restaurants, schools) around a specified location.
    OSRM Route Calculations: Compute driving distances and travel times between locations.
    Data Handling: Combine and process location data into Pandas DataFrames for further analysis.

## Installation

To get started, clone the repository, navigate to the project directory, and install the package:

bash

    git clone https://github.com/eventually11/MockOrderDataGenerator.git
    cd MockOrderDataGenerator
    pip install .

    cd ..


    git clone https://github.com/eventually11/MockOrderDataStructured.git
    cd MockOrderDataStructured
    pip install .

    
# Outputs
CSV and Json files:
        df_orders = collector.collect_order_data(...)
        df_orders.to_csv('output/orders.csv', index=False)
        df_orders.to_json('output/orders.json', orient='records', lines=True)

# Usage

Install Dependencies: Ensure all required Python packages are installed.

bash

    pip install requests pandas

Run Scripts: Use the provided scripts to generate and process test data.


bash

    python script_name.py

Testing: The repository includes unit tests to verify functionality. Run the tests with:



bash

    python -m unittest discover


# Importing the Package

    import MockOrderDataGenerator
    import MockOrderDataGenerator.route_info_collector
    
    collector = MockOrderDataGenerator.route_info_collector.RouteInfoCollector()
    routes = collector.collect_route_info(...)


# Run
To run the run_saas_partner_order_generator.py script, which uses the configuration file and generates test data, use the following command:
    python run_saas_partner_order_generator.py

# Configuration
The script uses a config.yaml file to control the data generation process. Here is an example configuration file:
    config.yaml
    
    Number of orders to generate （hundred）
    num_orders: 10
