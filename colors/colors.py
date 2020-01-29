# Script that embeds the colors from a given colors markdown file in config
# files.

#!/usr/bin/env python3

import argparse

# Get the colors markdown file from an argument.
parser = argparse.ArgumentParser()
parser.add_argument('file_path',
                    metavar='file_path',
                    help='path to colors markdown file')
file_path = parser.parse_args().file_path
file_contents = open(file_path, 'r').read()
print(file_contents)

# Split the file contents by color.
