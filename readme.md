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

