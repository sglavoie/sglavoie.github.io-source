Title: Using dmenu to Optimize Common Tasks
Date: 2019-11-10 9:02
Slug: using-dmenu-to-optimize-common-tasks
Tags: bash, dmenu, i3, linux, productivity, script
Authors: Sébastien Lavoie
Summary: If remembering dozens of keyboard shortcuts isn't your forte, let [dmenu](https://tools.suckless.org/dmenu) come to the rescue! With this awesome tool, you will be able to create menus from plain text files swiftly and effortlessly (almost).
Description: If remembering dozens of keyboard shortcuts isn't your forte, let dmenu come to the rescue! With this awesome tool, you will be able to create menus from plain text files swiftly and effortlessly (almost).

# Introduction
[dmenu](https://tools.suckless.org/dmenu) is one of those tools that look a little unimpressive at first but can accomplish so much! It's a program that you can use to receive any output redirected from other programs (through pipes in the terminal, the symbol `|`) and treat that output so that it can pop up within a simple menu to make it available for execution. If you want to know more about other fantastic tools from [suckless.org](https://suckless.org), I [went over some of them before](https://www.sglavoie.com/posts/2019/05/12/suckless-minimalist-tools-that-work-great), such as the `st` terminal and `slock`, a dead simple screen locker.

---

# Any Simple Example?
You bet! Before diving in with how to install it and some more concrete examples, you could give `dmenu` a go with a simple command such as the following (assuming the program is installed on your machine).

```bash
ls | dmenu
```

This will effectively "pipe" the output of `ls` into `dmenu` and a menu like the following would appear (by default, it shows as a thin stripe at the top covering the width of the screen):

<a href="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_ls_command.png"><img src="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_ls_command.png" alt="dmenu_ls_command" class="max-size-img-post"></a>

If you start typing, the displayed list will be filtered down like so:

<a href="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_ls_command_typing.png"><img src="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_ls_command_typing.png" alt="dmenu_ls_command_typing" class="max-size-img-post"></a>

You can also switch to the next item to be highlighted by typing `Ctrl + n`, to the previous item by typing `Ctrl + p` and exit by reaching for the `Escape` key. For now, if you type `Enter` once your desired selection is highlighted, the selection will be outputted to the terminal and that will be the end of it. Let's convert this into a practical thing, then.

Keeping the same output as before which only contained directories, we could open a file manager (here, I'm going with `pcmanfm`) and do something like this (bear with me, the explanation follows!):

```bash
ls | dmenu -l 5 | xargs -I {} pcmanfm "{}"
```

This is now a fully functional example, albeit its practicality is debatable. What will happen, exactly?

First, `ls` will output a list of directories in the current working directory. That is, the following would be printed in the terminal without any piping:
```text
Desktop    Downloads  Learning  Pictures     Public   Templates  virtualbox_vms
Documents  Dropbox    Music     Programming  SortOut  Videos
```

When we _pipe_ this into `dmenu`, we will get a menu with all that output nicely formatted vertically, which is what the `-l 5` options does (here, we want only **5** lines to show). We will see a maximum of **5** items as this is the value we passed to the `-l` option:

<a href="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_ls_command_vertical_5_items.png"><img src="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_ls_command_vertical_5_items.png" alt="dmenu_ls_command_vertical_5_items" class="max-size-img-post"></a>

We can still start typing a word that doesn't show up in this list like `Mu` and we will see that this list is filtered to only include the matching directory `Music` even though we couldn't see it before since we limited our results to **5** items. We could also use the same technique with `Ctrl + n` and `Ctrl + p` to cycle between the elements.

Up to this point, we are getting our selection outputted to the terminal. Next, we pipe it into `xargs`, which will allow us to specify a command to which we will pass our result (what is printed to the terminal) as an argument (we could make use of more arguments depending on the output we get, but let's start simple). The `-I {}` option will make it possible to "quote" our result so it is read as a single argument and properly _escaped_. This means that without this option, if we have spaces or other special characters in the argument (such as a folder called `My Music`), it would try to pass each word as a new argument to `pcmanfm`, trying to open both `My` and `Music` directories at once.

We are representing our output as `{}` and when we quote it with `pcmanfm "{}"`, spaces are interpreted without any trouble. If we wanted to use various arguments instead, we could try something like this:

```bash
echo "file1.txt file2.txt\nfile3.txt file4.txt" | dmenu -l 2 | xargs cat
```

The part before the first pipe character will print to the terminal those two lines:
```text
file1.txt file2.txt
file3.txt file4.txt
```

When we pipe this into `dmenu -l 2`, we will get this menu:

<a href="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_echo_command_filenames.png"><img src="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_echo_command_filenames.png" alt="dmenu_echo_command_filenames" class="max-size-img-post"></a>

Typing `Enter` on one of the highlighted items would then trigger `xargs` to pass the content literally to `cat` as arguments, which would then print to the terminal the content of both `file1.txt` and `file2.txt` (the first line containing two arguments for `cat`) or the content of both `file3.txt` and `file4.txt` (the second line also containing two arguments for `cat`) in succession.

Now that we got our feet wet with what `dmenu` does (_displays a menu_), we might want to install it.

---

# How do You Install It?
In Manjaro Linux, it comes with `i3` if you use that flavor of the distribution and can be opened by pressing the modifier key (either `Super/Windows` key or `Alt` key) along with the letter `d`, as in the shortcut `mod + d`, or by typing `dmenu_run` in a terminal, which will present a list of installed applications to launch. Otherwise:

## Debian-based (such as Ubuntu)
```bash
sudo apt install dmenu
```

## Arch-based (such as Manjaro)
```bash
pacman -Syu dmenu
```

You can also install it from your distribution's package manager if available or [from source](https://tools.suckless.org/dmenu).

---

# Useful Real-World Examples
Here are a couple of ways I like to use `dmenu` to open a menu with a list of:

- cheat sheets;
- filesystem paths;
- most used documents;
- documents & books I read at the university;
- custom scripts I want to run in the background.

Here are a few screenshots of how it currently looks like in my daily usage so you get a better idea.

## Cheat sheets
<a href="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_cheat_sheets.png"><img src="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_cheat_sheets.png" alt="dmenu_cheat_sheets" class="max-size-img-post"></a>

## University shortcuts
<a href="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_university_shortcuts.png"><img src="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_university_shortcuts.png" alt="dmenu_university_shortcuts" class="max-size-img-post"></a>

## File manager shortcuts
<a href="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_file_manager_shortcuts.png"><img src="{static}/images/posts/0018_using-dmenu-to-optimize-common-tasks/dmenu_file_manager_shortcuts.png" alt="dmenu_file_manager_shortcuts" class="max-size-img-post"></a>

So, how does that all work? As a starting point, all of those menus are launched through a specific keyboard shortcut that uses a mnemonic for each one (`mod` being the "modifier" key on **i3**, which is set to `Super/Windows`):

- `mod + Alt + c`: **c**heat sheets;
- `mod + Alt + d`: **d**ocuments;
- `mod + Alt + f`: **f**ile manager;
- `mod + Alt + s`: **s**cripts;
- `mod + Alt + u`: **u**niversity.

Let's take the cheat sheets example, which is a bit more interesting since it launches different applications.

## Setting Up a Custom Command
### Configuration for i3 (bind a keyboard shortcut)
Here, I'm using [i3](https://i3wm.org) to set a keyboard shortcut to run a specific command, but this will be a similar experience on other window managers and desktop environments.

```text
# i3config file
# The backslash at the end of the line allows us
# to split the line to increase readability

## Cheatsheets

bindsym $mod+Mod1+c exec --no-startup-id \
cat ~/.custom/dmenu/cheatsheets.conf \
| dmenu -l 30 | sed 's/.*    \+//' | sh
```

You would usually be able to launch a custom command from your environment through a keyboard shortcut. If passing a direct command such as the above one isn't an option, you can always store it in a Bash script and run that Bash script instead as the designated custom command. The script would then contain the following:

```bash
#!/bin/bash

## Cheatsheets
cat ~/.custom/dmenu/cheatsheets.conf \
| dmenu -l 30 | sed 's/.*    \+//' | sh
```

As far as **i3** is concerned, that's all you need to do. You would need to reload the configuration file (by default: _i3config_) where the previous `bindsym` command has been set up to apply the changes (default shortcut to reload: `mod + Shift + c`).

### Configuration for cheatsheets.conf
The content of this file is literally what will be shown when **dmenu** opens it. An excerpt:
```
#---------- Cheat Sheets -------------------------------------------------------
bash          st -e nvim ~/Dropbox/Programming/cheatsheets/bash.sh
git           zathura ~/Dropbox/Programming/cheatsheets/github-git.pdf
vimwiki       firefox ~/Dropbox/Programming/cheatsheets/vimwiki.html
```

Here, we have set a maximum of **30** lines to be displayed (`-l 30`). What follows after an element has been selected with **dmenu** allows us to parse the content of the line and retrieve only the command we are interested in with `sed` before passing that filtered content around to `sh` to execute it as a shell command. With more complex commands requiring multiples arguments to be received, we could add one more pipe between `sed` and `sh` like this (or with `xargs -I {}` to avoid problems with spaces):
```bash
cat ~/.custom/dmenu/cheatsheets.conf \
| dmenu -l 30 | sed 's/.*    \+//' | xargs -r | sh
```

If the line we want to run only includes a path to a file as in:
```text
myshortcut       ~/path/to/a/file.pdf
```

We could instead pipe it into an external command of choice if the same program applies to all items presented in the menu, say Firefox:
```bash
cat ~/.custom/dmenu/pdf-and-docs.conf \
| dmenu -l 30 | sed 's/.*    \+//' | xargs -I {} firefox "{}"
```

What's nice with the way pipes work in a Unix-like system is that we can chain harmless commands until the very end so they will simply be printed to the terminal. In this example, if we want to see how to filter our lines before running a command, we can do so as follow.

#### Pipe 1
```bash
cat ~/.custom/dmenu/cheatsheets.conf \
| dmenu -l 30
```

If you remember from the menu we saw earlier, there's a shortcut to open a cheat sheet for Git. Let's say we selected that one with **dmenu**. Because our command isn't doing anything with the result, it will be outputted to the terminal like so (just like in the excerpt of `cheatsheets.conf`):
```bash
git           zathura ~/Dropbox/Programming/cheatsheets/github-git.pdf
```

What `sed` does here is to cut everything from the beginning of the line up to where the command starts (that's where we find [zathura](https://pwmt.org/projects/zathura/), which is a powerful document viewer), because we need to isolate that part of the line so it looks like a shell command we could run on its own. Let's add a new pipe to our command and see what `sed` does with it\*.

\* <sub>We could have used other tools to parse the string like `awk`, `grep`, `cut`, etc.</sub>


#### Pipe 2
```bash
cat ~/.custom/dmenu/cheatsheets.conf \
| dmenu -l 30 | sed 's/.*    \+//'
```
If we select the same item as before with **dmenu** to illustrate more clearly what this new addition does, we will get this output:
```bash
zathura ~/Dropbox/Programming/cheatsheets/github-git.pdf
```

If we were to type this in the terminal (assuming the file exists and **zathura** is installed!), that would do the trick and it would open with the specified document viewer. **Pipe 2** and subsequent pipes before we execute something is where the filtering magic happen. In short:

- Everything **before** `| dmenu` is how our input will look like when we run `dmenu`;
- Everything **after** `| dmenu [options here] |` is what we need to do to our input so that it is converted into a working shell command;
- Finally, what comes **after the last pipe** (either `xargs`, `sh` or a combination of both) is our way to redirect our string to the shell so it can be executed.

Once we are visually satisfied with how our command is supposed to look like (it has to be something that works when typed directly in the terminal), the next step is to pipe it again so it can be executed.

#### Pipe 3
```bash
cat ~/.custom/dmenu/cheatsheets.conf \
| dmenu -l 30 | sed 's/.*    \+//' | sh
```

There we go, the command is launched. If we keep the same simple syntax in all of our `.conf` files —or whatever extension we choose— where the content of our menus is stored in plain text, we can quickly and painlessly create keyboard shortcuts to run custom lists of commands that can be edited on the fly. Once our shortcuts are active, it's only a matter of editing one of those `.conf` files and automatically our lists will be up-to-date when we trigger the shortcut again.

## Running a Custom Script
If we want to run custom scripts, we need to indicate a command that would work in the terminal, such as `python myscrypt.py` or `./myscript.sh`. When it comes to shell scripts, we have to make sure they are executable. We can do so through a file manager or within the terminal like this:
```bash
chmod +x ~/path/to/script.sh
```

This will add the necessary permissions for the user to execute the script. As we already know, we would then need to add a keyboard shortcut to launch our custom menu and store our command in a file like `scripts.conf` that would contain the following:
```bash
#---------- scripts.conf -------------------------------------------------------
myscript           ~/scripts/script.sh
```

And that's all there is to know to get piping with `dmenu`! You may also find [this video from Luke Smith](https://www.youtube.com/watch?v=8E8sUNHdzG8) on YouTube to be quite helpful as well, which is where the inspiration for this post came from. He also [posted a complementary video](https://www.youtube.com/watch?v=R9m723tAurA) about adding prompts to your commands which is a nice way to add interactivity to your scripts!

---

# Customize the Look of dmenu
As they say, _"beauty is in the eye of the beholder"_. If you would rather make some changes to how dmenu look, you can. **dmenu** will be searching for the configuration file located at `~/.dmenurc`, which could contain something as put below (with this configuration, it will look like the screenshots shown previously):
```text
#
# ~/.dmenurc
#

## define the font for dmenu to be used
DMENU_FN="NotoSans-10.5"

## background colour for unselected menu-items
DMENU_NB="#161925"

## textcolour for unselected menu-items
DMENU_NF="#fdfffc"

## background colour for selected menu-items
DMENU_SB="#235789"

## textcolour for selected menu-items
DMENU_SF="#fdfffc"

## command for the terminal application to be used:
TERMINAL_CMD="st -e"

## export our variables
DMENU_OPTIONS="-fn $DMENU_FN -nb $DMENU_NB -nf $DMENU_NF -sf $DMENU_SF -sb $DMENU_SB"
```

# Conclusion
Hopefully this introduction to what **dmenu** has to offer gave you some ideas. I hope you'll find many ways to adapt the examples so you can benefit from this amazing tool. You can find more configuration details in my [dotfiles on GitHub](https://github.com/sglavoie/dotfiles/tree/master/config) for anything related to **i3**, **dmenu**, **zathura**, **st**, **slock** and many more useful programs.

Have a good time automating your digital life!
