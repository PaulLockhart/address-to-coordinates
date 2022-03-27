import googlemaps
import configparser
from datetime import datetime

class Geocoder:
    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)

    def encode(self, address, region=None, components=None):
        return self.gmaps.geocode(address)