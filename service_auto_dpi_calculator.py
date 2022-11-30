import service_image_sizes_reader


class DpiAndMargins:
    def __init__(self, dpi, bottom_margin, right_margin) -> None:
        self.dpi = dpi
        self.bottom_margin = bottom_margin
        self.right_margin = right_margin

    def __str__(self) -> str:
        return f"dpi:{self.dpi}, bottom_margin:{self.bottom_margin}, right_margin:{self.right_margin}"


def _calculate_distance(x1, y1, x2, y2):
    return abs((x1 - x2) ^ 2) + abs((y1 - y2) ^ 2)


def calculate_dpi_and_margins_from_image_size(width, height, is_verbose) -> DpiAndMargins:
    image_sizes = service_image_sizes_reader.get_image_sizes_config()
    min_distance = 10000000
    closest_image_size = image_sizes[0]
    for i in range(0, len(image_sizes)):
        this_image_size = image_sizes[i]
        distance = _calculate_distance(
            width, height, this_image_size.width, this_image_size.height)
        if (distance < min_distance):
            min_distance = distance
            closest_image_size = this_image_size
    dpi_and_margins = DpiAndMargins(
        closest_image_size.dpi, closest_image_size.bottom_margin, closest_image_size.right_margin)
    if is_verbose:
        print(f"[{width}x{height}] -> {dpi_and_margins}")
    return dpi_and_margins
