import unittest
from PIL import Image, ImageDraw
import numpy as np

import TourImageService


class TestTourImageService(unittest.TestCase):
    def test_draw_tour(self):
        SIZE = (400, 400)
        CIRCLE_COLOR = (255, 0, 0)
        CIRCLE_RADIUS = 5
        LINE_COLOR = (255, 0, 0)
        LINE_WIDTH = 2
        MARGIN = 50

        # make a simple tour and draw the image manually
        test_tour = ["4001 South 700 East", "1060 Dalton Ave S", "1330 2100 S"]
        TourImageService.TourImageService.draw_tour(test_tour)
        test_image = Image.open("test0000.png")

        answer_image = Image.new("RGB", SIZE)
        image_draw = ImageDraw.Draw(answer_image)

        latlong_normalized = (0.354527581490741, 0.752944407822478)

        x1_image = MARGIN + (SIZE[0] - 2 * MARGIN) * latlong_normalized[1]
        y1_image = MARGIN + (SIZE[1] - 2 * MARGIN) * latlong_normalized[0]

        image_draw.circle((x1_image, y1_image), CIRCLE_RADIUS, fill=CIRCLE_COLOR)

        latlong_normalized = (0.78905715751084, 0.465210942649979)

        x2_image = MARGIN + (SIZE[0] - 2 * MARGIN) * latlong_normalized[1]
        y2_image = MARGIN + (SIZE[1] - 2 * MARGIN) * latlong_normalized[0]

        image_draw.circle((x2_image, y2_image), CIRCLE_RADIUS, fill=CIRCLE_COLOR)

        image_draw.line([(x1_image, y1_image), (x2_image, y2_image)],
                        fill=LINE_COLOR, width=LINE_WIDTH)

        latlong_normalized = (0.625911784818796, 0.858036695231847)

        x3_image = MARGIN + (SIZE[0] - 2 * MARGIN) * latlong_normalized[1]
        y3_image = MARGIN + (SIZE[1] - 2 * MARGIN) * latlong_normalized[0]

        image_draw.circle((x3_image, y3_image), CIRCLE_RADIUS, fill=CIRCLE_COLOR)

        image_draw.line([(x2_image, y2_image), (x3_image, y3_image)],
                        fill=LINE_COLOR, width=LINE_WIDTH)

        test_image_array = np.array(test_image)
        answer_image_array = np.array(answer_image)

        image_compare = test_image_array.shape == answer_image_array.shape and \
                        np.all(test_image_array == answer_image_array)

        self.assertTrue(image_compare)
