from typing import List
import util_file
from image_size import ImageSize


def get_image_sizes_config() -> List[ImageSize]:
    lines = util_file.read_lines_from_file("image_sizes.csv.config")
    image_sizes = []
    for line in lines:
        if line.startswith("#"):
            continue
        parts = line.split(",")
        dimensions = parts[0].split("x")
        image_sizes.append(ImageSize(int(dimensions[0]), int(
            dimensions[1]), int(parts[1]), int(parts[2]), int(parts[3])))
    return image_sizes
