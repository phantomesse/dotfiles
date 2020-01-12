# Lauren's Dotfiles Setup

This repository contains my personal dotfiles for both MacOS and Linux. This
dotfiles setup uses [GNU Stow](https://www.gnu.org/software/stow/) to install
the dotfiles in the correct locations and to install only the dotfiles required
for each operating system.

## Step 1: Install GNU Stow

### MacOS

Make sure that [Homebrew](https://brew.sh/) is installed and then install GNU
Stow as a brew package: `brew install stow`

### Linux

`sudo apt-get install stow`

## Step 2: Install zsh and setup terminal things

I'm using [zplug](https://github.com/zplug/zplug) as the plugin manager. It
should install automagically when sourcing `.zshrc`.

* Install [lolcat](https://github.com/busyloop/lolcat): This lets us print `ls`
  in rainbow colors.
* Install [colorls](https://github.com/athityakumar/colorls)
  * Install [nerd-fonts](https://github.com/ryanoasis/nerd-fonts)
    * If gem installing colorls doesn't work, try installing ruby-dev:
        `sudo apt-get install ruby-dev`
* Install [vim-plug](https://github.com/junegunn/vim-plug) and install plugins
  by opening vim and running `:PlugInstall`

## Step 3: Clone this GitHub repo

Clone this repository into `~/.dotfiles`:
`git clone git@github.com:phantomesse/dotfiles.git ~/.dotfiles`

# Step 4: Install config files

## Both MacOS and Linux
Be in the `.dotfiles` directory. `stow` puts everything in the `~` directory.

`stow shared`

# Linux-specific

## Install i3 as the window manager
i3 is a tiling window manager. First install i3:

```
sudo apt-get install i3
```

Then install i3-gaps, which allows you to add gaps between the windows. Follow the instructions for building i3-gaps here:

```
https://github.com/Airblader/i3
```

Install feh for the desktop wallpaper: `sudo apt-get install feh`
* Add a wallpaper to the home directory named `wallpaper.png`
  * Must be a `.png` for it to also work with i3lock

Install lxappearance to change the window theme:
```
sudo apt-get install lxappearance
```

Install kitty terminal:
```
sudo apt-get install kitty
```

## Install a compositor
Compositors allow windows to become transparent and blurred. I'm using a branched version of compton that allows kawase blur. Kawase blur creates a really smooth blur, which isn't possible with the default box blur that's supported by the original compton tool.

Build the compton compositor from this repo:
```
https://github.com/tryone144/compton
```

Make sure to install all dependencies, specifically make sure to install the mesa version of glx as opposed to the nvidia version of glx. If you don't do this, the tool will show an error where it can't find the glx context.

## Install fonts
To install fonts, download the font and put it in the `~/.fonts` folder and then run `sudo fc-cache -fv`.

## Install redshift
Redshift makes the screen tinted yellow for night mode. Install:

```
sudo apt-get install redshift
```

Adjust the latitude and longitude of your location in `.config/redshift.conf`.

## Install polybar
Polybar is an alternative to i3's status bar. It allows more a ton more customization.

Install polybar from this repo:
```
https://github.com/jaagr/polybar
```

## Install i3lock-coor
http://techmythoughts.blogspot.com/2018/01/installing-i3lock-color-on-ubuntu.html
https://github.com/PandorasFox/i3lock-color

# Extras
* Install numlockx for numlock control: `sudo apt-get install numlockx`
