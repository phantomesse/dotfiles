#!/bin/bash
window_class=$(i3-msg -t get_tree | jq -r 'recurse(.nodes[];.nodes!=null)|select(.focused == true).window_properties.class')

if [[ $window_class == *"Google-chrome"* ]]; then
    i3-msg split v
    i3-msg focus parent
    i3-msg fullscreen
    i3-msg focus child
else
    i3-msg focus child
    i3-msg fullscreen
fi

