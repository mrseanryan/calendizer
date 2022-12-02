from typing import List
from parameterized import parameterized
import unittest

from image_size import ImageSize

import service_auto_dpi_calculator


class TestServiceAutoDpiCalculator(unittest.TestCase):

    def get_image_sizes_config() -> List[ImageSize]:
        return [
            ImageSize(100, 50, 666, 10, 20),
            ImageSize(200, 50, 1, 11, 21),
            ImageSize(300, 50, 2, 33, 22),
            ImageSize(49, 90, 3, 10, 20),
            ImageSize(50, 100, 777, 10, 20),
            ImageSize(55, 110, 5, 10, 20),
            ImageSize(55, 140, 888, 10, 20),
            ImageSize(50, 200, 6, 11, 21),
            ImageSize(50, 300, 7, 33, 22),
        ]

    @ parameterized.expand([
        (95, 49, 666, 10, 20),
        (95, 55, 666, 10, 20),
        (105, 55, 666, 10, 20),
        (100, 50, 666, 10, 20),
        (149, 51, 666, 10, 20),
        (50, 105, 777, 10, 20),
        (50, 100, 777, 10, 20),
        (50, 149, 888, 10, 20),
        (51, 105, 777, 10, 20)
    ])
    def test_selects_expected_dpi_from_image_size(self, width, height, expected_dpi, expected_bottom_margin, expected_right_margin):
        # Arrange
        # Act
        dpi_and_margins = service_auto_dpi_calculator.calculate_dpi_and_margins_from_image_size(
            width, height, False, TestServiceAutoDpiCalculator.get_image_sizes_config)

        # Assert
        self.assertEqual(expected_dpi, dpi_and_margins.dpi)
        self.assertEqual(expected_bottom_margin, dpi_and_margins.bottom_margin)
        self.assertEqual(expected_right_margin, dpi_and_margins.right_margin)
