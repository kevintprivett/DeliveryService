from PIL import Image, ImageDraw
from typing import List

import CoordinateService


class TourImageService:
    """ Service that accepts a truck tour and produces a 100x100 image with
    all stops and route lines shown.

    Instance Methods:
    draw_tour(tour: List[str]):
        Takes a tour as an ordered list of addresses, creates an image of the
        addresses and route lines, and saves the image file to the local
        directory.

    """

    file_number = 0

    @staticmethod
    def draw_tour(tour: List[str], count=None, miles=None):
        """ Takes a tour and generates an image file of this tour

        Args:
            tour: list of strings representing an ordered route of addresses
            that represents a trucks route.
            watermark: optional string that appears in bottom right corner

        Returns:
            None
        """
        SIZE = (400, 400)
        CIRCLE_COLOR = (255, 0, 0)
        HOME_COLOR = (0, 255, 0)
        CIRCLE_RADIUS = 3
        LINE_COLOR = (255, 0, 0)
        LINE_WIDTH = 2
        MARGIN = 50
        COUNT_ANCHOR = (SIZE[0] - MARGIN // 2, SIZE[1] - MARGIN // 2 - 30)
        MILES_ANCHOR = (SIZE[0] - MARGIN // 2, SIZE[1] - MARGIN // 2)
        TEXT_COLOR = (255, 0, 0)
        FONT_SIZE = 30

        file_number_string = "{:04d}".format(TourImageService.file_number)

        TourImageService.file_number += 1

        coordinate_service = CoordinateService.CoordinateService()

        image = Image.new("RGB", SIZE)
        image_draw = ImageDraw.Draw(image)

        latlong_normalized = coordinate_service.get_normalized_lat_long(tour[0])

        x1_image = MARGIN + (SIZE[0] - 2 * MARGIN) * latlong_normalized[1]
        y1_image = MARGIN + (SIZE[1] - 2 * MARGIN) * latlong_normalized[0]

        image_draw.circle((x1_image, y1_image),
                          CIRCLE_RADIUS,
                          fill=CIRCLE_COLOR)

        for i in range(1, len(tour)):
            latlong_normalized = coordinate_service.get_normalized_lat_long(tour[i])

            x2_image = MARGIN + (SIZE[0] - 2 * MARGIN) * latlong_normalized[1]
            y2_image = MARGIN + (SIZE[1] - 2 * MARGIN) * latlong_normalized[0]

            image_draw.circle((x2_image, y2_image),
                              CIRCLE_RADIUS,
                              fill=CIRCLE_COLOR)

            image_draw.line([(x1_image, y1_image), (x2_image, y2_image)],
                            fill=LINE_COLOR,
                            width=LINE_WIDTH)

            x1_image = x2_image
            y1_image = y2_image

        latlong_normalized = coordinate_service.get_normalized_lat_long(tour[0])

        x1_image = MARGIN + (SIZE[0] - 2 * MARGIN) * latlong_normalized[1]
        y1_image = MARGIN + (SIZE[1] - 2 * MARGIN) * latlong_normalized[0]

        image_draw.circle((x1_image, y1_image), CIRCLE_RADIUS, fill=HOME_COLOR)

        if count:
            image_draw.text(COUNT_ANCHOR, count, fill=TEXT_COLOR, anchor="rs",
                            font_size=FONT_SIZE)

        if miles:
            image_draw.text(MILES_ANCHOR, miles, fill=TEXT_COLOR, anchor="rs",
                            font_size=FONT_SIZE)

        image.save(f"test{file_number_string}.png", "PNG")
