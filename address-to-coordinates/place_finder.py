import configparser
import googlemaps

class PlaceFinder:
    def __init__(self, key) -> None:
        self.gmaps = googlemaps.Client(key=key)

    def find_places(self, place_strings):
        addresses = []
        for place_string in place_strings:
            addresses += self.gmaps.find_place(place_string, 'textquery', ["formatted_address"])['candidates'][0]
            # TODO: Error checking, etc.
        return addresses # this will probably be a result dict, not raw addresses