# Generate colors file for Xresources.

#!/usr/bin/env python3


def generateFile(root_path, colors, color_names):
    file_content = '\n'.join(
        map(
            lambda color_name: '*color%s: %s' %
            (color_names.index(color_name), colors[color_name]),
            color_names)) + '\n'
    file_path = '%s/linux/.Xresources.d/colors' % root_path
    file = open(file_path, 'w+')
    file.write(file_content)
    file.close()
