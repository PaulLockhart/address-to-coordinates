# address-to-coordinates
Searches for a location and converts it to coordinates using the Google Maps places/geocoding API

# Requirements
* Python 3.8 or higher
* a [Google Maps Api key](https://developers.google.com/maps/documentation/embed/get-api-key)

# First time setup
### Create a config.ini file
* Create a copy of the example config file named config.ini
  * `$ cp config.example.ini config.ini`
* Replace the line \*INSERT API KEY HERE\* with your actual API key
  * `$ sed -i 's/\\\*INSERT API KEY HERE\\\*/*actual_api_key*/g' config.ini`
### Install Dependencies
* If desired, initialize a virtualenv for the file
  * `$ python3 -m venv env`
* install the requirements from requirements.txt
  * `$ pip install -r requirements.txt`

After these steps, you should be good to go!

# Usage

    usage: address-to-coordinates.py [-h] [-f FILENAME] [-s] [location]
    
    Convert addresses/named locations into coordinates.
    
    positional arguments:
      location              Single address or description (business name) of the desired location.
    
    optional arguments:
      -h, --help            show this help message and exit
      -f FILENAME, -file FILENAME, -filename FILENAME
                            Relative file path to your input csv file (if you want to use one)
      -s, --skip-check      Flag for whether to validate inputs and convert location strings to addresses. If you're
                            confident your inputs are all only valid you can skip the validation and save time/api calls

### To run the program after setup:
* To get the coordinates for a single location, type `$ python3 address-to-coordinates.py location_to_check`
* If you wish to supply a file, instead type `$ python3 address-to-coordinates.py -f your_input_file.csv`
	* Your input file should be a newline-delimited list of location strings (either valid addresses, or locations to search for)
	* The first line of the CSV should have a name for the column, such as Addresses
	* an example input CSV can be found in `address-to-coordinates/docs`
