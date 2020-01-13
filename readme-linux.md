# Linux-specific setup

## Install `i3`
`i3` is a tiling window manager. First install `i3`:
```
sudo apt-get install i3
```

Then install `i3-gaps`, which allows you to add gaps between the windows. Follow
the instructions for building `i3-gaps` here:
```
https://github.com/Airblader/i3
```

## Setup `feh` the desktop wallpaper
```
sudo apt-get install feh
```

Add a wallpaper named `wallpaper.png` to the home directory. The wallpaper image
must be a `.png` for it to also work with `i3lock`.

## Install `lxappearance` to change the window theme
```
sudo apt-get install lxappearance
```

## Install kitty terminal
```
sudo apt-get install kitty
```

## Install a compositor
Compositors allow windows to become transparent and blurred. I'm using a
branched version of compton that allows kawase blur. Kawase blur creates a
really smooth blur, which isn't possible with the default box blur that's
supported by the original compton tool.

Build the compton compositor from this repo:
```
https://github.com/tryone144/compton
```

Make sure to install all dependencies, specifically make sure to install the mesa version of glx as opposed to the nvidia version of glx. If you don't do this, the tool will show an error where it can't find the glx context.

## Install `redshift`
Redshift makes the screen tinted yellow for night mode. Install:
```
sudo apt-get install redshift
```

Adjust the latitude and longitude of your location in `.config/redshift.conf`.

## Install `polybar`
Polybar is an alternative to i3's status bar. It allows more a ton more customization.

Install polybar from this repo:
```
https://github.com/jaagr/polybar
```

## Install [`i3lock-color`](https://github.com/PandorasFox/i3lock-color)
```
http://techmythoughts.blogspot.com/2018/01/installing-i3lock-color-on-ubuntu.html
```

## Extras
* Install `numlockx` for numlock control:
  ```
  sudo apt-get install numlockx
  ```