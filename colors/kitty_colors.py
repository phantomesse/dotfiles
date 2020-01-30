# Generate colors.conf for kitty config.

#!/usr/bin/env python3

def generateFile(root_path, colors, color_names):
  file_content = '\n'.join([
    'background %s' % colors['bg'],
    'foreground %s' % colors['fg'],
    'selection_background %s' % colors['magenta'],
    'selection_foreground %s' % colors['bg'],
    'cursor %s' % colors['yellow'],
    'url_color %s' % colors['cyan']
  ])
  for i in range(len(color_names)):
    file_content += '\ncolor%s %s' % (i, colors[color_names[i]])
  file_content += '\n'

  file_path = '%s/linux/.config/kitty/colors.conf' % root_path
  file = open(file_path, 'w+')
  file.write(file_content)
  file.close()
