Title: Executing Shell Commands in a Python Script
Date: 2019-03-08 14:34
Tags: python, script
Slug: executing-shell-commands-in-a-python-script
Authors: Sébastien Lavoie
Summary: Even for simple tasks, it is often worth basing one's work on existing solutions when it is an appropriate option... And such can be the case when writing Python scripts!
Description: Even for simple tasks, it is often worth basing one's work on existing solutions when it is an appropriate option... And such can be the case when writing Python scripts!

Python is awesome for producing high-quality code quickly
and efficiently, but it is not necessary to reinvent the
wheel in each project: this is why the third-party library on
[PyPI](https://pypi.org/) is so extensive. There are also occasions when
it is convenient to execute shell commands available in the terminal,
either to retrieve its output or to perform some work in the background.
I have wanted to do both when building this website, so here is one way
to accomplish this!

### Retrieve the output

```{.python}
def read_tree():
    '''Execute `tree` command and store the output in
    `tree.txt`.'''
    tree = subprocess.getoutput(f'tree .')
    print(tree)
    with open('./tree.txt', 'w') as f:
        f.write(tree)


read_tree()
```

In this example, the structure from the current directory is printed
when executing the code and it is later stored in a file. The output
could look something like the following:

```{.txt}
.
├── database_example
│   ├── example.sqlite
│   ├── db_manager.py
│   ├── review
│   │   └── sql_queries.txt
│   └── settings.py
├── database_sql.py
├── dump.sql
├── example.db
├── example.db.sql
├── example_info.txt
├── example_old.db
├── example_old.db.sql
├── sample
│   ├── chinook.db
│   └── sqlite-sample-database-diagram-color.pdf
├── test.db
└── test.sql

3 directories, 15 files
```

### Execute a command in the background

There are also instances in which is it useful to execute a program
from the terminal inside a Python script. This website, for example,
currently exports daily Git statistics in the `output/` folder. This
looks like this:

```{.python}
def daily_stats():
    '''Execute `Gitstats` once a day based on the date found in
    `stats_counter.txt`. Very simple with a caveat: it won't check if
    there are new commits on the same day if stats have already been
    generated on that day.'''
    today = datetime.today().strftime('%Y%m%d')
    with open('stats_counter.txt') as f:
        content = f.readline().strip()
    if content != today:
        current_loc = current_path()
        cmd = ["gitstats", "-c", "project_name='sglavoie.com'",
               f"{current_loc}", f"{current_loc}/output/stats/"]
        subprocess.run(cmd)
        with open('stats_counter.txt', 'w') as f:
            f.write(today)
```

This is an automated process, which is something Python is easy to use
for. However, it won't be necessary to program everything: it all gets
generated on demand!

## Conclusion

I am always amazed at how easy it can be to automate simple tasks like
those mentioned above. Programming can be very rewarding regardless of
initial abilities. Just beyond the most basic stuff, suddenly there is a
world that opens up to those that stay curious long enough.
