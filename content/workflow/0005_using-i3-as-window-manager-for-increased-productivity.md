Title: Using i3 as a Window Manager for Increased Productivity
Date: 2019-01-08 11:12
Modified: 2019-01-08 18:48
Tags: productivity, window-manager
Slug: using-i3-as-a-window-manager-for-increased-productivity
Authors: Sébastien Lavoie
Summary: I was striving to improve my productivity as one of my New Year's resolutions and finally found the courage to take the time to try out i3, a fantastic window manager.

## What is i3?

[i3](https://i3wm.org/) is a tiling window manager.  To get to know `i3` better, it's good to situate what desktop environments are in the first place.

----

### What are desktop environments?

If you are familiar with Linux <i class="fab fa-linux"></i>, you certainly know about desktop environments such as [GNOME](https://www.gnome.org/), [KDE](https://www.kde.org/), [Xfce](https://www.xfce.org/)... and actually many more are available (you can see [this article on Wikipedia](https://en.wikipedia.org/wiki/Desktop_environment) <i class="fab fa-wikipedia-w"></i> for an extended selection)! The classic Graphical User Interface (GUI) on Windows XP was known as [Luna](https://en.wikipedia.org/wiki/Luna_(theme)) <i class="fab fa-wikipedia-w"></i> and is now called Modern on Windows 10. [Aqua](https://en.wikipedia.org/wiki/Aqua_(user_interface)) <i class="fab fa-wikipedia-w"></i> is the name of the GUI on MacOS. Well, every desktop environment comes with a window manager, the main component that makes interactions with windows possible, like moving, resizing, minimizing or closing them.

Desktop environments are very useful in many ways:

- They are usually very easy to set up as they come fully functional out of the box. Like opening a user session on MacOS or Windows.
- They are sometimes quite customizable, but you don't have to change anything to get them to work, as they normally set default applications to open with certain file types.
- They automatically integrate services such as WiFi network detection, automatic mounting of drives when you plug them in, etc.
- You can enable [virtual desktops](https://en.wikipedia.org/wiki/Virtual_desktop) <i class="fab fa-wikipedia-w"></i> to split your work across different spaces. This concept can grow to _[Activities](https://docs.kde.org/trunk5/en/kde-workspace/plasma-desktop/activities-interface.html)_, which is a feature implemented in KDE that allows you to use virtual spaces literally for different activities by having settings that are specific to each activity (like launching one application or keeping widgets in determined positions), plus the ability to use multiple virtual desktops inside each _activity_.
- They integrate with applications that are specifically designed to take advantage of the desktop environment in question by adapting colors and themes perfectly to match the general look of the system and arranging settings in a common location for all applications.

----

### Why use a window manager like i3?

Even though desktop environments are user-friendly and include many goodies, they do have several disadvantages that make window managers great alternatives <i class="fas fa-thumbs-up"></i>.

#### Less bloated

Desktop environments are often bloated with many applications that you may not need but that are nevertheless occupying system resources as they have many dependencies. For example, if you use [Thunderbird](https://www.thunderbird.net) for managing your emails and your desktop environment is GNOME, try to remove Evolution, the default application for emails that comes with it... It's still relatively easy to disable its processes, but you sometimes have to configure files manually to satisfy your need for removing clutter.

#### Lower memory and CPU consumption

Other than coming with a set of default applications (more disk space), the whole environment occupies a lot more memory to run smoothly. On my modest laptop, I was still experiencing speed issues because the system was occupying too much RAM when opening heavy applications (lots of tabs when web browsing, photo editing, loading IDEs like PyCharm for programming, etc.) and I had 4 GB of RAM installed at the time. KDE requires at least 600 MB, same is true for GNOME in most recent versions (but used to be over 1 GB not very long ago, just like for KDE). Windows, for example, requires more than 1.5 GB of RAM to operate with basic features. **`i3`** needs less than **~15 MB** with as many windows and spaces open as you would ever want. Since there are much less processes to take care of, CPU consumption is also lower, which is more noticeable on older machines.

#### Keyboard efficiency

There are obviously ways to go about using keyboard shortcuts for pretty much anything you want with desktop environments. However, window managers and especially `i3` make this a must, as there is really no reason to use a mouse for moving windows.

First of all, windows are "stuck" in place and never overlap by default. You can't move them around with a mouse unless they are "floating" windows, which means you can separate them to move them around freely like in most desktop environments. The whole point of using a window manager like `i3` is to maximize screen space, so every window opens in full screen. Honestly, the only time I ever found the need to use a floating window with `i3` is when using the operating system Windows in a virtual environment when connecting through RDP with Google Chrome on Google Cloud Platform (that is, not very often). Other than that, I find it very practical to split the screen with no overlapping windows, even with my small 15 inches screen.

Because windows are managed the way they are in `i3`, getting split when multiple windows are in the same workspace and never overlapping, it nurtures the good habit of dividing workspaces appropriately to maximize the space that each application occupies, which is done with keyboard shortcuts. With (customizable) shortcuts, you can split windows, move them to other workspaces, change workspaces, open applications automatically in specific workspaces, etc. Using exclusively the keyboard to manage the windows becomes a huge time saver, and even more so when considering the very small footprint required to use the window manager, making for a lightning fast experience.

#### Extremely fast customization

Once you get past the initial lack of visual appeal and weird way to move around, you can actually customize many aspects of `i3`, including fonts, mouse bindings, window border decorations, colors, automatic execution of apps when initiating a session, etc.

Why is it so fast to customize? Because the configuration is all contained in one simple text file and you can make a change and reload the window manager on the fly to see your changes being reflected. Setting the number of workspaces is as easy as adding or removing a line (well, as a bare minimum, otherwise it's useful to also bind certain keyboard shortcuts to move to those newly created workspaces). Setting a wallpaper is one line, setting a screen lock is another one. Quick and efficient.

#### Easy to switch layouts and focus

I actually enjoy the default layout quite a lot, in which there exists no overlap between windows (they split as needed) and all windows are visible at the same time in each workspace. If you need to make more space for a window, you can either "focus" on the current window, which will make it full screen and cover every pixel of the screen, or you can move particular windows to other workspaces. This last option will automatically resize windows so that they occupy the maximum space available.

Besides the default layout, you can also _stack_ and _tab_ windows, depending on how you like to work (it is well worth having a look at the [i3 user's guide](https://i3wm.org/docs/userguide.html) to see the many other features available). Personally, I prefer seeing everything at once and dividing my work into many workspaces. If you are curious, here is how I currently have my workspaces set up:

1. **Programming** — Exclusively for programming purposes.
2. **Terminals** — For working in the terminal, opening another instance of a terminal text editor, etc.
3. **Web** — Just for Internet. Always full screen unless I open some website that requires to open new windows (like banking), which conveniently split the windows. The web browser automatically launches in the background when opening a session in `i3`.
4. **Multimedia** — Editing photos or watching videos.
5. **Music** — [ncmpcpp](https://github.com/arybczak/ncmpcpp) (terminal music player) automatically launches in the background when opening a session.
6. **Experiments** — I use this workspace when trying to understand some programming concepts with an interactive IPython console or for breaking the system in one way or another because I don't know what I'm doing.
7. **Fix** — After realizing that sometimes experiments need to be cleaned up a bit, I now use this workspace exclusively to run tools in the background, such as [BleachBit](https://www.bleachbit.org) for cleaning files or [glances](https://nicolargo.github.io/glances/) (similar to the `top` command) for watching how the system is doing.
8. **Words** — I use that workspace for reading e-books or for writing, either in [Neovim](https://neovim.io/) or [LibreOffice](https://www.libreoffice.org/) depending on the task.
9. **Tools** — This workspace is reserved for anything that I might want to have access to once in a while, like a calendar or [KeepassXC](https://keepassxc.org/) for accessing a password database.
10. **sg** — I mainly use that workspace to update this very website, but I also use it for setting up local web servers for making personal projects in [Flask](http://flask.pocoo.org/) and [Django](https://www.djangoproject.com/) or even just a temporary server with `python -m http.server` to share files with other devices on the local network.

Only workspaces that contain windows will appear on the screen at any given time and are automatically created when you access and use them.

----

## What does it look like in action?

Here is a screenshot\* of the workspace where this article is being written (click to open):

<a href="{static}/images/posts/0005_using-i3-as-window-manager-for-increased-productivity/i3-example.png"><img src="{static}/images/posts/0005_using-i3-as-window-manager-for-increased-productivity/i3-example.png" class="max-size-img-post"></a>

\* <sub>In this particular scenario, the splits on the right side are intentionally very small as I do not need to read the output, but need quick access to a terminal to enter commands. Moving back and forth between windows is a breeze, so that's how I currently handle the situation.</sub> 

**Note**: With <code>Neovim</code>, there is an embedded terminal, which makes things very easy to handle by avoiding splits altogether. In that case, it is also possible to divide a workflow with tabs inside <code>Neovim</code> instead of physically splitting windows.


----

## Conclusion

I am not trying to convince myself anymore: I really prefer this workflow <i class="fas fa-grin-hearts"></i>! If you are looking for a change and would like to maximize both your productivity and your system resources, `i3` is a great window manager to consider. It doesn't seem very intuitive at first, but I swear it quickly becomes easy to use and you also end up learning more about how Linux works and set things up manually (just once!) to your likings. For example, I use Rofi instead of dmenu to have a window pop-up to select applications or switch to any window on any workspace... which was only one line to modify in the configuration file.

I have found the following screencasts on YouTube to be quite useful in learning how to configure `i3` (apart from the official documentation which is very comprehensive):

- [i3wm: Jump Start (1/3)](https://www.youtube.com/watch?v=j1I63wGcvU4)
- [i3wm: Configuration (2/3)](https://www.youtube.com/watch?v=8-S0cWnLBKg)
- [i3wm: How To "Rice" Your Desktop (3/3)](https://www.youtube.com/watch?v=ARKIwOlazKI)
