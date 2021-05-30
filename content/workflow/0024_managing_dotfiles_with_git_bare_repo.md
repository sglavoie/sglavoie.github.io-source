Title: Managing dotfiles with a Git bare repository
Date: 2021-05-30 13:13
Tags: dotfiles, git, terminal
Slug: managing-dotfiles-with-git-bare-repository
Authors: Sébastien Lavoie
Summary: Keeping configuration files under version control with a Git bare repository is a fast, elegant and convenient solution!
Description: Keeping configuration files under version control with a Git bare repository is a fast, elegant and convenient solution!

[TOC]

---

# Introduction

I have been managing my configuration files for the past year using a technique I originally came across in [this YouTube video from DistroTube](https://www.youtube.com/watch?v=tBoLDpTWVOM). This uses a Git bare repository instead of the "usual" way, which consists of using a normal Git repository where one would store the actual configuration files and create symbolic links to all those files to the expected path on the system.

Needless to say, symlinks are a pain to manage when potentially hundreds of files need to be tracked in this way. Fortunately, working with a bare repository is much simpler: there's neither a need to move files around nor store any of them in the dotfiles bare repository either. Let's dive in to see how this works! I'll keep the instructions to the point: for more details, please refer to the article [The best way to store your dotfiles: A bare Git repository](https://www.atlassian.com/git/tutorials/dotfiles) from Atlassian, the source of knowledge behind this post.

---

# 1. Set up the system

Open a terminal and brace yourself to type a few commands. This will need to be done only once on any machine you use.

Set the following variable to the name of the directory where you want to store your dotfiles (e.g. `.dotfiles`, `dotfiles`, `cfg`, etc.):

```{.bash}
DOTFILES=dotfiles
```

Then type the following commands:

```{.bash}
git init --bare $HOME/$DOTFILES
alias config='/usr/bin/git --git-dir=$HOME/$DOTFILES/ --work-tree=$HOME'
config config --local status.showUntrackedFiles no
```

Depending on where you store your terminal aliases (e.g. `.bashrc`, `.zshrc`, `.bash_aliases`, etc.), set the following variable according to your needs:

```{.bash}
ALIASES=.bash_aliases
```

Once that is done, type the following command (or open the file containing your aliases with a text editor to manually put the alias wherever you want):

```{.bash}
echo "alias config='/usr/bin/git --git-dir=$HOME/$DOTFILES/ --work-tree=$HOME'" >> $HOME/$ALIASES
```

You can of course change the `config` alias to something else. I like to simply use `c` instead.

## 1.1 Create a repository to host your dotfiles

At this point, you will want to make sure you have created an empty Git repository on a website such as [GitHub](https://github.com/), [GitLab](https://gitlab.com/) or [BitBucket](https://bitbucket.org/). In the interface of that website, you should find a place that allows you to copy the link to that Git repository, which might look like something like this: `git@github.com:username/dotfiles.git`.

## 1.2 Set the remote to track your dotfiles

With your new Git repository created in the previous step, you will now want to add tracking information to be able to connect to the remote Git repository. You can do so as follows:

```{.bash}
config remote set-url origin git@github.com:username/dotfiles.git
```

For more information about this, you can read the article [Setting up SSH and Git for Multiple Accounts](https://www.sglavoie.com/posts/2020/10/03/setting-up-ssh-and-git-for-multiple-accounts/) if you'll be using an SSH key to connect and more specifically [the official documentation on the `git remote` command](https://git-scm.com/docs/git-remote).

---

# 2. Use the new system

## 2.1 On your current machine

Tracking changes will now be a breeze! All we have to do is to add files with our new alias (assuming `config` was chosen) to Git, commit and push to a remote repository to keep everything neatly backed up.

A typical workflow will look like this:

```{.bash}
config status
config add .gitconfig
config commit -m "Add .gitconfig"
config add .zshrc
config commit -m "Add .zshrc"
config push
```

## 2.2 On a different machine

Once yet have set up the system once with a remote repository, then the process becomes simpler as you can clone that repository and save a few steps. Here's what you'd be expected to do to set up the same dotfiles management system on another machine:

```{.bash}
# set to different values as desired
DOTFILES=dotfiles
REMOTE=git@github.com:username/dotfiles.git

alias config='/usr/bin/git --git-dir=$HOME/$DOTFILES/ --work-tree=$HOME'
echo "$DOTFILES" >> .gitignore
git clone --bare $REMOTE $HOME/$DOTFILES
config checkout
```

At this point, you might see an error message if you have existing configuration files on your machine in locations that are already tracked by Git in your dotfiles on the remote repository. If that's the case, you can move them to a secure place like so:

```{.bash}
mkdir -p .config-backup && \
config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | \
xargs -I{} mv {} .config-backup/{}
```

Let's make sure we don't show all untracked files again:

```{.bash}
config config --local status.showUntrackedFiles no
```

From here, this will be the same workflow as described in the section [2.1 On your current machine](#21-on-your-current-machine).

---

# Conclusion

No more symlinks: this is definitely a nicer approach! You will need to be a bit more familiar with Git if you need to edit your Git history such as with the `rebase` sub-command or when adding changes selectively such as with the sub-command `add -p` to add files interactively — which might be the case if you want to commit only part of the changes made to one file — but that's a great tool to master anyways ;).

## More resources and references

- [Git Bare Repository - A Better Way To Manage Dotfiles](https://www.youtube.com/watch?v=tBoLDpTWVOM) — DistroTube, YouTube
- [The best way to store your dotfiles: A bare Git repository](https://www.atlassian.com/git/tutorials/dotfiles), the source of the idea for this post. — Atlassian
