import os
import sys
# Get the full path to the current file
current_file_path = os.path.abspath(sys.argv[0])
# Determine the parent directory (one level up)
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../main'))
# Insert the parent directory into sys.path
sys.path.insert(0, parent_directory)
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from open_street_map_api import OpenStreetMapAPI

class TestOpenStreetMapAPI(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.api = OpenStreetMapAPI()
        self.query = "restaurant"
        self.latitude = -12.4634
        self.longitude = 130.8456
        self.radius = 1

    @patch('open_street_map_api.requests.get')
    def test_get_places(self, mock_get):
        """Test the get_places method."""
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"display_name": "Test Restaurant", "lat": "-12.4634", "lon": "130.8456"}
        ]
        mock_get.return_value = mock_response

        places = self.api.get_places(self.query, self.latitude, self.longitude, self.radius)
        self.assertEqual(len(places), 1)
        self.assertEqual(places[0]['display_name'], "Test Restaurant")

    def test_convert_to_dataframe(self):
        """Test the convert_to_dataframe method."""
        places = [
            {"display_name": "Test Restaurant", "lat": "-12.4634", "lon": "130.8456"},
            {"display_name": "Test School", "lat": "-12.4635", "lon": "130.8457"}
        ]
        df = self.api.convert_to_dataframe(places)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 2)
        self.assertEqual(df.iloc[0]['name'], "Test Restaurant")

    @patch('open_street_map_api.requests.get')
    def test_search_and_combine_places(self, mock_get):
        """Test the search_and_combine_places method."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"display_name": "Test Restaurant", "lat": "-12.4634", "lon": "130.8456"}
        ]
        mock_get.return_value = mock_response

        queries = ["restaurant"]
        df_combined = self.api.search_and_combine_places(queries, self.latitude, self.longitude, self.radius)
        self.assertIsInstance(df_combined, pd.DataFrame)
        self.assertEqual(df_combined.shape[0], 1)
        self.assertEqual(df_combined.iloc[0]['name'], "Test Restaurant")

if __name__ == "__main__":
    unittest.main()
