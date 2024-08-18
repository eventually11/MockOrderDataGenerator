# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 00:24:36 2024

@author: Administrator
"""
import requests
import pandas as pd

class OpenStreetMapAPI:
    """
    A class to interact with OpenStreetMap Nominatim API to search for amenities such as restaurants
    around a specified location and convert the results to a Pandas DataFrame.

    Attributes
    ----------
    base_url : str
        The base URL for the Nominatim API.

    Methods
    -------
    get_places(query, lat, lon, radius)
        Searches for places based on the query and location details.
    
    convert_to_dataframe(places)
        Converts the search results to a Pandas DataFrame.
    """
    
    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search"

    def get_places(self, query, lat, lon, radius):
        """
        Searches for places based on the query and location details.

        Parameters
        ----------
        query : str
            The search query, e.g., 'restaurant'.
        lat : float
            Latitude of the center point for the search.
        lon : float
            Longitude of the center point for the search.
        radius : float
            The radius for the search in degrees (approximate).

        Returns
        -------
        list
            A list of places matching the query.
        """
        params = {
            'q': query,
            'format': 'json',
            'limit': 50,
            'extratags': 1,
            'addressdetails': 1,
            'viewbox': f"{lon-radius},{lat-radius},{lon+radius},{lat+radius}",
            'bounded': 1
        }
        
        headers = {
            'User-Agent': 'YourAppName/1.0 '  # Customize this with your app name and email
        }
        
        response = requests.get(self.base_url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None

    def convert_to_dataframe(self, places):
        """
        Converts the search results to a Pandas DataFrame.

        Parameters
        ----------
        places : list
            A list of places returned by the get_places method.

        Returns
        -------
        DataFrame
            A Pandas DataFrame containing the place details.
        """
        rows = []
        for place in places:
            row = {
                'name': place.get('display_name', 'N/A'),
                'latitude': place.get('lat', 'N/A'),
                'longitude': place.get('lon', 'N/A'),
                'type': place.get('type', 'N/A'),
                'address': place.get('address', {}).get('road', 'N/A')
            }
            rows.append(row)
        
        df = pd.DataFrame(rows)
        return df

    def search_and_combine_places(self, queries, lat, lon, radius):
        """
        Searches for multiple query types and combines the results into a single DataFrame.

        Parameters
        ----------
        queries : list
            A list of search queries, e.g., ['restaurant', 'school'].
        lat : float
            Latitude of the center point for the search.
        lon : float
            Longitude of the center point for the search.
        radius : float
            The radius for the search in degrees (approximate).

        Returns
        -------
        DataFrame
            A Pandas DataFrame containing the combined results of all search queries.
        """
        all_places = []

        for query in queries:
            places = self.get_places(query, lat, lon, radius)
            if places:
                df_places = self.convert_to_dataframe(places)
                all_places.append(df_places)
            else:
                print(f"Failed to retrieve {query} places")

        if all_places:
            df_combined = pd.concat(all_places, ignore_index=True)
            return df_combined
        else:
            print("No places found")
            return pd.DataFrame()  # Return an empty DataFrame if no places are found

# Example usage
if __name__ == "__main__":
    # Search parameters
    queries = ["restaurant", "school"]
    latitude = -12.4634  # Latitude of Darwin
    longitude = 130.8456  # Longitude of Darwin
    radius = 1  # Search radius in degrees 

    osm_api = OpenStreetMapAPI()
    df_combined = osm_api.search_and_combine_places(queries, latitude, longitude, radius)

    if not df_combined.empty:
        print("Combined results for restaurant and school:")
        print(df_combined)
    else:
        print("No places found")
