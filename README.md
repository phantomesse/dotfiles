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

# Step 2: Install config files

### Both MacOS and Linux
Be in the `.dotfiles` directory. `stow` puts everything in the `~` directory.

`stow vim`
