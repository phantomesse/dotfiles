# Lauren's dotfiles setup
This repository contains my personal dotfiles for both MacOS and Linux. Further
documentation on [MacOS-specific setup](readme-macos.md) and
[Linux-specific](readme-linux.md) setup is available in linked files.

## 1️⃣ Clone this GitHub repo

Clone this repository into `~/.dotfiles`:
```
git clone git@github.com:phantomesse/dotfiles.git ~/.dotfiles
```

## 2️⃣ Use `stow` to place the correct dotfiles
This dotfiles setup uses [GNU Stow](https://www.gnu.org/software/stow/) to
install the dotfiles in the correct locations and to install only the dotfiles
required for each operating system.

### Install GNU Stow
MacOS (install via [Homebrew](https://brew.sh/)):
```
brew install stow
```

Linux:
```
sudo apt-get install stow
```

### Place the dotfiles
When running `stow` commands, ensure that you are in the .dotfiles directory:
```
cd ~/.dotfiles
```

For both MacOS and Linux, install the shared dotfiles:
```
stow shared
```

For MacOS-specific dotfiles:
```
stow macos
```

For Linux-specific dotfiles:
```
stow linux
```

## 3️⃣ Setup terminal things
I use [zsh](https://www.zsh.org/) as my shell instead of the default bash shell
since it is faster and provides more modern configuration. I'm using
[zplug](https://github.com/zplug/zplug) as the plugin manager. It should install
automagically when sourcing `.zshrc`.

To improve the terminal experience, install the following:

* [tmux](https://github.com/tmux/tmux) - a terminal multiplexer that allows
  split screens and multiple panes within the terminal
* [lolcat](https://github.com/busyloop/lolcat) - I use this to print `ls` in
  rainbow colors
* [colorls](https://github.com/athityakumar/colorls) - adds icons to `ls`
  * To get the icons to show up, make sure that a font from
    [nerd-fonts](https://github.com/ryanoasis/nerd-fonts) is installed
  * If `gem` installing `colorls` doesn't work, try installing `ruby-dev`:
    ```
    sudo apt-get install ruby-dev
    ```
* [vim-plug](https://github.com/junegunn/vim-plug) - plugin manager for vim
  * Install plugins by opening `vim` and running `:PlugInstall`

Aliases such as the `ls` alias that uses `lolcat` and `colorls` are stored in
`~/bin`. Make sure that they are executable by doing:
```
chmod a+x ~/bin/ls
```

## Colors
The `colors.py` script in the colors folder updates the terminal (Kitty) and the
Xresrouces colors. It also generates an iTerm2 color theme which must be manually imported into iTerm2. Run this script to update the colors:

```
python3 colors/colors.py colors/solarized.md
```

## Fonts
On my personal Mac, I use
[Operator Mono](https://www.typography.com/fonts/operator/styles) as my
monospace font.

On machines that do not have an Operator Mono license, I use
[Input Mono](https://input.fontbureau.com/) with the customized settings
ready-to-download from here:
```
https://input.fontbureau.com/preview/?size=14&language=css&theme=solarized-dark&family=InputSans&width=300&weight=400&line-height=1.4&a=ss&g=ss&i=serifs_round&l=serifs_round&zero=0&asterisk=height&braces=0&preset=default&customize=please
```

For my Linux machines, I use San Francisco as the window font (e.g. in the
toolbar and GUIs). It can be downloaded from here:
```
https://github.com/AppleDesignResources/SanFranciscoFont
```

I also use the [Noto Color Emoji](https://www.google.com/get/noto/help/emoji/)
font to have colored emojis on my Linux machines. It can be downloaded from
here:
```
https://github.com/googlefonts/noto-emoji
```

To install fonts on Linux, download the font, put it in the `~/.fonts` folder,
and then run:
```
sudo fc-cache -fv
```
