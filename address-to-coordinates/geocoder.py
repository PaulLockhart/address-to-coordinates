import googlemaps

class Geocoder:
    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)

    def geocode_addresses(self, addresses):
        coordinates = []
        for address in addresses:
            coordinates += self.gmaps.geocode(address)
        
        return coordinates # This will probably be a result dict, not raw coordinates