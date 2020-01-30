# Generate 16 colors from a given image (e.g. the wallpaper).
# Requires pillow package, install by running: `sudo pip3 install pillow`

import argparse
import os, sys
from PIL import Image
import math
import colorsys


class Color:
    def __init__(self, rgb):
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        hsl = colorsys.rgb_to_hls(red / 255, green / 255, blue / 255)
        self.hexcode = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
        self.brightness_key = red + green + blue
        self.saturation_key = max(red, green, blue) - min(red, green, blue)
        self.hue = hsl[0]
        self.redness = 1 - abs(self.hue - .1) + (red - blue - green) / 255
        self.greenness = 1 - abs(self.hue - .3) + (green - blue - red) / 255
        self.blueness = 1 - abs(self.hue - .6) + (blue - red - green) / 255


# Get image to pull colors from.
parser = argparse.ArgumentParser()
parser.add_argument('image_file_path',
                    metavar='image_file_path',
                    help='path to image file')
image_file_path = parser.parse_args().image_file_path

image_size = 30
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
parition = math.floor(len(colors) / 5)
highlights = colors[0:parition]
midtones = colors[math.floor(parition / 2):math.floor(len(colors) / -2)]
shadows = colors[-parition:]

# Within each section, sort by saturation.
highlights.sort(key=lambda color: color.saturation_key)
midtones.sort(key=lambda color: color.saturation_key)
shadows.sort(key=lambda color: color.saturation_key)

# Keep only the more saturated half of the midtones and sort midtones by hue.
midtones = midtones[math.floor(len(midtones) / -2):]
midtones.sort(key=lambda color: color.hue)

# Set the foreground and background colors.
fg_color = highlights[math.floor(len(highlights) * 2 / 3)]
bg_color = shadows[math.floor(len(shadows) / 3)]

# Find the reddest, bluest, and greenest colors from the midtones.
red_index = 0
green_index = 0
blue_index = 0
for i in range(math.floor(len(midtones))):
    color = midtones[i]
    if color.redness > midtones[red_index].redness: red_index = i
    if color.greenness > midtones[green_index].greenness: green_index = i
    if color.blueness > midtones[blue_index].blueness: blue_index = i

# Fill in the other colors.
yellow_index = math.floor(abs(red_index - green_index) / 2) + min(
    red_index, green_index)
cyan_index = math.floor(abs(blue_index - green_index) / 2) + min(
    blue_index, green_index)
magenta_index = math.floor(red_index / 2 if red_index > len(midtones) -
                           blue_index else (len(midtones) - blue_index) / 2 +
                           blue_index)
color_to_midtone_index_map = {
    'red': red_index,
    'green': green_index,
    'yellow': yellow_index,
    'blue': blue_index,
    'magenta': magenta_index,
    'cyan': cyan_index,
}

# Determine white by finding the largest gap between colors and taking the
# middle of the largest gap.
index_pairs = [(red_index, yellow_index), (yellow_index, green_index),
               (green_index, cyan_index), (cyan_index, blue_index)]
largest_gap_index_pair = index_pairs[0]
for pair in index_pairs:
    if pair[1] - pair[0] > largest_gap_index_pair[1] - largest_gap_index_pair[
            0]:
        largest_gap_index_pair = pair
color_to_midtone_index_map['white'] = math.floor(
    (largest_gap_index_pair[1] - largest_gap_index_pair[0]) /
    2) + largest_gap_index_pair[0]

# Add bright colors.
bright_color_to_midtone_index_map = {}
for color_name in color_to_midtone_index_map:
    normal_color_index = color_to_midtone_index_map[color_name]
    bright_index = normal_color_index + 1 if normal_color_index < len(
        midtones) else normal_color_index - 1
    bright_color_to_midtone_index_map[color_name] = bright_index

# Create file.
file_content = '**fg**\n%s\n\n**bg**\n%s\n' % (fg_color.hexcode,
                                               bg_color.hexcode)

shadows.sort(key=lambda color: color.brightness_key)
file_content += '\n**black**\n%s\n%s\n' % (shadows[0].hexcode,
                                           shadows[1].hexcode)

for color_name in color_to_midtone_index_map:
    file_content += '\n**%s**\n%s\n%s\n' % (
        color_name, midtones[color_to_midtone_index_map[color_name]].hexcode,
        midtones[bright_color_to_midtone_index_map[color_name]].hexcode)

root_path = '/'.join(os.path.realpath(__file__).split('/')[0:-2])
file_path = '%s/colors/wallpaper.md' % root_path
file = open(file_path, 'w+')
file.write(file_content)
file.close()
