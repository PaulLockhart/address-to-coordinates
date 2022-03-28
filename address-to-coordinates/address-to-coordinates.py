import configparser
import argparse
from fileinput import filename
from place_finder import PlaceFinder
from geocoder import Geocoder

def main():
    key = get_key_from_config()
    args = parse_args()
    place_finder = PlaceFinder(key)
    geocoder = Geocoder(key)
            
    if args.filename:
        locations = load_locations_from_file(args.filename)
    else:
        locations = [args.location]
    
    if not args.skip_check:
        addresses = place_finder.find_places(locations)
    else:
        addresses = locations
    
    coordinates = geocoder.geocode_addresses(addresses)

    print(coordinates)
    return 0
    


def get_key_from_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['googlemaps']['api_key']

def parse_args():
    parser = argparse.ArgumentParser(description='Convert addresses/named locations into coordinates.')
    parser.add_argument('location', nargs='?', help="Address or description (business name) of the desired location.")
    parser.add_argument('-f', '-file', '-filename', dest='filename', help='Relative file path to your input file.')
    parser.add_argument('-s', '--skip-check', required=False, dest='skip_check', action="store_true", help="Flag for whether to validate inputs and convert location strings to addresses. If you're confident your inputs are all only valid you can skip the validation and save time/api calls")
    args = parser.parse_args()

    if args.filename and args.location:
        # throw error
        pass
    
    return args

def load_locations_from_file(filename):
    # depends on file format here, we'll figure it out later (should be simple)
    # assume output is just an array of strings
    pass

if __name__ == "__main__":
    main()