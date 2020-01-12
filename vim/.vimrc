" Enable modern Vim features not compatible with Vi spec.
set nocompatible

" All of your plugins must be added before the following line.
call plug#begin('~/.vim/plugged')

" All of your plugins must be added before the following line.
call plug#begin('~/.vim/plugged')
Plug 'dart-lang/dart-vim-plugin'
Plug 'natebosch/vim-lsc'
Plug 'PotatoesMaster/i3-vim-syntax'
Plug 'scrooloose/nerdtree'
Plug 'scrooloose/nerdcommenter'
Plug 'leafgarland/typescript-vim'
call plug#end()

let g:lsc_server_commands = {'dart': 'dart_language_server'}
let g:lsc_auto_map = v:true
let g:lsc_enable_apply_edit = v:true

" Map Ctrl+N to toggle nerd tree.
map <C-n> :NERDTreeToggle<CR>

" Remove "Press ? for help" text in nerd tree.
let NERDTreeMinimalUI = 1

" Show hidden files.
let NERDTreeShowHidden = 1

" Enable file type based indent configuration and syntax highlighting.
filetype plugin indent on
syntax on
set modeline

" Enable auto-completion.
set wildmode=longest,list,full

" Custom dividers.
set fillchars+=vert:│
hi StatusLine    ctermfg=DarkMagenta ctermbg=None  cterm=None
hi StatusLineNC  ctermfg=DarkGray    ctermbg=None  cterm=None
hi VertSplit     ctermfg=Black       ctermbg=None  cterm=None

" Highlight current line.
set cursorline
set nu " Show line number.
hi CursorLine    ctermfg=None        ctermbg=Black cterm=None
hi LineNr        ctermfg=DarkGray

set backspace=indent,eol,start
set history=1000
set nobackup
set nowrap
set mousehide
set nu " Show line number

set incsearch
set hlsearch
set ignorecase
set smartcase

set shiftround
set tabstop=4 softtabstop=0 expandtab shiftwidth=2 smarttab
set ai " Auto indent
set si " Smart indent
set whichwrap+=<,>,h,l,[,]

autocmd FileType make set noexpandtab
autocmd FileType txt set wrap
autocmd BufRead,BufNewFile *.zsh-theme set syntax=sh

" Markdown file settings.
autocmd BufRead,BufNewFile *.md setlocal wrap
autocmd BufRead,BufNewFile *.md setlocal spell
autocmd BufRead,BufNewFile *.md setlocal colorcolumn=80

set clipboard=unnamedplus

set mouse=a

" Copy to buffer.
vmap <C-c> :w! ~/.vimbuffer<CR>
nmap <C-c> :.w! ~/.vimbuffer<CR>

" Paste from buffer.
map <C-p> :r ~/.vimbuffer<CR>

