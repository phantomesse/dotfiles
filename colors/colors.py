# Script that embeds the colors from a given colors markdown file in config
# files.

#!/usr/bin/env python3

import os
import argparse
import kitty_colors
import xresources_colors
import iterm_colors

# Color names, where the index corresponds to their number
# (e.g yellow = color3).
color_names = [
    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
]
bright_color_names = list(
    map(lambda color_name: 'bright%s' % color_name, color_names))
color_names.extend(bright_color_names)

# Get the colors markdown file from an argument.
parser = argparse.ArgumentParser()
parser.add_argument('file_path',
                    metavar='file_path',
                    help='path to colors markdown file')
file_path = parser.parse_args().file_path

# Get and split the file contents by color.
file_contents = open(file_path, 'r').read().split('\n\n')
color_groups = map(lambda group: group.split('\n'), file_contents)
colors = {}
for color_group in color_groups:
    label = color_group[0][2:-2]
    colors[label] = color_group[1]
    if (len(color_group) > 2): colors['bright%s' % label] = color_group[2]

# Generate config files.
root_path = '/'.join(os.path.realpath(__file__).split('/')[0:-2])
kitty_colors.generateFile(root_path, colors, color_names)
xresources_colors.generateFile(root_path, colors, color_names)
iterm_colors.generateFile(root_path, colors, color_names)
