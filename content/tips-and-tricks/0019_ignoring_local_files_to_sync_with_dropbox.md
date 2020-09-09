Title: Ignoring Sync of Local Files to Dropbox on Linux
Date: 2019-11-30 13:22
Slug: ignoring-sync-of-local-files-to-dropbox-on-linux
Tags: aliases, linux, shell, terminal
Authors: Sébastien Lavoie
Summary: To make the most of Dropbox, it can make sense to backup the files you care the most about and skip the ones that simply take too long to upload and eat up all your space. Such candidates could be hidden `.git/` folders and `node_modules/`, but how do you exclude them locally? Let's find out.
Description: To make the most of Dropbox, it can make sense to backup the files you care the most about and skip the ones that simply take too long to upload and eat up all your space. Such candidates could be hidden .git/ folders and node_modules/, but how do you exclude them locally? Let's find out.

[TOC]

---

# Introduction

[Dropbox](https://www.dropbox.com) is an awesome company which has been until recently the working home of none other than [Guido van Rossum](https://gvanrossum.github.io), the creator of the [Python](https://www.python.org) programming language. It works like a charm out of the box on Linux and can be installed easily enough through the package manager that comes with your chosen distribution.

## Why Dropbox?

In my experience, it has been working flawlessly and syncs consistently faster than Google Drive. It's also worth mentioning that there is still no official Google Drive Linux client to this day: some users of the [GNOME](https://www.gnome.org) desktop environment will connect to their Google account and mount Google Drive within the file manager [Nautilus/Files](https://wiki.gnome.org/Apps/Files); other users will use the paid software [Insync](https://www.insynchq.com) or the free software alternative [ODrive](https://liberodark.github.io/ODrive/). No thanks.

On the other hand, Dropbox is easy to use with any flavor of Linux and also syncs seamlessly with mobile devices. I use Dropbox for its convenience, but other solutions exist like [Syncthing](https://syncthing.net) that do not depend on proprietary software and third-party cloud services. I store mostly insensitive information in my Dropbox account and for the few files that happen to be a bit more sensitive (such as the password database I synchronize on both desktop and mobile with [KeePassXC](https://keepassxc.org) and [Keepass2Android](https://github.com/PhilippC/keepass2android), respectively), they are of course encrypted (hopefully in a secure way).

Because I like to keep things simple and light on system resources, I do not let Dropbox run in the background (it only syncs once a day in the evening). Since all one needs to do in order to use it is to create and modify files inside a specific folder (such as `~/Dropbox` by default), it can just synchronize at any moment and conflicts will be handled automatically if you make changes in more than one place that's being synced.

## So, what's wrong with Dropbox?

With all that said, there's one little feature that I find missing with Dropbox when using the official Linux client and that's the **ability to selectively sync local files**. Yes, there is a [selective sync](https://help.dropbox.com/installs-integrations/sync-uploads/selective-sync-overview) feature available, but that will delete the local copy of your files and store them in the cloud only, _not the other way around by keeping your local files intact and prevent uploading them to the cloud_. There are some hacks you can do to avoid this, but this isn't a particularly enticing work flow, because we can do better.

<a href="{static}/images/posts/0019_ignoring-local-files-to-sync-with-dropbox-on-linux/dropbox_selective_sync.png"><img src="{static}/images/posts/0019_ignoring-local-files-to-sync-with-dropbox-on-linux/dropbox_selective_sync.png" alt="dropbox_selective_sync" class="max-size-img-post"></a>

You may have heard of other alternatives like [GoodSync](https://www.goodsync.com) that allow, through yet another third-party proprietary software, to ignore specific files at your request. That's not what we are after here: instead, there's something you can do from the terminal that works quite well, too. At the time of this writing, it is still a _beta feature_ [according to this page](https://help.dropbox.com/files-folders/restore-delete/ignored-files):

> This feature is currently in beta and not available to all Dropbox users. It will be rolled out to more users in the future.

Yet, because you can work with this feature programmatically to ignore and _un-ignore_ files from your Dropbox directory, I thought it was worth giving it a try. Here is how I'm using it to give you a few ideas.

---

# Any simple example?

Getting started is quick and painless. To ignore a file within your Dropbox folder, you only need to use the `attr` command to **set** (`-s`) the special attribute `com.dropbox.ignored` to give it a **value** of `1` (`-V 1`) so it ignores a file (`file.txt` in this example) as follow:

```bash
cd /path/to/file/in/Dropbox/folder

attr -s com.dropbox.ignored -V 1 file.txt
```

## Ignore all .git and node_modules folders

Things get **really** interesting when we can do that automatically by matching a specific pattern (it depends who you ask, anyways). How about exploring recursively the whole directory tree to exclude only hidden `.git` folders? Suppose you store your Git projects in `~/Dropbox/git/`. You would then do something like this:

```bash
cd ~/Dropbox/git/

find . -type d -name ".git" |
    xargs -I {} attr -s com.dropbox.ignored -V 1 "{}"
```

In an instant, you will start getting some feedback printed to the terminal for each `.git` folder that is being found:

```text
Attribute "com.dropbox.ignored" set to a 1 byte value for ./path/to/.git:
1
```

Dealing with `node_modules` folders is equally easy. Because a message will be printed to the console every time a file attribute is changed, you could want to delete the output (preferably once you are sure you are modifying only the targeted files!) by redirecting it to `/dev/null`, a _null device_ that discards all data it receives. We can always split a long command onto multiple lines with a backslash character `\` like so (it's not required right after the pipe `|` symbol):

```bash
find . -type d -name "node_modules" |
    xargs -I {} attr -s com.dropbox.ignored -V 1 \
    "{}" > /dev/null
```

---

# Can we make this simpler?

Yes we can! An `alias` might be a bit hard to manage, but we can definitely create a set of functions that will be accessible from anywhere in the terminal. It suffices to add them to your shell configuration file, which could be located in `~/.profile`, `~/.bash_profile`, `~/.zshrc` or something else depending on your shell.

One solution that I see fit for this purpose is to have two distinct functions that have antagonistic effects so that we can revert our changes in a pinch. Basically, setting a value of `1` for the attribute `com.dropbox.ignored` ignores a file while setting it back to `0` tells Dropbox to sync it again. Our functions could be conveniently called `dropbox-ignore` and `dropbox-sync`.

Now, the following functions could become quite a bit more complicated to take into account various scenarios and custom behaviors, but let's keep things simple and assume that the user knows what is going to happen. We could have our two functions as follow:

```bash
# Ignore specific files/directories in Dropbox
dropbox-ignore(){
  arg1=$1
  arg2=$2
  find . -type $arg1 -name "$arg2" |
      xargs -I {} attr -s com.dropbox.ignored -V 1 "{}"
}

# Sync specific files/directories in Dropbox
# that were previously ignored (or not)
dropbox-sync(){
  arg1=$1
  arg2=$2
  find . -type $arg1 -name "$arg2" |
      xargs -I {} attr -s com.dropbox.ignored -V 0 "{}"
}
```

## How do you use those functions?

Our commands will be accessible by typing `dropbox-ignore` and `dropbox-sync` the next time we open a terminal window. Both functions do exactly the same thing, but `dropbox-ignore` sets the attribute value to `1` to ignore files and `dropbox-sync` sets the attribute to `0` to allow syncing to happen.

<sub>Note: For simplicity and practicality, keep in mind that those commands will search <strong>recursively from the current working directory</strong>. It's also good to know that if you set an attribute value to <code>1</code> then back to <code>0</code> again, Dropbox will need to re-sync the affected files and directories.</sub>

We need to pass them two arguments: the first is the type of search to perform (pass `f` for **files** and `d` for **directories**) and the second is the pattern to match in the name (`node_modules` or `.git` would fit here, no need to use quotes). Concretely, that will look like this:

```bash
# To ignore a file matching the pattern `myfile`
dropbox-ignore f myfile

# To avoid syncing node_modules/ directory
dropbox-ignore d node_modules

# Te re-add a .git/ folder to Dropbox
dropbox-sync d .git

```

---

# Conclusion

This tip may certainly not be the best approach to solving this particular issue with Dropbox on Linux, but I hope you find it useful nevertheless as it worked out very nicely on my end! One could store files and directories elsewhere, working with symbolic links or hard links as necessary to reference files or simply give up on making a backup with Dropbox in some circumstances. But I like to keep an extra copy of projects I'm working on in Dropbox and that can include potentially large files that don't need to be backed up, so ignoring what's not indispensable can speed up the syncing process tremendously while keeping disk usage in the cloud possibly much lower.

Dropbox only calculates the size of the files being synced in the cloud, so you can end up needing a lot more space locally if you ignore a number of big files or, conversely, selectively syncing many files will result in a cloud storage larger than what's needed locally.
