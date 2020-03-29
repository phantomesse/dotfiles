# Check if zplug is installed.
#
# If zplug is not installed, then install it.
if [[ ! -d ~/.zplug ]]; then
  git clone https://github.com/zplug/zplug ~/.zplug
  source ~/.zplug/init.zsh && zplug update --self
fi

# Essential for loading in zplug.
source ~/.zplug/init.zsh

# Make sure to use double quotes to prevent shell expansion.
zplug "zsh-users/zsh-syntax-highlighting"
zplug "softmoth/zsh-vim-mode"
zplug "denysdovhan/spaceship-prompt"
zplug "zdharma/history-search-multi-word" # Ctrl + r

# Install packages that have not been installed yet.
if ! zplug check --verbose; then
  printf "Install? [y/N]: "
  if read -q; then
    echo; zplug install
  else
    echo
  fi
fi

SPACESHIP_PROMPT_ORDER=(host dir git char)

# Spaceship prompt configuration.
SPACESHIP_HOST_SHOW="always"
SPACESHIP_HOST_COLOR="magenta"
SPACESHIP_HOST_COLOR_SSH="magenta"
SPACESHIP_DIR_COLOR="cyan"
SPACESHIP_DIR_TRUNC="0"
SPACESHIP_GIT_BRANCH_COLOR="yellow"
SPACESHIP_GIT_PREFIX=" on "
SPACESHIP_GIT_SUFFIX=""
SPACESHIP_CHAR_SYMBOL=" ❥ "
if [[ -n $SSH_CONNECTION ]]; then
  SPACESHIP_HOST_SHOW_FULL="true"
fi

# Need this for switching quickly between insert/normal in vim mode.
KEYTIMEOUT=2
MODE_CURSOR_VICMD="block"
MODE_CURSOR_VIINS="underline"

# Case-insensitive auto-complete.
zstyle ":completion:*" matcher-list "m:{a-zA-Z}={A-Za-z}"

# Select completions with arrow keys.
zstyle ":completion:*" menu select

# Allow multi-word history search to work with zsh syntax highlighting.
zstyle ":plugin:history-search-multi-word" reset-prompt-protect 1

# Bold the active history entry instead of underlining it.
zstyle ":plugin:history-search-multi-word" active "bold"

# Color auto-completion on "cd".
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"

# Load zplug plugins.
zplug load


###########
# HISTORY #
###########

# Preserve history when session exits.
export HISTFILE=~/.zsh_history
export HISTSIZE=10000
export SAVEHIST=10000

# Make "!!" show the last command rather than execute it.
setopt histverify


##########################
# USE VIM FOR EVERYTHING #
##########################

# Preferred editor.
export EDITOR='vim'

# Open the current command line in vim when pressing the "v" key.
bindkey -v


###########
# ALIASES #
###########

# Export path for ~/bin for custom functions.
export PATH=$HOME/bin:$PATH


###############
# OS SPECIFIC #
###############

case "$OSTYPE" in
  darwin*) # Mac
    # Use the homebrew in the local path.
#    export PATH=$HOME/homebrew/bin:$PATH
#    export PATH=/usr/local/Homebrew/bin:$PATH
  ;;
  linux*) # Linux
    # Export the NodeJS path.
    export NODEJS_HOME=/usr/local/lib/nodejs/node-$VERSION/bin
    export PATH=$NODEJS_HOME:$PATH

    # Find the id for a port.
    alias findport='netstat -plten | grep'
  ;;
esac

