Title: fzf - A Fuzzy Finder to Accomplish Anything
Date: 2019-05-24 10:56
Tags: plugin, productivity, shell, terminal
Slug: fzf-a-fuzzy-finder-to-accomplish-anything
Authors: Sébastien Lavoie
Summary: Search and, most importantly, finally find what you are looking for on your machine. If you rely on the terminal a lot, **fzf** may well be capable of speeding up your productivity!
Description: Search and, most importantly, finally find what you are looking for on your machine. If you rely on the terminal a lot, fzf may well be capable of speeding up your productivity!

I know people who make such a mess when _not_ organizing their files and
directories appropriately on their system, they would benefit greatly
from `fzf`.

## What is fzf?

From the [official GitHub page](https://github.com/junegunn/fzf):

> fzf is a general-purpose command-line fuzzy finder. It's an
interactive Unix filter for command-line that can be used with any list;
files, command history, processes, hostnames, bookmarks, git commits,
etc.

----

## Terminal aliases

One of the main uses of `fzf` is from the terminal. Being so flexible
to use, it can be combined with all kinds of commands with the help
of pipes (`|`) to bend it to your desires. Here are some aliases I am
currently using that undoubtedly improve my terminal workflow.

~~~~{.bash}
##### Functions

# Select a configuration file with fzf and open it with Neovim
conf() { du -a ~/.dotfiles/* ~/.config/* | awk '{print $2}' | fzf | xargs -r nvim ;}

# Select a file from current folder and recursively with fzf and open it with Neovim
se() { du -a ./* | awk '{print $2}' | fzf | xargs -r nvim ;}

# Select a file recursively from university folder with fzf and open it with default app
sc() { du -a ~/Dropbox/university/* | awk '{print $2}' | fzf | xargs -r xdg-open ;}
~~~~

The first alias, `conf` (short for _configuration_), allows to search
only within the two folders specified for configuration files, which
makes it pop almost instantaneously since it doesn't have to scan files
scattered anywhere else. You can then type anything that partially
matches a file path and even include slashes (`/`) in your match if you
know in which directories to look. You can then type `Enter` to open the
file with your favorite text editor (here set to `nvim`) or type `CTRL +
c` to abort the command.

The other aliases work in a similar fashion. `se` (short for _search_)
will simply search recursively for any kind of files in the current
directory and open the selected file in a text editor. Of course,
certain file types can be excluded and everything else can be tweaked
with more piping power. In the case of the third alias, `sc` (short for
_school_), it will also search recursively for any kind of file in the
`university` folder and will open it with the default application set to
open that kind of file (video, image, text, PDF, etc.).

----

## Vim/Neovim integration

Using [Vim-Plug](https://github.com/junegunn/vim-plug) from the same
author as `fzf` is as easy as adding the following to Vim/Neovim's
configuration file. First, we make sure that `fzf` is available on the
system and install it if it's not. Then, we install the `fzf.vim` plugin
to integrate fzf in Vim and optionally, we may configure more options so
that `fzf` can be used more optimally, which can be found on the [GitHub
plugin page](https://github.com/junegunn/fzf.vim).

~~~~{.vim}
Plug 'junegunn/fzf', { 'dir': $HOME . '/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'

""""" [ FZF ]
" Allows fzf to ignore patterns in .gitignore
let $FZF_DEFAULT_COMMAND = 'ag -g ""'

" Mapping selecting mappings
nmap <leader><tab> <plug>(fzf-maps-n)
xmap <leader><tab> <plug>(fzf-maps-x)
omap <leader><tab> <plug>(fzf-maps-o)

" Insert mode completion
imap <c-x><c-k> <plug>(fzf-complete-word)
imap <c-x><c-f> <plug>(fzf-complete-path)
imap <c-x><c-j> <plug>(fzf-complete-file-ag)
imap <c-x><c-l> <plug>(fzf-complete-line)

" Advanced customization using autoload functions
" (expand word completing window)
inoremap <expr> <c-x><c-k> fzf#vim#complete#word({'left': '20%'})

" Make use of fzf command instead of CtrlP
map <C-p> :FZF<cr>
""" [ / FZF ]
~~~~

### Working with Neovim

`fzf` really shines when used with Neovim as it is extremely fast,
especially when configured with
[The Silver Searcher](https://github.com/ggreer/the_silver_searcher)
which deserves its own article. It
integrates with core functionality of Vim and makes it easy to find what
you are looking for.

From the above configuration, for instance:

~~~~{.vim}
nmap <leader><tab> <plug>(fzf-maps-n)
~~~~

This allows to search for existing mappings and commands, which can be
faster than diving in the help pages when looking for a quick reference.

This one in insert mode is very handy:

~~~~{.vim}
imap <c-x><c-k> <plug>(fzf-complete-word)
~~~~

Without affecting keyword completion with `CTRL + n` and `CTRL + p`
(unless you have `set complete+=k` in your configuration file), you can
complete words from a custom dictionary of your choice with `CTRL + x
CTRL + k`. The window that appears can be moved and resized, which is
what is happening here:

~~~~{.vim}
inoremap <expr> <c-x><c-k> fzf#vim#complete#word({'left': '20%'})
~~~~

In the same way, file paths can be completed from the current working
directory `CTRL + x CTRL + f` and existing lines can be quickly inserted
with `CTRL + x CTRL + l`.

<a href="{static}/images/posts/0016_a_fuzzy_file_finder_to_accomplish_anything/fzf_autocompletion.png"><img src="{static}/images/posts/0016_a_fuzzy_file_finder_to_accomplish_anything/fzf_autocompletion.png" alt="fzf_line_autocompletion" class="max-size-img-post"></a>

Finally, I use `fzf` to open any file quickly from the working directory
inside Neovim with the mapping `CTRL + p`, which replaces the CtrlP
plugin and can work much faster on larger codebases.

----

## Conclusion

There is much more that can be done with it and I am barely scratching
the surface here. Luke Smith shared
[a great video](https://www.youtube.com/watch?v=vt33Hp-4RXg) that will
complement the information from this post nicely with a more technical
approach. Highly recommended to see more practical ways to use this
superb piece of software!

[Luke Smith](https://lukesmith.xyz/) also makes a strong point of
combining `fzf` with [dmenu](https://tools.suckless.org/dmenu/), a tool
that I described succinctly in
[a previous article](https://www.sglavoie.com/posts/2019/05/12/suckless-minimalist-tools-that-work-great/).

