from PIL import Image
from collections import Counter
import sys


def extract_hex_colors(image_path, num_colors=5):
    """Return the most common colors in the image as hex strings."""
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        pixels = list(img.getdata())
    counter = Counter(pixels)
    top_colors = counter.most_common(num_colors)
    return ['#{:02x}{:02x}{:02x}'.format(r, g, b) for (r, g, b), _ in top_colors]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_hex_colors.py <image> [num_colors]")
        sys.exit(1)

    image_path = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    hex_colors = extract_hex_colors(image_path, count)
    for color in hex_colors:
        print(color)
