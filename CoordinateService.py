import csv
from typing import Tuple


class CoordinateService:
    """ Simple service to load and hold a coordinate lookup table.  Keys for
    the dictionary are the address string, similar to the other lookup tables
    in this project.

    Constructor:
    CoordinateService():
        Constructs an instance to the coordinate service that will initiate
        the coordinate lookup map if it hasn't already been done.

    Instance Methods:
    get_normalized_lat_long(address: str):
        returns a tuple of the normalized latitude and longitude of the given
        address.  Coordinates are normalized between [0, 1].
    """
    coordinates = {}

    def __init__(self):
        # Call import process for coordinates so that it is loaded in memory
        # when first coordinate service instance is created
        if not CoordinateService.coordinates:
            CoordinateService.init_coordinates()

    def get_normalized_lat_long(self, address: str) -> Tuple[float, float]:
        """ Returns lat and long of a specific address, normalized between
            [0-1].

        Args:
            address: String of the address used to lookup coordinates

        returns:
            Tuple(float, float): (latitude, longitude) as floats between [0-1]
        """
        return_tuple = (CoordinateService.coordinates[address]['Normalized_Latitude'],
                        CoordinateService.coordinates[address]['Normalized_Longitude'])

        return return_tuple

    @staticmethod
    def init_coordinates():
        """ Load coordinate lookup table into memory from csv

        Args:
            None

        returns:
            None
        """
        with open('latlong.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                key = row["Address"]
                CoordinateService.coordinates[key] = {
                    k: float(v) for k, v in row.items() if k != "Address"
                }
