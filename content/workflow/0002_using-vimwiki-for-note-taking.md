Title: Using Vimwiki for Note-Taking
Date: 2018-12-03 13:26
Modified: 2018-12-26 14:45
Tags: neovim, note-taking, productivity, vim, vimwiki
Slug: using-vimwiki-for-note-taking
Authors: Sébastien Lavoie
Summary: This short article explains why Vimwiki felt like the right solution to organize my notes.

## What is Vimwiki?

From the [official website](https://vimwiki.github.io/):
> Vimwiki is a personal wiki for Vim – interlinked, plain text files written in a markup language.

As this relies upon Vim's power to write content in a simple format, this quickly became a viable option to organize more and more notes!

----

## What were the other options <span style="white-space:nowrap">considered?</span>

I have used various approaches in the past for different purposes and reasons, including *Evernote*, *Simplenote*, *Microsoft OneNote*, *Google Docs*, *Boostnote*, *Freeplane*/*FreeMind* (mind-mapping), *Workflowy* and even plain `.txt` files. Each has its pros and cons, but I then decided to limit my options based on the following self-imposed requirements:

- It has to be **available on Linux**. Right from the start, this would disqualify many applications such as *Notational Velocity*, *Bear*, *Quiver*, *Paper*, *Ulysses* and *Squid*.
- It has to be **open source** as this is a philosophy that I strongly embrace. Plus, having the ability to freely modify it and contribute to the project is an important additional bonus. Adiós *Evernote*, *Google Docs*, *Dropbox Paper*, *Microsoft OneNote*, *Workflowy* and *Quip*.
- It has to be **fast to use** and it has to make it possible to **express oneself in more than one way**. Say goodbye to *[Freeplane](https://www.freeplane.org)* (otherwise great for general brainstorming!) and *FreeMind* (which has been abandoned by its own developers): both are relatively slow on an old machine because they use Java and it is quite a stretch to use them for something other than mind maps. In that same category would disappear *[draw.io](https://www.draw.io/)*, which is fantastic for making flowcharts and diagrams!
- It has to be versatile enough to handle features such as **including images, links and attached files** and have a way to perform **search and replace**. Ciao *[Simplenote](https://simplenote.com/)* which is, well, simple. Even though it doesn't fit the bill in this case, it remains a great option as it can synchronize your notes with many different devices (iOS, MacOS, Android, Windows and Linux). It has a feature that allows you to move a slider which acts as a timeline and shows you a different version of your note since its creation with the actual date and time down to the minute for each *restore point*. You can also use tags and Markdown and it has options to share and collaborate with others. Highly recommended <i class="fas fa-grin-alt"></i>!
- It should have a hefty user base to back it up. This would exclude text editor plugins such as `atom-notes` for *Atom* or `VSNotes` for *VS Code*, which also lack features for accomplishing all of the above.
- On top of everything else, it has to be **available offline**, in a **portable and readable format**. Now, after discarding most options, we are left with *Boostnote* which uses CoffeeScript-Object-Notation and *Vimwiki* which has its own Wiki syntax that's similar in many ways to Markdown\*. Those are the strongest contenders that I could think of but of course, if you would like to share your recommendations, please do so in the comments below!

\* <sub>I somehow discredited **[Emacs](https://www.gnu.org/software/emacs)** simply because I started to learn Vim first and since I'm still far from understanding all of its features, I had to postpone the discovery of Emacs <i class="fas fa-grin-beam"></i>.</sub> 

### One feature-rich alternative to Vimwiki

After settling down on Vimwiki, I later found out about <a href="https://joplin.cozic.net">Joplin</a>, which comes with many great features and characteristics such as:

- Free & Open Source
- Manages notes and todo lists
- Search across all notes/todos
- Import/Export from/to various formats, including Markdown and even imports from Evernote
- Support for attachments
- Tags
- Synchronization with multiple providers such as Dropbox, Nextcloud, OneDrive and even your own private cloud
- Available for Windows, Linux, macOS, Android and iOS
- Web Clipper integration

This application left me a great first impression to say the least and I will make sure to stay up to date on its active development, which you can <a href="https://github.com/laurent22/joplin">follow on GitHub <i class="fab fa-github"></i></a>.

----

## Why did Vimwiki win in the end?

### In short
> The modal nature of Vim makes it very hard to enjoy any other text editor once you get used to it. The learning curve is quite considerable and nearly infinite, but this is also why I think it is worth investing more time to master it as it has proven to be an everlasting piece of trusty software <i class="fas fa-thumbs-up"></i>.

> There is a feature in Boostnote to set the Editor Keymap to `vim` so that you can edit text in a very similar way, but then you miss out on Vim's `Command mode` which adds tremendous extensibility and the ability to create any mappings you wish on the fly.

---

#### Expanded edition

Boostnote comes with nice features such as Tags, the ability to set multiple storage locations for notes, a `Preferences` panel to adjust many options, a feature to add code snippets, real-time preview of Markdown being edited, etc. Make no mistake: this is a great program. But there are many Vim features that are hard or impossible to replicate and everything that you can do in Boostnote can be done in Vim also (ctags, emmet syntax, plugins for Markdown, etc.).

- For starters, the terminal integration is obviously unmatched. In Vim, `CTRL+Z` will _stop_ Vim and gives you access to the terminal to do whatever you want to do. From that point, you can simply switch back to Vim by issuing the command `fg`. The terminal integration goes even further: you can have full access to the terminal inside Vim buffers since Vim 8.1 and that is a feature that has been available in Neovim for even longer.

- Even though `vim` mode can be enabled to edit text, you have to use the mouse to get many tasks done and the editing window can loose the focus. On the other hand, Vim is just one single window by default that you can split however you want, including adding tabs if your heart tells you to.

- You have to open your notes with Boostnote if you want them to be fully readable out of the box. Vimwiki does almost no processing with the content of the files so that it is very easy to open them with any other text editor. On a related note, it is much easier to export many notes at the same time with Vimwiki. Boostnote does have a few options to export individual notes (`.md`, `.txt`, `.html` and print), but it is not as user-friendly with many notes.

- Vimwiki makes it easy to link notes together and navigate between them, even within subfolders: highlight text, press `Enter` to create a link and open a new note, write your note and press `Backspace` to go back to where you created the link. That's quick and easy!

----

## Conclusion

In the end, it is a matter of taste as those programs are indeed very distinct. Boostnote has a polished interface, is much easier to use and has many settings easily changed. Vim/Neovim, on the contrary, requires a lot of initial effort both to understand and to set up according to your needs, but it does deliver a good dose of productivity... Eventually <i class="fas fa-laugh-beam"></i>!

An honorable mention goes to Simplenote, which is a joy to use with mobile devices and allows for quick synchronization between different devices across all the supported platforms.

Where things really get in favor of Vim, you could mention the extensive help system (command `:help`), the use of macros, words and lines completion, the dot (`.`) command, the many registers at your disposal for different tasks, the impressive amount of plugins available, the ways in which you can configure mappings, functions... But that's for a whole new story!
