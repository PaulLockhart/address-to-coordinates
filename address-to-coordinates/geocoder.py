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
        county = "Could not find county"
        state = "Could not find state"
        for component in response_dict[0]['address_components']:
            if "locality" in component['types']:
                county = component["short_name"]
            if "administrative_area_level_1" in component['types']:
                state = component["short_name"]

        return (county, state, response_dict[0]["geometry"]["location"]["lat"], response_dict[0]["geometry"]["location"]["lng"])