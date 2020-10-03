Title: Setting up SSH and Git for Multiple Accounts
Date: 2020-10-03 15:25
Tags: ssh, git, gpg
Slug: setting-up-ssh-and-git-for-multiple-accounts
Authors: Sébastien Lavoie
Summary: Simple workflow with SSH, GPG and Git to work remotely with multiple accounts in a convenient way.
Description: Simple workflow with SSH, GPG and Git to work remotely with multiple accounts in a convenient way.

[TOC]

---

# Introduction

To work effectively with services such as GitHub and GitLab, it is useful to set up a workflow that doesn't get in the way, especially when multiple accounts are involved. SSH will be set up to avoid entering the username/password combination every time we interact with remote repositories and Git will be set up to work differently for each account while signing the commits potentially with different GPG keys.

In short, we need to do the following:

* Set up SSH locally (in `~/.ssh/`);
* Set up SSH keys remotely (GitLab, GitHub, Bitbucket, etc.);
* Set up Git locally (in `~/.gitconfig`);
* Set up GPG keys remotely (add our keys(s) to GitLab, GitHub, etc.);
* Start interacting with remote repositories.

---

# Setting SSH locally

First, let's make sure we have some SSH keys to work with. The default location is `~/.ssh/id_rsa` (you can just press `Enter` when asked to save to a path):

```{.bash}
$ ssh-keygen -t rsa -C "email@personal.com"
```

The next key should have a different path:
```{.bash}
$ ssh-keygen -t rsa -C "email@work.com"
$ Enter file in which to save the key
  (/home/sglavoie/.ssh/id_rsa): /home/sglavoie/.ssh/id_rsa_work
```

Add the keys to the authentication agent like so:
```{.bash}
$ ssh-add /.ssh/id_rsa
$ ssh-add /.ssh/id_rsa_work
```

See which keys were added:
```{.bash}
$ ssh-add -l  # list the keys
```

If you need to delete any keys that were cached prior to that:
```{.bash}
$ ssh-add -D
```

Now, we need a configuration file:
```{.bash}
$ touch ~/.ssh/config
$ chmod 600 ~/.ssh/config
```

Let's add some content in there, assuming we deal with GitHub and GitLab, both with a personal account and a work account:
```{.txt}
AddKeysToAgent yes
Host github
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa
Host github-work
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_work
Host gitlab
   HostName gitlab.com
   User git
   IdentityFile ~/.ssh/id_rsa
Host gitlab-work
   HostName gitlab.com
   User git
   IdentityFile ~/.ssh/id_rsa_work
```

* The directive `AddKeysToAgent yes` is useful to avoid typing `ssh-add path_to_key` every time SSH is needed.
* The `Host` can have any name we want, it doesn't need to match the `HostName`.
* The `HostName` is the address we need to access. This should be the same thing for all accounts using a particular service (here, GitHub or GitLab).
* We can set the user to be `git` by default.
* For each `Host`, we indicate which `IdentityFile` to use when trying to work with a remote repository.

## Automatically load the keys from the Shell

For Zsh, the following can be added near the top of `~/.zshrc` when using the `ssh-agent` plugin:

```{.bash}
# Load multiple SSH keys
zstyle :omz:plugins:ssh-agent identities id_rsa id_rsa_work
```

With [Oh-My-Zsh](https://ohmyz.sh/), the `ssh-agent` plugin should be contained in `plugins` like so:

```{.bash}
plugins=(git ssh-agent fzf gitignore zsh-autosuggestions history-substring-search)

# Somewhere below
source $ZSH/oh-my-zsh.sh
```

With this setup, the SSH keys will be loaded when opening a terminal after booting up and those will be available for any subsequent terminal sessions until the user session is exited.

---

# Setting SSH keys remotely

The process will be slightly different on each platform on which we want to authenticate, but the gist of it is to paste the content of the public SSH key in the field when asked to do so.

* [Instructions for GitLab](https://gitlab.com/help/ssh/README).
* [Instructions for GitHub](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh).
* [Instructions for Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/set-up-an-ssh-key/).

---

# Setting Git locally

The idea is to have a `~/.gitconfig` file from which we load the main Git configuration by default (let's say, our personal account) and then we load another account  – overwriting the Git settings of the personal account with the settings defined for that other account – whenever we navigate to a directory that relates to that other account. Let's see this in action.

## Minimal `~/.gitconfig`

```{.bash}
# default configuration settings to load
[include]
  path = ~/.gitconfig-personal

# when working with company-x
# those settings are loaded only when the
# directory matches the pattern defined
[includeIf "gitdir:**/company-x/**/.git"]
  path = ~/.gitconfig-company-x
[gpg]
	program = gpg
[credential]
	helper = store
```

* The `[credential]` section with the setting `helper = store` will store your username/password combination when using HTTPS so you don't have to type it over and over again. You could also set this to `helper = cache` if you don't want to permanently store credentials.
* The `includeIf` directive will be triggered whenever you are in a directory containing `company-x` in this case so that your correct GPG key and Git settings will be used instead of the default settings for your personal account.
* In the block `[gpg]`, your system may be using the program `gpg2` instead of `gpg`.

## Minimal `~/.gitconfig-personal` and `~/.gitconfig-company-x`

Example for one of those:
```{.bash}
[user]
  email = email@work.com
  name = Sébastien Lavoie
  signingkey = A343702EBE11E0C2
[commit]
  gpgsign = true
```

If you don't have a GPG key already, you can generate one with this command:

```{.bash}
gpg --gen-key
```

To list existing GPG keys to determine the `signinkey` value to use in those files, you can type:

```{.bash}
gpg --list-secret-keys --keyid-format LONG
```

You might get an output similar to the following (this one is showing only one key):

```{.txt}
sec   rsa3072/A343702EBE11E0C2 2020-10-03 [SC] [expires: 2022-10-03]
      EF731EFC008D47D176C05910A343702EBE11E0C2
uid                 [ultimate] Sébastien Lavoie <email@work.com>
ssb   rsa3072/718726CCFED43B47 2020-10-03 [E] [expires: 2022-10-03]
```

The bit you need to retrieve for the `signingkey` value comes after the type of encryption, here it's `rsa3072` and the bit we want is `A343702EBE11E0C2`.

If you need to edit a key, there are plenty of options described with `man gpg` or `man gpg2`. For instance, to remove the expiration date for the above key:

```{.bash}
gpg2 --edit-key EF731EFC008D47D176C05910A343702EBE11E0C2
```

At the `gpg>` prompt, type `expire` and follow the instructions.

To delete a key, you can do so by referring to the email address like this:

```{.bash}
gpg --delete-secret-and-public-key email@work.com
```

Just follow the instructions from there. You may need to repeat the process multiple times if your email address is associated with more than one key.

---

# Setting GPG keys remotely

Just like with the SSH keys, the process differs from one platform to the other.

* [Instructions for GitLab](https://docs.gitlab.com/ee/user/project/repository/gpg_signed_commits/).
* [Instructions for GitHub](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-gpg-key-to-your-github-account).
* [Instructions for Bitbucket](https://confluence.atlassian.com/bitbucketserver/using-gpg-keys-913477014.html).

---

# Interacting with remote repositories

Now that the Git configuration is set up and we have SSH and GPG keys to authenticate ourselves and verify our identity when committing, respectively, we can start interacting with remote repositories. From the example we have been following, the file `~/.gitconfig-personal` will be used by default (and by consequence, our personal account).

## The SSH part

When first cloning, change the host so that it reflects what you have in `~/.ssh/id_rsa_correct_key_file`. For your personal account, no change would be required:

```{.bash}
git clone git@github.com:organization/repo.git
```

For a repository at work requiring the SSH key set up for the work account, you would need to change to the appropriate host like so (we still use the `git` user for convenience):

```{.bash}
git clone git@github-work:organization/repo.git
```

For a refresher, the following are the hosts we have set in `~/.ssh/config`: `github`, `github-work`, `gitlab`, `gitlab-work`.

The difference will be noticed when pushing/pulling as seen with `git remote -v`:

```{.bash}
$ git remote -v
origin	git@github-work:organization/repo.git (fetch)
origin	git@github-work:organization/repo.git (push)
```

Whereas the personal account will have the same host as usual, for instance `git@github.com:organization/repo.git`.

## The GPG part

If we want to keep our personal and work Git configurations separate (and we probably want that! ;)), it's only a matter of ensuring that the `includeIf` pattern contains, in this example, `company-x` somewhere in the path. When this is the case, we will see with `git config --list` in the cloned repository that our personal account details are loaded first, but if the `includeIf` directive matches, the settings for that other account will be applied on top and used when committing.

If you type `git config --list` and search for the word "email" in the output, it will appear only once when the default `~/.ssh/id_rsa` key is used (or whatever is read for the `IdentityFile` from the SSH configuration file) while you will see that same personal email showing up first in a work repository, but then later in the output you will find the work email, work GPG key and so on.

---

# Conclusion

This is one possible kind of setup we can use to work with SSH and GPG comfortably. This is pretty much a "set it and forget it" approach as long as you remember the following:

* **SSH**: Change the SSH host when cloning. If the repository is not publicly available, it would fail anyways (or you may realize you can clone it if it's a public repo but have no `push` access).
* **Git**: Make sure you are in a directory where the `includeIf` directive will kick in to set up the email, GPG key and so on.

One nice tip to help with the latter bullet point could be to define an alias, say in `~/.bash_aliases`, something like what follows:

```{.bash}
cdwork='cd /path/to/work/dir/with/appropriate/pattern'
```

Then, you simply `cdwork` and store all your Git repositories for work under that root repository, which would always match the desired pattern by default. That's it. Anything else related to the personal account can be cloned anywhere on the file system since this is the default configuration file used.
