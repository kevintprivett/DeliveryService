import unittest

import CoordinateService


class TestCoordinateService(unittest.TestCase):
    def test_init(self):
        coordinate_service = CoordinateService.CoordinateService()
        self.assertAlmostEqual(
          coordinate_service.coordinates['4001 South 700 East']['Normalized_Latitude'],
          0.354527581490741)
        self.assertAlmostEqual(
          coordinate_service.coordinates['3365 S 900 W']['Normalized_Longitude'],
          0.497687321467793)

    def test_get(self):
        coordinate_service = CoordinateService.CoordinateService()
        coordinates_1 = coordinate_service.get_normalized_lat_long('4001 South 700 East')
        coordinates_2 = coordinate_service.get_normalized_lat_long('3365 S 900 W')
        self.assertAlmostEqual(coordinates_1[0], 0.354527581490741)
        self.assertAlmostEqual(coordinates_1[1], 0.752944407822478)
        self.assertAlmostEqual(coordinates_2[0], 0.452872122179157)
        self.assertAlmostEqual(coordinates_2[1], 0.497687321467793)
