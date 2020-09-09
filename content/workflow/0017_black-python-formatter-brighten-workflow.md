Title: Black: A Python Formatter to Brighten Your Workflow
Date: 2019-07-13 13:10
Tags: neovim, plugin, productivity, terminal, vim
Slug: black-a-python-formatter-to-brighten-your-workflow
Authors: Sébastien Lavoie
Summary: Meet [Black](https://github.com/python/black), a superb Python code formatter that will automatically reformat your code in accordance to PEP-8 standards.
Description: Meet Black, a superb Python code formatter that will automatically reformat your code in accordance to PEP-8 standards.

[TOC]

---

## What is Black?

From its [GitHub repository](https://github.com/python/black):

> Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

**Black** will take less than ideal code and will automatically reformat it according to the [PEP-8 style guide](https://www.python.org/dev/peps/pep-0008/). It will take care of many things, including the following (taken in that order from `README.md` in **Black**'s repo):

-   Wrapping lines properly by shortening as much as possible single statements;
-   Break long lines;
-   Remove superfluous empty lines;
-   Take care of adding trailing commas where necessary;
-   Convert single quotes (`'`) to double quotes (`"`);
-   Convert numeric literals to lowercase (`0XAB` to `0xAB`);
-   Superfluous parentheses are removed;
-   Split call chains on different lines;
-   Works from the terminal and support many code editor integrations (Emacs, Vim, VS Code, Sublime, etc.).

Now that it's clear _why_ it can be a good idea to use it, let's see how it works with Vim and the terminal.

---

## How to use it?

First, we need to install it using Python 3.6.0+:

```{.bash}
$ pip install black
```

That's it!

### Use it from the terminal

In its simplest invocation, we can use **Black** by specifying a file or a directory by typing:

```{.bash}
$ black path_to_file_or_directory
```

It doesn't come with many options as its goal is to automatically format code consistently, but you can find out more about this tool in the following way:

```{.bash}
$ black --help
```

### Use it with Vim

Using **Black** as part of your workflow in a code editor is where I believe it really shines, because you can see almost in real-time when you make a formatting mistake, which will help down the road in committing less sins.

Integrating **Black** with Vim or Neovim is quick and painless, adding a simple line in your `.vimrc` or `init.vim` file. You can also proceed to do a manual installation without a plugin manager as explained in the GitHub repository.

With [vim-plug](https://github.com/junegunn/vim-plug):

```{.vim}
Plug 'python/black'
```

With [Vundle](https://github.com/VundleVim/Vundle.vim):

```{.vim}
Plugin 'python/black'
```

Once the plugin is installed, it may well be convenient to automatically format Python files when saving the buffer, which can be accomplished by adding the following line to the configuration file:

```{.vim}
autocmd BufWritePre *.py execute ':Black'
```

By default, **Black** works surprisingly well on its own. I only went ahead and changed the default line length from 88 to 79 characters by also adding this line:

```{.vim}
let g:black_linelength = 79  " default is 88
```

Finally, it's worth noting you can update **Black** at any point from the terminal with `pip` and you can also do it directly from within Vim/Neovim with this command:

```{.vim}
:BlackUpgrade
```

Vim will then output something along those lines:

> Upgrading Black with pip...

> DONE! You are all set, thanks for waiting

## Any example?

Taking a random Python 3.6+ code sample, we could originally have something like this (hopefully not):

```{.python}
    for source in  data_sources :


        # Retrieve a list of all matching log files in `source`
        log_files=glob.glob( f'{source}/{LOG_NAME}*' )
        if log_files  ==  [ ]:
                print(f'\nThere is no log file to delete in {source}.')
                continue
        else    :
                print(f'Log files in {source}:')
                for log_file in log_files:
                    if (ARGUMENTS.remind): REMINDER_IS_SET = True
                    print(
                            log_file
                    )
                message = (
                    '\nDo you want to delete log files ' 'for this source? (y/n) '
                )
                if (user_says_yes( message = message )) :
                    for log_file in log_files: os.remove(log_file)
                    print(
                            'Log files deleted.'
                            )
                    continue
                else : continue
        print( 'Exiting script...' )
        sys. exit(0)
```

Running **Black**, we will get something that's quite a bit more palatable:

```{.python}
    for source in data_sources:

        # Retrieve a list of all matching log files in `source`
        log_files = glob.glob(f"{source}/{LOG_NAME}*")
        if log_files == []:
            print(f"\nThere is no log file to delete in {source}.")
            continue
        else:
            print(f"Log files in {source}:")
            for log_file in log_files:
                if ARGUMENTS.remind:
                    REMINDER_IS_SET = True
                print(log_file)
            message = (
                "\nDo you want to delete log files " "for this source? (y/n) "
            )
            if user_says_yes(message=message):
                for log_file in log_files:
                    os.remove(log_file)
                print("Log files deleted.")
                continue
            else:
                continue
        print("Exiting script...")
        sys.exit(0)
```

---

## Conclusion

I think the results speak for themselves: enforcing a style with a tool like **Black** is definitely useful to avoid arguments about conflicting coding styles. It lets you focus on what matters instead: being productive while providing value to the world.
