import configparser
import googlemaps

class PlaceFinder:
    def __init__(self, key) -> None:y
        self.gmaps = googlemaps.Client(key=key)

    def find_place(self, place_string):
        return self.gmaps.find_place(place_string, 'textquery', ["formatted_address"])['candidates'][0]