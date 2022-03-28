import configparser
import argparse
import csv
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
    
    if args.filename:
        write_coordinates_to_file(coordinates, args.filename)
    else:
        print(coordinates[0])

    return 0

def get_key_from_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['googlemaps']['api_key']

def parse_args():
    parser = argparse.ArgumentParser(description='Convert addresses/named locations into coordinates.')
    parser.add_argument('location', nargs='?', help="Single address or description (business name) of the desired location.")
    parser.add_argument('-f', '-file', '-filename', dest='filename', help='Relative file path to your input csv file (if you want to use one)')
    parser.add_argument('-s', '--skip-check', required=False, dest='skip_check', action="store_true", help="Flag for whether to validate inputs and convert location strings to addresses. If you're confident your inputs are all only valid you can skip the validation and save time/api calls")
    args = parser.parse_args()

    if args.filename and args.location:
        raise ValueError("Can't use filename flag AND manually input an individual location")
    
    return args

def load_locations_from_file(filename):
    res = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=",")
        line_number = 0
        for row in reader:
            if line_number != 0:
                res.append(row[0])
            line_number += 1
    return res

def write_coordinates_to_file(coordinates, filename):
    with open(filename, 'r') as input_file, \
        open(filename[:-4] + "_results.csv", 'w') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        line_number = 0
        for row in reader:
            if line_number == 0:
                row.append('Locality')
                row.append('State')
                row.append('Latitude')
                row.append('Longitude')
            else:
                row.append(coordinates[line_number - 1][0])
                row.append(coordinates[line_number - 1][1])
                row.append(coordinates[line_number - 1][2])
                row.append(coordinates[line_number - 1][3])

            writer.writerow(row)
            line_number += 1

            

if __name__ == "__main__":
    main()