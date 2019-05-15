Title: Tag Navigation in Vim
Date: 2019-04-19 17:52
Tags: productivity, vim
Slug: tag-navigation-in-vim
Authors: Sébastien Lavoie
Summary: A quick introduction to tag navigation in Vim/Neovim.
Description: A quick introduction to tag navigation in Vim/Neovim.

Let's jump right in.

## Navigate to definitions and tags

### Navigate inside the current buffer
There is a command `gd` that stands for **Goto local Declaration**. It is quite useful when looking for a variable inside the current buffer as it allows to jump to where it is declared when the variable is under the cursor. Using that command, you can also find where a function is declared and it will find the first occurrence in the current function. If looking for the first occurrence in the buffer, `gD`  (**Goto global Declaration**) will do the trick. You can jump back and forth to where you were with the commands `Ctrl + O` (older position) and `Ctrl + I` (newer position) in normal mode.

### Navigate inside all buffers within the current project
To be able to jump between buffers and go back to the origin of a declaration when it is imported in the current module, generating tags comes in very handy as it allows you to use the command `Ctrl + ]` to jump to a tag, just like when using the help pages in **Vim**.

To make this work, we can conveniently use `ctags`. First, we need to make sure it's installed on the system as follow:

---

#### Debian/Ubuntu

```bash
sudo apt-get install ctags
```

or

```bash
sudo apt-get install exuberant-ctags
```

#### OS X

```bash
brew install ctags
```

---

You can put the following command in your configuration file to be able to generate the necessary tags inside **Vim** by typing `MakeTags` in command mode:
```vim
command! MakeTags !ctags -R .
```

This will make it easy to remember how to do it. After that, open an existing project in its root directory and use this newly created `MakeTags` command to generate the tags. This will create a file named `tags` in the current working directory\*. Now, you will be able to open any file inside your project and jump to all the available declarations with `Ctrl + ]`.

\* <sub>Note: This will create tags recursively from the <em>current working directory</em>, <strong>not</strong> from the path matching the current buffer.</sub>


If you go to a tag that leads you a few declarations away in one file or another, you can come back with `Ctrl + T`. Here is a clear explanation from Vim's help:
```
The most obvious way to use this is while browsing through the call graph of
a program.  Consider the following call graph:

	main  --->  FuncA  --->  FuncC
	      --->  FuncB

(Explanation: main calls FuncA and FuncB; FuncA calls FuncC).
You can get from main to FuncA by using CTRL-] on the call to FuncA.  Then
you can CTRL-] to get to FuncC.  If you now want to go back to main you can
use CTRL-T twice.  Then you can CTRL-] to FuncB.
```

To keep those tags useful when you update your project, you can map a sequence that saves the buffer you are working on and then regenerates the tags automatically. Here is an example:
```vim
nnoremap <leader>W :w<CR>:MakeTags<CR>:echo 'ctags have been updated.'<CR>
```

And on this note, we're ready to conquer the world <i class="fas fa-smile-wink"></i>.
