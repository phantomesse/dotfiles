# Generate colors file for iterm2.

#!/usr/bin/env python3


def __getColorFileContent(hexcode, alpha=1):
    rgb = tuple(int(hexcode[i:i + 2], 16) / 255 for i in (1, 3, 5))
    pairs = {
        'Alpha Component': alpha,
        'Blue Component': rgb[2],
        'Color Space': 'sRGB',
        'Green Component': rgb[1],
        'Red Component': rgb[0],
    }
    file_content = '  <dict>\n'
    for key in pairs:
        value = pairs[key]
        value_type = 'string' if type(value) == str else 'real'
        file_content += '    <key>%s</key>\n    <%s>%s</%s>\n' % (
            key, value_type, value, value_type)
    file_content += '  </dict>\n'
    return file_content


def generateFile(root_path, colors, color_names):
    file_content = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n'

    # Add the ansi colors.
    for i in range(len(color_names)):
        file_content += '  <key>Ansi %s Color</key>\n%s' % (
            i, __getColorFileContent(colors[color_names[i]]))

    # Add other colors.
    key_to_color_name_and_alpha_map = {
        'Background Color': ('bg', 1),
        'Badge Color': ('red', .5),
        'Bold Color': ('fg', 1),
        'Cursor Color': ('yellow', 1),
        'Cursor Guide Color': ('brightblack', .25),
        'Cursor Text Color': ('fg', 1),
        'Foreground Color': ('fg', 1),
        'Link Color': ('cyan', 1),
        'Selected Text Color': ('bg', 1),
        'Selection Color': ('magenta', 1),
    }
    for key in key_to_color_name_and_alpha_map:
        color_name_and_alpha = key_to_color_name_and_alpha_map[key]
        color = colors[color_name_and_alpha[0]]
        alpha = color_name_and_alpha[1]
        file_content += '  <key>%s</key>\n%s' % (
            key, __getColorFileContent(color, alpha))
    file_content += '</dict>\n</plist>'

    file_path = '%s/macos/Theme.itermcolors' % root_path
    file = open(file_path, 'w+')
    file.write(file_content)
    file.close()
