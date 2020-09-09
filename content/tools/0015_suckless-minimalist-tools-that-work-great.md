Title: Suckless: Minimalist Tools That Work Great
Date: 2019-05-12 22:50
Tags: productivity, software, web
Slug: suckless-minimalist-tools-that-work-great
Authors: Sébastien Lavoie
Summary: I have been using a few different tools from [suckless.org](https://suckless.org/) for a while and I must say that once everything is configured properly, they are a joy to use. Some tools, like **dmenu** and **slock**, seem simple on the surface, but they allow to simplify your workflow by quite a bit. Another one, **st**, is a truly fantastic and lightweight terminal!
Description: I have been using a few different tools from suckless.org for a while and I must say that once everything is configured properly, they are a joy to use. Some tools, like dmenu and slock, seem simple on the surface, but they allow to simplify your workflow by quite a bit. Another one, st, is a truly fantastic and lightweight terminal!

[TOC]

---

## What are Suckless tools?

From the [official website](https://suckless.org/):

> Home of [dwm](https://dwm.suckless.org/),
> [dmenu](https://tools.suckless.org/dmenu) and other quality software
> with a focus on simplicity, clarity, and frugality.

There are also other incredible pieces of software that are worth
mentioning, including [st](https://st.suckless.org/).

Here, I will only go over the tools I use frequently, but keep in mind
that everything from Suckless... Sucks less.

---

## st — Simple Terminal

I did not know what to expect from this terminal and I found it delivers what I need! Configuring it is quite different than other terminals like [Konsole](https://konsole.kde.org/) or [GNOME Terminal](https://help.gnome.org/users/gnome-terminal/stable/): you just edit a text file and compile the software before you can even use it. It may seem tedious at first, but compiling such a small piece of software is very fast and it needs to be done on seldom occasions when you may want to adjust a setting.

I have experienced rendering issues when scaling the text with other terminals (including Konsole), where some weird flickering would happen at certain font sizes. [Simple Terminal](https://st.suckless.org/) just works without hassle. It doesn't have much bells and whistles out of the box, but it can be _patched_ to extend its functionality if you know what you are doing. I don't, so my compiled version remains pretty basic although I must say I like the simplicity of it very much.

### Configuration

I didn't have to adapt the configuration file very much. I ended up changing mainly the following lines:

```{.cpp}
static char *font = "Consolas:pixelsize=18:antialias=true:autohint=true";

static char *shell = "/bin/zsh";

/* Terminal colors (16 first used in escape sequence) */
static const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#1c1c1c", /* black   */
  [1] = "#ff005b", /* red     */
  [2] = "#70e502", /* green   */
  [3] = "#fcdd11", /* yellow  */
  [4] = "#00a0ea", /* blue    */
  [5] = "#bd1efc", /* magenta */
  [6] = "#14ecfc", /* cyan    */
  [7] = "#ededed", /* white   */

  /* 8 bright colors */
  [8]  = "#666666", /* black   */
  [9]  = "#ff00a0", /* red     */
  [10] = "#5dff00", /* green   */
  [11] = "#ff9f00", /* yellow  */
  [12] = "#71a9fc", /* blue    */
  [13] = "#d571fc", /* magenta */
  [14] = "#6cf2fc", /* cyan    */
  [15] = "#fcfcfc", /* white   */

  /* special colors */
  [256] = "#0a0500", /* background */
  [257] = "#e0e0e0", /* foreground */
};

/*
 * Default colors (colorname index)
 * foreground, background, cursor
 */
unsigned int defaultfg = 257;
unsigned int defaultbg = 256;
static unsigned int defaultcs = 257;
static unsigned int defaultrcs = 256;

/*
 * Colors used, when the specific fg == defaultfg. So in reverse mode this
 * will reverse too. Another logic would only make the simple feature too
 * complex.
 */
static unsigned int defaultitalic = 7;
static unsigned int defaultunderline = 7;

/*
 * Default shape of cursor
 * 2: Block ("█")
 * 4: Underline ("_")
 * 6: Bar ("|")
 * 7: Snowman ("☃")
 */
static unsigned int cursorshape = 2;

/*
 * Default columns and rows numbers
 */

static unsigned int cols = 80;
static unsigned int rows = 24;
```

## dmenu

[dmenu](https://tools.suckless.org/dmenu/) can be configured in the same way as Simple Terminal by editing a text file and compiling the software. I like to use many keyboard shortcuts, but I find that for launching applications I don't use that often or to launch custom Bash or Python scripts on the fly, nothing beats the simplicity of **dmenu**.

### Configuration

This one is very easy to configure and doesn't really require any attention at all besides defining where you want it to appear on the screen and what colors you prefer. Here are some smalls changes I made to the configuration in `config.h` before compiling it:

```{.cpp}
static int topbar = 1;                      /* -b  option; if 0, dmenu appears at bottom     */
/* -fn option overrides fonts[0]; default X11 font or font set */
static const char *fonts[] = {
	"Consolas:size=12"
};
static const char *prompt      = NULL;      /* -p  option; prompt to the left of input field */
static const char *colors[SchemeLast][2] = {
	/*     fg         bg       */
	[SchemeNorm] = { "#D8D8D8", "#000000" },
	[SchemeSel] = { "#000000", "#ff7400" },
	[SchemeOut] = { "#000000", "#00ffff" },
};
/* -l option; if nonzero, dmenu uses vertical list with given number of lines */
static unsigned int lines      = 0;

/*
 * Characters not considered part of a word while deleting words
 * for example: " /?\"&[]"
 */
static const char worddelimiters[] = " ";
```

## slock

What can be said about slock? It just works and never gets in your way. Set it and really forget it. From the official page:

> This is the simplest X screen locker we are aware of.

Again, its simplicity is charming and nothing really needs to be changed in `config.h` apart from colors and setting the correct username and group name to lock and unlock the screen.

---

## Conclusion

This was a lighting fast overview of some of the tools I now use on a daily basis. Suckless tools caught my attention and kept it! They offer other specialized software like a web browser, a tool for presentation from the terminal, IRC client and others... but the ones described here are really those which I now can't live without.

I was originally inspired to seek out those tools thanks to [Luke Smith](https://lukesmith.xyz/), a [fantastic YouTuber](https://www.youtube.com/channel/UC2eYFnH61tmytImy1mTYvhA).
