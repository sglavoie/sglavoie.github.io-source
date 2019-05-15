Title: Aliases: Also Known as Terminal User's Best Friends
Date: 2018-12-08 13:52
Tags: aliases, bash, productivity, terminal
Slug: aliases-also-known-as-terminal-users-best-friends
Authors: Sébastien Lavoie
Summary: Here are presented a few terminal aliases that I find myself using regularly.
Description: Here are presented a few terminal aliases that I find myself using regularly.


## Some aliases that I find useful

---

> In all the following examples, the dollar sign `$` at the beginning of
commands represents the prompt, it should not be typed.

### General-purpose

---

#### List all aliases

~~~~{.bash}
$ alias
~~~~

Prints all of your aliases. If you have plenty of those, you might
prefer to pipe this command with `less` to get a nice pager that allows
you to easily nagivate them:

~~~~{.bash}
$ alias | less
~~~~

---

#### Setting an alias in `~/.bash_aliases`

~~~~{.bash}
alias c='clear'
~~~~

This would set `c` as a shortcut to `clear`. In order to use the
newly created alias, you would have to close the terminal or type the
following command in the terminal:

~~~~{.bash}
$ source ~/.bash_aliases
~~~~

---

#### Clear the screen

~~~~{.bash}
alias c='clear'
~~~~

I like being absorbed into the emptiness of the terminal, so this one
comes in handy to tidy up the work space.

---

#### Reset the terminal

~~~~{.bash}
alias re='tput reset'
~~~~

If for some reasons the terminal displays badly or display funky
characters, it can usually be reset this way.

---

#### Exit from the terminal

~~~~{.bash}
alias q='exit'
~~~~

For exiting the terminal as if you were still in Vim!

---

#### Display all file extensions recursively from the current directory

~~~~{.bash}
alias allextensions="find . -type f -name '*.*' | sed 's|.*\.||' | sort -u"
~~~~

It comes in handy to spot if a file shouldn't be there or to check for
lower or uppercase extensions.

---

#### Find text inside files, including filenames

~~~~{.bash}
alias findinfiles='ag --nobreak --nonumbers --noheading . | fzf'
~~~~

In this example, the alias is set up with
[ag](https://github.com/ggreer/the_silver_searcher), a fast
code-searching tool and [fzf](https://github.com/junegunn/fzf), a great
fuzzy finder.

---

#### Reboot and shutdown the system

~~~~{.bash}
alias reboot='systemctl reboot'
alias shutdown='systemctl poweroff'
~~~~

This will reboot or power off the system without needing root privileges
in most working conditions.

---

#### List and sort files and directories by modification time

~~~~{.bash}
alias treeold='tree -hDF | less'
~~~~

This requires the command `tree` to be installed. The parameters are
(descriptions taken from `man tree`):

`-h`: Print the size of files in a human readable way.

`-D`: Print the date of the last modification time.

`-F`: Append a '`/`' for directories, a '`=`' for socket files, a '`\*`'
for executable files, a '`>`' for doors (Solaris) and a '`|`' for
FIFO's, as per `ls -F`.

---

#### Open files quickly with default applications

~~~~{.bash}
alias o='xdg-open'
~~~~

This will open files and URLs specified as argument in the default
application detected.

---

#### Moving around

If you are going to be working on projects for some time and require to
`cd` into them, I have found the following to be useful:

~~~~{.bash}
$ cdnameOfProject  # instead of having to do cd /path/to/project/
$ # More examples:
$ cdcodeabbey  # For codeabbey.com
$ cdhackerrank  # For hackerrank.com
$ cdeuler  # For projecteuler.net
$ cdgit  # For all Github repositories
~~~~

This is not advanced by any means, but it helps quite regularly! Since
you can take advantage of tab completion, you can type `cd` (without
adding a space) and then press `TAB` key to autocomplete the aliases.

~~~~{.bash}
alias ...='cd ../..'
~~~~

Make it easier to navigate into deep directory structures by basically
doing `cd .. && cd ..` to go back up two directories at once.

---

#### Listing files

~~~~{.bash}
alias l='ls -CFh'
alias la='ls -Ah'
alias ll='ls -ahlF'
alias ls='ls --color=auto'
~~~~

Different ways to set up the command ls to quickly see the needed files.
The parameters are (descriptions taken from `man ls`):

`-A`: _Do not list implied `.` and `..`._

`-C`: _List entries by columns._

`-F`: _Append indicator (one of `\*/=>@|`) to entries._

`-a`: _Do not ignore entries starting with ._

`-h`: _With `-l` and/or `-s`, print human readable sizes (e.g., 1K 234M 2G)._

`-l`: _Use a long listing format._

---

### Python-related

---

~~~~{.bash}
alias aNameOfProject='source /path/to/project/bin/activate'
alias aa='source ~/Programming/anaconda3/bin/activate'  # Example using Anaconda distribution
~~~~

The purpose is to activate a specific virtual environment quickly. The
command `cd` could be added to go to the related project also:

~~~~{.bash}
alias gNameOfProject='cd /path/to/project/ && ./.venv/bin/activate'
~~~~

Where `.venv` would be the name of the virtual environment.

I like to **a**ctivate environments starting aliases with `a` and **go**
and activate at the same time starting aliases with `g`. This way, it
feels like I am speaking the Vim language (`cw` for **c**hange **w**ord,
for example).

---

~~~~{.bash}
alias da='deactivate'
~~~~

This will deactivate a virtual environment.

---

~~~~{.bash}
alias p36='python3.6'
alias p='python3.7'  # Simply using `p` for main version of Python
~~~~

Practical way to quickly open the desired Python version.

---

~~~~{.bash}
alias pyclean='find . -regex ".*\(__pycache__\|\.py[co]\)" -delete'
~~~~

This will delete recursively all files and directories that match one of
the following patterns in their name: `__pycache__`, `.pyc` or `.pyo`.

---

## Conclusion

I hope you will find at least one alias to improve your productivity.
Of course, you are welcome to chime in with your own suggestions <i
class="fas fa-smile-wink"></i> !
