Title: Surfing with qutebrowser — a Keyboard-Driven Web Browser
Date: 2019-02-11 14:46
Tags: productivity, software, web
Slug: surfing-with-qutebrowser-a-keyboard-driven-web-browser
Authors: Sébastien Lavoie
Summary: I recently started using this software as my main web browser and, as a Vim (Neovim) user, I must say I am finding the adventure quite compelling!
Description: I recently started using this software as my main web browser and, as a Vim (Neovim) user, I must say I am finding the adventure quite compelling!

## What is qutebrowser?

[qutebrowser](https://qutebrowser.org/) is a web browser that makes
great use of **Vim** commands to navigate. From its website:

> qutebrowser is a keyboard-focused browser with a minimal GUI. It’s
> based on Python and PyQt5 and free software, licensed under the GPL.
> It was inspired by other browsers/addons like dwb and
> Vimperator/Pentadactyl.

---

### Why use it?

#### Perfect companion to any Vim user

The first notable feature of **qutebrowser** is obviously how well
the use of keyboard shortcuts is integrated with the experience of
using the software (there is a useful key binding cheatsheet on the
[homepage](https://qutebrowser.org/)). Search bindings (`/`, `n`/`N`,
`?`), visual mode (`v`), tabs (`gt`, `T`), copy (`yy`), open URLs
(`o`/`O`), `J` and `K` for switching tabs, etc. Many key bindings will
look familiar to Vim users.

It even features a _command mode_, accessible by typing `:`, just like
with Vim. Settings can be set from there directly, help can be accessed
by typing `:help [command/setting]`, the configuration file can be
customized on the fly, the position and size of tabs can be set in many
ways, history and settings page can be accessed and navigated through
like any other page (`hjkl`, `Ctrl + d`, `Ctrl + u`, `gg`, `G`), etc.

Even though it is based on Python which is a "_slow_" language, most of
the libraries and the web engine rely on C++ and the end result is a
fast and powerful browser that's totally customizable... Not unlike Vim.

#### Minimal interface ⇒ more space

Until I upgrade my laptop to a larger screen (≥ 17 inches), my
current setup with its 15 diagonal inches benefits tremendously
from configuring all applications to use pixels as efficiently as
possible — which is why I now use exclusively [i3 as a window
manager](/posts/2019/01/08/using-i3-as-a-window-manager-for-increased-pr
oductivity/).

**qutebrowser** doesn't even have a menu bar. By default, it only
displays a small tab bar at the top (which can be moved to another
side or removed) and a thin status bar at the bottom to see the URL,
the current position in the page expressed in percentage, the number
assigned to the current tab, etc. There is also a fullscreen mode
available like in most other web browsers with the key `F11`, which will
remove any window decoration and leave you in a (possibly) productive
mode.

#### History, bookmarks and quickmarks

The history page (`:history`), while being minimal like all the rest,
loads extremely fast and is a joy to navigate. The bookmarks page (`Sb`)
is equally simple yet useful. The way I like to open a bookmark is in
a new tab by typing `gB` (**g**o **b**ookmark as a mnemonic. Note that
usually all uppercase letters open or do some action in a new space,
such as a window or a tab).

Where **qutebrowser** shines in my opinion is with quickmarks. This is
a simple but genius way to find what you are looking for: you type `b`
(or `B` for new tab) to open a list of pages that are defined with a
keyword, you type that keyword (or can type anything to search for a
page), move around with arrow keys if necessary to select a page, type
`Enter` and there you go. As far as I know, Google Chrome doesn't offer
the equivalent (only keywords for search engines). Firefox allows to add
keywords for any bookmark that you have, but there is no good way to
search around for keywords, define them quickly, remove them quickly,
etc. **qutebrowser** comes with a set of commands that serve just this
purpose (`:quickmark-add`, `quickmark-del`, etc.), apart from adding
them very quickly by typing `m` for quickmarks and `M` for bookmarks.

#### Hinting system

You may have tried extensions for other web browsers such as Vimium,
Vimperator, or Vimium-FF that let you navigate with Vim shortcuts. They
usually use the letter `f` for **f**ollowing links. Some text appear on
the screen for each visible link and you type the letters that match the
link you want to see. The best way to get how it works is just to try it
out, really.

<a href="{static}/images/posts/0007_surfing-with-qutebrowser/qutebrowser_hints.png"><img src="{static}/images/posts/0007_surfing-with-qutebrowser/qutebrowser_hints.png" alt="qutebrowser-hints" class="max-size-img-post"></a>

Well, **qutebrowser** takes those features and make them even greater!
There is, for example, a _rapid hinting mode_ you can access by typing
`f` followed by `Ctrl + r` and it will open links in the background
for as long as you type any matching _hint_ provided as a letter or
combination of two letters when there are many visible links on the
page. This is especially useful when doing some research to avoid
breaking the rhythm on the current reading while preparing more
resources to be available.

---

### What's the best place to start learning about it?

The [help page](https://qutebrowser.org/doc/help/) on the website
contains all the information you really need. I did stumble upon the
following resources, which I would recommend to read in order of
appearance:

1. [Quickstart Guide](https://qutebrowser.org/doc/quickstart.html).
2. [Key bindings
   cheatsheet](https://raw.githubusercontent.com/qutebrowser/qutebrowser/ma
   ster/doc/img/cheatsheet-big.png).
3. [FAQ](https://qutebrowser.org/doc/faq.html), which is interesting
   but not indispensable. It did help me take a step forward in trying out
   **qutebrowser** though.
4. _Open inside qutebrowser_: [default
   keybindings](qute://help/settings.html#bindings.default).
5. _Open inside qutebrowser_: [settings page](qute://settings/).
6. [List of commands](https://qutebrowser.org/doc/help/commands.html).

---

## Conclusion

**qutebrowser** has been around for a while and is very stable. It is
ideal for any Vim user and is a great option for anyone interested in
efficiency and/or in trying out alternatives. Because I am very fond
of relying on the keyboard as much as possible and because I love to
program in Python, I have grown to like this web browser very quickly.
This is clearly a tool designed for a specific type of user in mind and
who knows, you might be one of those.
