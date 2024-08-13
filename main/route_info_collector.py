# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:23:55 2024

@author: Administrator

Description:
This script searches for specific places (restaurants and schools) around a given location
using the OpenStreetMap API. It then calculates the driving distance and duration from the 
starting location to each of these places using the OSRM API. The results are combined into 
a DataFrame that includes the name, coordinates, distance, and travel time for each place.

Usage:
- Set the latitude and longitude of the starting location.
- Specify the search radius and the types of places to search for.
- The script outputs the search results along with the calculated route information.
"""

from open_street_map_api import OpenStreetMapAPI
from osrm_route_calculator import OSRMRouteCalculator
import pandas as pd

class RouteInfoCollector:
    def __init__(self, queries, latitude, longitude, radius):
        self.queries = queries
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.df_combined = None
        self.df_route_info = None

    def search_places(self):
        # Initialize OpenStreetMapAPI and search for places
        osm_api = OpenStreetMapAPI()
        self.df_combined = osm_api.search_and_combine_places(self.queries, self.latitude, self.longitude, self.radius)

    def calculate_routes(self):
        if self.df_combined is not None and not self.df_combined.empty:
            print("Combined results for restaurant and school:")
            print(self.df_combined)

            # Create a list to hold the distance and duration information
            route_info_list = []

            # Iterate over each row in the combined DataFrame
            for index, row in self.df_combined.iterrows():
                # Extract the latitude and longitude for the current place
                dest_lat = row['latitude']
                dest_lng = row['longitude']

                # Use OSRMRouteCalculator to calculate distance and duration
                route_calculator = OSRMRouteCalculator(self.latitude, self.longitude, dest_lat, dest_lng)
                distance, duration = route_calculator.get_route_info()

                # Append the route info to the list
                route_info_list.append({
                    'name': row['name'],
                    'latitude': dest_lat,
                    'longitude': dest_lng,
                    'distance_km': distance,
                    'duration_min': duration
                })

            # Convert the list of dictionaries to a new DataFrame
            self.df_route_info = pd.DataFrame(route_info_list)

            print("\nRoute Information DataFrame:")
            print(self.df_route_info)

        else:
            print("No places found")

    def get_route_info(self):
        return self.df_route_info

# Usage example
if __name__ == "__main__":
    # Parameters for the search
    queries = ["restaurant", "school"]
    latitude = -12.4634  # Latitude of Darwin
    longitude = 130.8456  # Longitude of Darwin
    radius = 1  # Search radius in degrees 

    # Create an instance of the RouteInfoCollector
    collector = RouteInfoCollector(queries, latitude, longitude, radius)

    # Perform the search and calculate routes
    collector.search_places()
    collector.calculate_routes()

    # Retrieve the final DataFrame with route information
    df_route_info = collector.get_route_info()

