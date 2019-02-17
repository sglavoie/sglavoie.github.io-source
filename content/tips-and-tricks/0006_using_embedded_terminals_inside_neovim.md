Title: Using Embedded Terminals Inside Neovim
Date: 2019-01-16 17:32
Tags: neovim, productivity, terminal
Slug: using-embedded-terminals-inside-neovim
Authors: Sébastien Lavoie
Summary: Because every pixel counts, this neat trick will allow to use terminals inside Neovim and maximize the screen estate for a flawless integration with one of the best text editor available.


## Terminals & Neovim

Terminal buffers are a built-in feature of `Neovim`. This means that terminals can be launched inside Neovim just like any other buffer, may it be a split window, a new tab or an independent buffer. Why is this so useful? Be prepared to be amazed.

<a href="{static}/images/posts/0006_using-embedded-terminals-inside-neovim/work_on_article.png"><img src="{static}/images/posts/0006_using-embedded-terminals-inside-neovim/work_on_article.png" alt="embedded-terminal" class="max-size-img-post"></a>

<a href="{static}/images/posts/0006_using-embedded-terminals-inside-neovim/terminal_buffers.png"><img src="{static}/images/posts/0006_using-embedded-terminals-inside-neovim/terminal_buffers.png" alt="terminal-buffers" class="max-size-img-post"></a>

(click to open)


### Seamless integration with Vim commands

For a start, terminals are not just _opened_ inside Neovim: they are truly integrated. When you type the letter `i` in a terminal buffer, it switches to a new mode, `Terminal`, where you have access to all underlying features of a regular Bash terminal, such as `CTRL + r` to search, tab completion of commands, `CTRL + w` to delete a word backwards or `CTRL + u` to delete the whole line backwards.

When you escape the `Terminal` mode, you switch back to `Normal` mode, where all Vim commands are available as usual, such as navigation, search, etc. Where this gets interesting is when you consider that the terminal is just like any other buffer (except it's not _modifiable_) and so you can for instance copy its content or paste into it from different registers. You can split them, view the line number, get automatic scrolling when output appears in `Insert` mode, you can switch back to `Normal` mode at any time even if a command hasn't completed... and of course all commands like `gt` to **g**o to another **t**ab work as always.

### Terminals get supercharged with the power of Vim

This is getting exciting (at least for me). Now, having a terminal with more power is useful in many cases:

- A whole terminal session can be saved to another file easily by copying the desired range (`:%y` to copy everything, for example).

- Instead of having to scroll with the mouse, all Vim commands are available to search and navigate through the buffer: `gg` to go to the beginning of the session, `G` to go to the end, `12G` to go to line number **12**, `/` or `?` to search forward and backward respectively. You can even set local or global marks to jump back and forth to precise lines consistently!

- It's even possible to send commands directly to a specific terminal or set up a REPL to execute any code, either a selection, a line or a range of lines. I don't personally use that feature yet, but I see how useful that can be and you can too if you watch this [screencast presented by Drew Neil](https://thoughtbot.com/upcase/videos/neovim-sending-commands-to-a-terminal-buffer) <i class="fas fa-tv"></i> on [thoughtbot.com](https://thoughtbot.com).

- If the terminal is opened in `Normal` mode, the cursor and the current position are kept intact even though new output could appear, such as would be the case if you are running a server in the background or waiting for a system update to finish. This is especially nice for instance if you are trying to debug a web application: you can leave the cursor exactly where you would like to keep reading the output and never get lost... Plus you have the ability to easily move around, search and copy like a ninja!


### The workflow is more compact and centralized

Because the terminals are running with one Neovim instance, you get everything in the same place, which is usually how you need to access your work anyway. If for some reasons you need to have multiple instances of Neovim running, this is possible too and in that situation you could simply split them into different workspaces.

Because everything is launched with Neovim, every terminal left open will also be exited when you close Neovim, shutting down any server or quitting any background interaction going on in the terminals. I have found that this behaviour is what I expect pretty much all the time because the idea of having a terminal inside a working session of Neovim is to work on something related, so it makes sense to close everything that's to do with a single project or task when you exit the text editor. No need for `CTRL + d` or `exit` anymore <i class="fas fa-smile-beam"></i>!

---

## Terminal settings to consider

I don't use many settings or mappings related to terminals, but I guess the nicest one is to remap the `Escape` key because by default, this is a weird mapping that leads to twisted fingers (`<C-\><C-n>`). Here is what I currently have in my `init.vim` file (the equivalent of `.vimrc` for Neovim):

~~~~{.vim}
set termguicolors  " Make colors look better in terminal

" Exit from terminal buffer (Neovim) more easily (remaps Esc key in terminal)
tnoremap <C-[> <C-\><C-n>

" Open terminal buffer (M stands for the Alt key)
nnoremap <M-t> :te<CR>

" Switch to terminal buffer automatically (when only one terminal is open)
nnoremap <M-0> :b term://<CR>

" Move between windows exactly the same way as usual
tnoremap <C-j><C-k> <C-\><C-N>
tnoremap <C-h> <C-\><C-N><C-w>h
tnoremap <C-j> <C-\><C-N><C-w>j
tnoremap <C-k> <C-\><C-N><C-w>k
tnoremap <C-l> <C-\><C-N><C-w>l
~~~~


---

## Conclusion

This was a quick overview of a feature that I have neglected for some time but recently realized how well it integrates with my workflow. You can find some more information by typing `:h terminal`. If you already use Neovim, it's worth giving it a try! Otherwise, it's worth giving [Neovim](https://neovim.io/) a try <i class="fas fa-laugh-wink"></i>.
