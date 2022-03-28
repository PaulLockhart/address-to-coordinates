import configparser
from urllib import response
import googlemaps

class PlaceFinder:
    def __init__(self, key) -> None:
        self.gmaps = googlemaps.Client(key=key)

    def find_places(self, place_strings):
        addresses = []
        for place_string in place_strings:
            addresses.append(self.parse_response(self.gmaps.find_place(place_string, 'textquery', fields=["formatted_address"]), place_string))
        return addresses # this will probably be a result dict, not raw addresses

    def parse_response(self, response_dict, place_string):
        status = response_dict['status']
        if status != "OK":
            raise ValueError("Error converting " + place_string + " to full address: " + status)
        return response_dict['candidates'][0]['formatted_address']