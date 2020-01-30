# Generate 16 colors from a given image (e.g. the wallpaper).
# Requires pillow package, install by running: `sudo pip3 install pillow`

import argparse
import os, sys
from PIL import Image
import math


class Color:
    def __init__(self, rgb):
        self.red = rgb[0]
        self.green = rgb[1]
        self.blue = rgb[2]
        self.hexcode = '#{:02x}{:02x}{:02x}'.format(self.red, self.green,
                                                    self.blue)
        self.brightness_key = self.red + self.green + self.blue
        self.saturation_key = max(self.red, self.green, self.blue) - min(
            self.red, self.green, self.blue)


# Get image to pull colors from.
parser = argparse.ArgumentParser()
parser.add_argument('image_file_path',
                    metavar='image_file_path',
                    help='path to image file')
image_file_path = parser.parse_args().image_file_path

image_size = 100
image = Image.open(image_file_path).resize([image_size, image_size],
                                           Image.LANCZOS)

# Get all unique pixels as Color objects, sorted from brightest to darkest.
colors = []
pixels = image.load()
for x in range(image_size):
    for y in range(image_size):
        rgb = pixels[x, y]
        colors.append(Color(rgb))
colors = list(dict.fromkeys(colors))
colors.sort(key=lambda color: color.brightness_key, reverse=True)

# Split colors into highlights, midtones, and shadows.
# Within each section, sort by saturation.
highlights = colors[::math.floor(len(colors) / 5)].sort(
    key=lambda color: color.saturation_key)
midtones = colors[math.floor(len(colors) / 5):0]
shadows = colors[math.floor(len(colors) / 5):
                 -1]  #.sort(key=lambda color: color.saturation_key)

print('\n'.join(map(lambda color: color.hexcode, shadows)))

# limit to a range to make it not too light / dark
# midtones will be the colors

fg_color = ''  # lightest color
bg_color = ''  # darkest color

# find 14 distinct colors and set them to red, green, yellow, etc. based on amount of red / green / yellow in each

# hex = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
