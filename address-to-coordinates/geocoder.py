import googlemaps

class Geocoder:
    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)

    def geocode_addresses(self, addresses):
        coordinates = []
        for address in addresses:
            coordinates.append(self.parse_response(self.gmaps.geocode(address)))
        
        return coordinates
    
    def parse_response(self, response_dict):
        return (response_dict[0]["geometry"]["location"]["lat"], response_dict[0]["geometry"]["location"]["lng"])