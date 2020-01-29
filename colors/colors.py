# Script that embeds the colors from a given colors markdown file in config
# files.

#!/usr/bin/env python3

import argparse

# Color names, where the index corresponds to their number
# (e.g yellow = color3).
color_names = [
  'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
]
bright_color_names = map(lambda color_name: 'bright%s' % color_name, color_names)
color_names.extend(bright_color_names)

# Get the colors markdown file from an argument.
parser = argparse.ArgumentParser()
parser.add_argument('file_path',
                    metavar='file_path',
                    help='path to colors markdown file')
file_path = parser.parse_args().file_path
file_contents = open(file_path, 'r').read().split('\n')

# Split the file contents by color.
for i in range(len(file_contents)):
  line = file_contents[i]
  if line == '': continue
  print(line)
