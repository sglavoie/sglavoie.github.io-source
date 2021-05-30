Title: Bash History Cleaner
Date: 2018-12-23 19:35
Modified: 2019-01-06 14:37
Tags: bash, linux, python, regex, script, terminal
Slug: bash-history-cleaner
Authors: Sébastien Lavoie
Summary: If you ever wanted to automatically clean your Bash history file, here is a working solution written in Python that uses regular expressions to set any kind of pattern you might be looking for.
Description: If you ever wanted to automatically clean your Bash history file, here is a working solution written in Python that uses regular expressions to set any kind of pattern you might be looking for.

[TOC]

---

# Introduction

This is a Python 3.6+ script that helps to clean the file containing
the Bash history commands. It will remove any line matching a specified
regular expression and can also remove any line starting with an alias.

The idea behind this small utility was simple:

-   The Bash history file (usually located in `~/.bash_history`) contains
    much of the work one ends up doing in the terminal.
-   The history can grow large over time and it becomes more cumbersome to
    find interesting information in all that clutter, such as a rarely used
    command with specific flags.
-   By removing all superfluous commands that are repeated often and which
    give no real benefit in certain contexts (such as `ls`, `cd`, `cat`,
    etc.), the history is much cleaner and easier to navigate and actually
    becomes much more useful in my opinion.
-   True, it will be harder to follow the bread crumbs for everything
    you did, but I haven't come across a situation where having access
    to yet another empty `ls` or `cd` has proven necessary and reading
    `.bash_history` doesn't make for a great narrative story either.

---

# Make history in a big way

I took advantage of the fact that the history can be cleaned with the
script you are about to see and set up what is known as an _eternal
history_ which, as it sounds like, can grow infinitely big! All you have
to do is append the following lines to the file `~/.bashrc`:

```{.bash}
# Eternal bash history.
# ---------------------
# Undocumented feature which sets the size to "unlimited".
# http://stackoverflow.com/questions/9457233/unlimited-bash-history
export HISTFILESIZE=-1
export HISTSIZE=-1
export HISTTIMEFORMAT="[%F %T] "
# Change the file location because certain bash sessions truncate
# .bash_history file upon close.
# http://superuser.com/questions/575479/bash-history-truncated-to-500-lines-on-each-login
export HISTFILE=~/.bash_eternal_history
# Force prompt to write history after every command.
# http://superuser.com/questions/20900/bash-history-loss
PROMPT_COMMAND="history -a; $PROMPT_COMMAND"
```

---

# Bash History Cleaner

And here is the script in question \*. It comes in two files that need to be in the same directory:

-   One is a Python file that needs to be launched from the terminal with
    Python 3.
-   The other file, `settings.json`, is a JSON file used to store the
    settings of the script, which will be detailed below.

\* <sub>Improvements to the original script can be found on <a
href="https://github.com/sglavoie/python-utilities/tree/main/bash_history_cleaner">Github</a>. To keep this
article a bit more readable, the original version is shown.</sub>

## `bash_history_cleaner.py`

```{.python}
'''
Python script that helps to clean the file containing the Bash history
commands.

Note: Requires Python 3.6+

It will remove any line matching a specified regular expression and can
also remove any line starting with an alias.

Description of available settings in `settings.json`:

    "home_directory":   Absolute path to user's home directory.

    "history_file":     Name of file where the history will be cleaned up.

    "aliases_file":     Name of file where Bash aliases are set up.

    "ignore_patterns":  List of patterns to ignore in `history_file`.
                        Each line where a pattern is found will be deleted.
                            → Patterns are specified as regular expressions.

    "add_aliases":      Boolean. If set to `true`, aliases from `aliases_file`
                        will be added to `ignore_patterns`.

    "aliases_match_greedily":
                        Boolean. If set to `true`, any line in `history_file`
                        starting with an alias in `aliases_file` will be
                        deleted. If set to `false`, delete line if the alias is
                        the content of the whole line (with optional space at
                        the end): `false` matches "^alias$" or "^alias $" only.

    "backup_history":   Boolean. If set to `true`, `history_file` will be backed
                        up in the same directory with a name ending in .bak
                        based on the current date.

    "delete_logs_without_confirming":
                        Boolean. If set to `true`, script with flag `-c` will
                        automatically delete all the backup files found for
                        `history_file`.
'''
from datetime import datetime
from pathlib import Path
import argparse
import fileinput
import glob
import json
import os
import re


def get_current_path():
    '''Returns the current working directory relative to where this script
    is being executed.'''
    return Path(__file__).parents[0]


def user_says_yes(message=""):
    '''Check if user input is either 'y' or 'n'. Returns a boolean.'''

    while True:
        choice = input(message).lower()
        if choice == 'y':
            choice = True
            break
        elif choice == 'n':
            choice = False
            break
        else:
            print("Please enter either 'y' or 'n'.")

    return choice


def delete_logs(settings: dict, history_file: str):
    '''Delete log files in `home_directory` based on `history_file`.'''

    # Retrieve a list of all matching log files
    log_files = glob.glob(f'{history_file}_*.bak')

    if log_files == []:
        print("There is no log file to delete.")
    else:
        print(f'Log files found in {settings["home_directory"]}:')

        for log_file in log_files:
            print(log_file)

        if settings['delete_logs_without_confirming']:
            for log_file in log_files:
                os.remove(log_file)
            print('Log files deleted.')
            return

        message = ("\nDo you want to delete those log files? [y/n] ")

        if user_says_yes(message=message):
            for log_file in log_files:
                os.remove(log_file)
            print('Log files deleted.')
            return

    print('Operation aborted.')
    return


def generate_date_string() -> str:
    '''Return date formatted string to backup a file.'''
    return datetime.strftime(datetime.today(), '_%Y%m%d_%H%M%S.bak')


def load_settings(settings_file: str) -> dict:
    '''Load settings in the script. Return them as a dictionary.'''
    with open(settings_file, "r") as read_file:
        settings = json.load(read_file)
    return settings


def get_list_aliases(bash_aliases_file: str, settings: dict) -> list:
    '''Retrieve the name of all the aliases specified in `bash_aliases_file`.

    Return aliases as a list of strings formatted as regular expressions.'''

    match_whole_line = bool(settings['aliases_match_greedily'])

    with open(bash_aliases_file) as file:
        content = file.read().splitlines()  # one alias per line
        aliases_list = []
        for line in content:
            try:
                # Get the actual alias in each line
                # Use negative lookbehind to remove 'alias ' at the beginning.
                # Matches anything after that is a dot, digit, underscore
                # or letter (will stop at the equal sign: alias blah='...')
                alias = re.search(r'(?<!not )alias ([\.\w]*)', line).group(1)

            # If for some reason the alias cannot be extracted, skip it
            # If search doesn't match, it's of type None and won't work
            except AttributeError:
                continue

            if match_whole_line:
                # Match the whole line if it starts with the alias.
                alias = f'^{alias}( )?$|^{alias} .*'
            else:
                # Will match only when alias is the whole content of the line,
                # followed by optional space.
                alias = f'^{alias}( )?$'

            # Escape dots in alias
            alias = alias.translate(str.maketrans({".":  r"\."}))

            aliases_list.append(alias)

    return aliases_list


def clean_bash_history(settings: dict, history_file: str):
    '''Modify in place `history_file` by removing every line where
    `ignore_patterns` is found.

    Optionally, add a list of aliases to `ignore_patterns` with
    `aliases` based on the value of `add_aliases` in settings.json.'''

    if settings['backup_history']:
        backup_str = generate_date_string()
        file_input = fileinput.FileInput(history_file,
                                         inplace=True,
                                         backup=backup_str)
    else:
        file_input = fileinput.FileInput(history_file,
                                         inplace=True)

    with file_input as file:
        for line in file:
            has_match = False
            for pattern in settings['ignore_patterns']:
                matched = re.compile(pattern).search
                if matched(line):
                    has_match = True
                    break
            # If no match is found (nothing to ignore), print the line
            # back into the file. Otherwise, it will be empty.
            if not has_match:
                print(line, end='')  # Line already has carriage return


def launch_cleanup(settings: dict, history_file: str, aliases_file: str):
    '''Main function that launches the cleanup process.'''

    bash_aliases = None
    if settings['add_aliases']:
        try:
            bash_aliases = get_list_aliases(aliases_file, settings)

            # add aliases to list of patterns to ignore
            settings['ignore_patterns'].extend(bash_aliases)
        except FileNotFoundError:
            print(f"File not found: {aliases_file}")
            quit()
    try:
        clean_bash_history(settings, history_file)
    except FileNotFoundError:
        print(f"File not found: {history_file}")


if __name__ == '__main__':
    SETTINGS_FILE_PATH = get_current_path() / 'settings.json'
    SETTINGS = load_settings(SETTINGS_FILE_PATH)
    ALIASES_FILE = SETTINGS['home_directory'] + '/' + SETTINGS['aliases_file']
    HISTORY_FILE = SETTINGS['home_directory'] + '/' + SETTINGS['history_file']

    # initiate the parser to check all the arguments passed to the script
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        '-c', '--clear', help='Delete all log files', action='store_true')

    # read arguments from the command line
    ARGUMENTS = PARSER.parse_args()

    if ARGUMENTS.clear:
        delete_logs(SETTINGS, HISTORY_FILE)
        quit()

    launch_cleanup(SETTINGS, HISTORY_FILE, ALIASES_FILE)
```

## `settings.json`

```{.json}
{
    "home_directory": "/home/sglavoie",
    "history_file": ".bash_eternal_history",
    "add_aliases": true,
    "aliases_file": ".bash_aliases",
    "aliases_match_greedily": true,
    "backup_history": true,
    "delete_logs_without_confirming": false,
    "ignore_patterns": [
        "^\\#\\d+",
        "^$",
        "^(\\.\\/)?pip$",
        "^(\\.\\/)?python.*$",
        "^\\.\\.$",
        "^alias",
        "^cd ",
        "^cd$",
        "^cd..$",
        "^fg$",
        "^df( )?",
        "^du( )?",
        "^exit$",
        "^git branch",
        "^git checkout master",
        "^git log$",
        "^git push$",
        "^git status$",
        "^git stauts$",
        "^kill \\d+.*",
        "^ls -a$",
        "^ls$",
        "^make|make install$",
        "^man ",
        "^pelican( )?$",
        "^pip install -r requirements.txt",
        "^pip.* list|pip.* show$",
        "^source ",
        "^sudo apt-get autoclean|sudo apt-get autoremove$",
        "^sudo apt-get dist-upgrade|sudo apt-get update$",
        "^which "
    ]
}
```

---

## Description of available settings in `settings.json`

| Name of setting                  | Description                                                                                                                                                                                                                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `home_directory`                 | Absolute path to user's home directory.                                                                                                                                                                                                                                      |
| `history_file`                   | Name of file where the history will be cleaned up.                                                                                                                                                                                                                           |
| `aliases_file`                   | Name of file where Bash aliases are set up.                                                                                                                                                                                                                                  |
| `ignore_patterns`                | List of patterns to ignore in `history_file`. Each line where a pattern is found will be deleted. Patterns are specified as regular expressions.                                                                                                                             |
| `add_aliases`                    | Boolean. If set to `true`, aliases from `aliases_file` will be added to `ignore_patterns`. (Default: `true`)                                                                                                                                                                 |
| `aliases_match_greedily`         | Boolean. If set to `true`, any line in `history_file` starting with an alias in `aliases_file` will be deleted. If set to `false`, delete line if the alias is the content of the whole line (with optional space at the end): `false` matches "^alias$" or "^alias $" only. |
| `backup_history`                 | Boolean. If set to `true`, `history_file` will be backed up in the same directory with a name ending in .bak based on the current date. (Default: `true`)                                                                                                                    |
| `delete_logs_without_confirming` | Boolean. If set to `true`, script with flag `-c` will automatically delete all the backup files found for `history_file`. (Default: `false`)                                                                                                                                 |

---

# Anecdotal evidence of satisfying performances

Performance-wise, this scans ~8,300 lines per second on my modest Intel
Core i5 laptop with files of over 200,000 lines long. Not that I type so
much stuff in the terminal: I just duplicated many lines.

---

# Conclusion

This is a simple solution to an nonexistent problem, but it was
in the end very instructive to me nonetheless. You may even find
a use for it! Otherwise, you might use the same functions for
other files such as logs! If you would like to take a closer look
at the source in a more convenient way, you can find the code <a href="https://github.com/sglavoie/python-utilities/tree/main/bash_history_cleaner">available on Github</a>.
