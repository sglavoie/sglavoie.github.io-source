Title: A Guided Tour of an i3 Configuration
Date: 2020-08-15 10:51
Modified: 2020-08-16 15:05
Slug: a-guided-tour-of-an-i3-configuration
Tags: i3, window-manager
Authors: Sébastien Lavoie
Summary: This article will go over my dear i3 configuration file, which contains quite a few sections I hope I had stumbled upon right from the start when I got introduced to the tiling window manager world. It would probably have been less scary and intimidating. May you find the shortcut you needed!
Description: This article will go over my dear i3 configuration file, which contains quite a few sections I hope I had stumbled upon right from the start when I got introduced to the tiling window manager world. It would probably have been less scary and intimidating. May you find the shortcut you needed!

# Introduction

In [Using i3 as a Window Manager for Increased Productivity](https://www.sglavoie.com/posts/2019/01/08/using-i3-as-a-window-manager-for-increased-productivity/), a number of reasons were given to get going with this fantastic tiling window manager. Now, it's time to jump in and explore how to actually use i3! If you're looking for an in-depth guide, the [official i3 documentation](https://i3wm.org/docs/userguide.html) or the [i3 page on the Arch Wiki](https://wiki.archlinux.org/index.php/i3) are awesome resources to dive deeper. Here, we'll focus on day-to-day usage based on my current configuration file which I have used and refined over the past two years or so. I hope that you'll be able to glean useful tips and tricks to apply to your own use case.

---

## The Configuration File

To set keybindings, it _may_ be handy to know the keycodes and their respective names. To get a full list, you can use `xmodmap -pk` in the terminal. If you're not sure of the name of the key you want to press (is it "PageDown", "PageDwn" or "Next"?), you can retrieve it by executing the `xev` command, which will open two windows: one for capturing the actual key press and the other one to display the relevant details for that key. For example, if you press the backspace key, the output will contain something like `keycode 22 (keysym 0xff08, BackSpace)`. From there, you will know that a mapping would be of the form `mod+BackSpace`, where `mod` is the modifier of your choice that is usually specified at the top of the configuration file. Now we can start!

### General settings

```{.bash}
# set mod key (Mod1=Alt, Mod4=Super)
# ⇒ the main modifier used to trigger shortcuts
set $mod Mod4

# font for window titles
# ⇒ this is what you see in your i3bar
font xft:JetBrainsMono-Regular 12

# launch a terminal
bindsym $mod+Return     exec alacritty

# kill focused window
# ⇒ usual way to close applications
bindsym $mod+x          kill

# reload the configuration file
# ⇒ apply changes from this file on the fly
bindsym $mod+Shift+c    reload

# restart i3 inplace
# ⇒ preserves your layout/session, can be used when upgrading i3
bindsym $mod+Shift+r    restart

# exit i3
# ⇒ logs you out of your X session
bindsym $mod+Shift+e    exec --no-startup-id i3-msg exit

# set shut down, restart and locking features
# ⇒ type `$mod+Shift+Delete` then either `e`, `r` or `s`
bindsym $mod+Shift+Delete   mode "$mode_system"
set $mode_system (e)xit, (r)eboot, (s)hutdown
mode "$mode_system" {
    bindsym e    exec --no-startup-id i3-msg exit
    bindsym r    exec --no-startup-id systemctl reboot
    bindsym s    exec --no-startup-id systemctl poweroff

    # exit system mode with "Enter" or "Escape"
    bindsym Return mode "default"
    bindsym Escape mode "default"
}

# shut down the system without confirmation
# ⇒ this shortcut is hard to trigger with one hand on purpose!
bindsym $mod+Shift+Escape exec --no-startup-id systemctl poweroff

# resize windows
# you can also use the mouse for that:
# for tiled windows ⇒
  # drag the border with LeftClick or RightClick
# for floating windows ⇒
  # `mod + RightClick`, then drag

# resize with smaller steps to get more control
bindsym $mod+r mode "resize"
mode "resize" {
        bindsym h resize shrink width 2 px or 2 ppt
        bindsym j resize grow height 2 px or 2 ppt
        bindsym k resize shrink height 2 px or 2 ppt
        bindsym l resize grow width 2 px or 2 ppt

        # exit resize mode: Enter or Escape
        bindsym Return mode "default"
        bindsym Escape mode "default"
}

# resize without entering "resize mode"
# ⇒ I find this more convenient. I usually don't care about
# precise window sizes, so here the steps are far greater.
# If I want more control, then entering resize mode will do.
bindsym $mod+Control+l resize shrink width 10 px or 10 ppt
bindsym $mod+Control+k resize grow height 10 px or 10 ppt
bindsym $mod+Control+j resize shrink height 10 px or 10 ppt
bindsym $mod+Control+h resize grow width 10 px or 10 ppt

# lock the screen with a black color background
bindsym $mod+Delete    exec --no-startup-id i3lock -c 000000

# hide/unhide i3status bar (applies to all monitors)
bindsym $mod+m    bar mode toggle
```

A few notes on the **General settings**:

- I use `Alt` in a few applications and reserve `Super` for the window manager only.
- Find the font name you need with `fc-list`. For instance, to use JetBrains' font: `fc-list | grep Jet`.
- Resizing and moving floating windows with the mouse also works great: `mod+LeftClick` to move around and `mod+RightClick` to resize. This way, it's also possible to move windows to other screens.

### Navigation

_Note_: I rely on Vim keybindings to move between containers and workspaces as I find the position of those keys on the home row really comfortable to apply to the main window actions one would want to execute.

```{.bash}
# Set up monitor at launch automatically and set laptop screen as the
# primary one. Set monitor to the top (being on the vertical axis
# makes it possible to focus bottom/top and jump from one monitor to
# the next, which is not possible if the monitor is set to top-left or
# top-right in diagonal, for instance)
exec_always xrandr --output eDP --primary --mode 1920x1080 --pos 0x1080 \
    --rotate normal --output HDMI-A-0 --mode 1920x1080 --pos 0x0 --rotate normal \
    --output DisplayPort-0 --off --output DisplayPort-1 --off

# container focuses where the mouse is (yes/no)
focus_follows_mouse    no

# go to last urgent workspace
# ⇒ this is the worspace that turns "red" by default when something happens
#   in an unfocused workspace, like an application pop-up
bindsym $mod+u    [urgent=latest] focus

# change focus
# ⇒ works in all modes: tabbed, stacked, etc.
bindsym $mod+h    focus left
bindsym $mod+j    focus down
bindsym $mod+k    focus up
bindsym $mod+Down focus down
bindsym $mod+Up   focus up
bindsym $mod+l    focus right

# move focused window (works in all modes)
bindsym $mod+Shift+h    move left
bindsym $mod+Shift+j    move down
bindsym $mod+Shift+k    move up
bindsym $mod+Shift+l    move right

# for example, switching from workspace 1 to workspace 2 (e.g. mod+2) then
# typing again mod+2 would bring you back to workspace 1 without having to
# remember that you came from workspace 1 in the first place.
workspace_auto_back_and_forth    no

# alternate between the last two workspaces that have been used
bindsym $mod+Tab    workspace back_and_forth

# move a container (window or group of windows if you grouped them) to the
# "alternate" workspace you visited last
# (the one brought with $mod+Tab in this case)
bindsym $mod+Shift+Tab           move container to workspace back_and_forth; \
                                 workspace back_and_forth

# switch to any window with Rofi
# ⇒ this simulates the familiar behavior of Alt+Tab on Windows and allows you
#   to find windows by typing, but uses a better operating system to do it ;).
bindsym Mod1+Tab    exec "rofi -theme Arc-Dark -font 'JetBrainsMono 14' \
                    -show-icons -width 90 -show window"

# toggle fullscreen mode for the focused container
# ⇒ this hides the i3bar for the current monitor
# ⇒ you can still leave the i3bar hidden and switch to other workspaces
bindsym $mod+f    fullscreen toggle

# navigate workspaces next / previous
# ⇒ works for all monitors and will go in increasing order
#   if workspaces 1 to 6 are on monitorX and workspaces
#   7 to 10 are on monitorY as in this config, this will switch
#   to any workspace where there is at least one container
bindsym $mod+Mod1+l         workspace next
bindsym $mod+Mod1+h         workspace prev
bindsym $mod+Shift+Right    workspace next
bindsym $mod+Shift+Left     workspace prev

# the difference with the above is that it limits movements to the
# the current monitor only
bindsym $mod+Right          workspace next_on_output
bindsym $mod+Mod1+Tab       workspace next_on_output
bindsym $mod+Left           workspace prev_on_output

# Bindings to "mark" and "goto" mark specified with 1 character
# ⇒ rarely used, but can still be useful if you have many containers open
bindsym $mod+z    exec i3-input -F 'mark %s' -l 1 -P 'Mark: '
bindsym $mod+g    exec i3-input -F '[con_mark="%s"] focus' -l 1 -P 'Goto: '

# Workspace names — can be customized with emojis and names
# ⇒ I find I like minimalism best and just mentally associate
#   one workspace number with a specific type of task
# ⇒ those are set across all monitors
set $ws1  "1"
set $ws2  "2"
set $ws3  "3"
set $ws4  "4"
set $ws5  "5"
set $ws6  "6"
set $ws7  "7"
set $ws8  "8"
set $ws9  "9"
set $ws10 "10"

# switch to workspace (no matter which monitor it is set to)
bindsym $mod+1    workspace $ws1
bindsym $mod+2    workspace $ws2
bindsym $mod+3    workspace $ws3
bindsym $mod+4    workspace $ws4
bindsym $mod+5    workspace $ws5
bindsym $mod+6    workspace $ws6
bindsym $mod+7    workspace $ws7
bindsym $mod+8    workspace $ws8
bindsym $mod+9    workspace $ws9
bindsym $mod+0    workspace $ws10

# determine which workspace appears on which screen
# ⇒ with a single output screen, this is not necessary
workspace 1  output HDMI-A-0
workspace 2  output HDMI-A-0
workspace 3  output HDMI-A-0
workspace 4  output HDMI-A-0
workspace 5  output HDMI-A-0
workspace 6  output HDMI-A-0
workspace 7  output eDP
workspace 8  output eDP
workspace 9  output eDP
workspace 10 output eDP

# move focused container to workspace and switch to workspace
bindsym $mod+Shift+1    move container to workspace $ws1;  workspace $ws1
bindsym $mod+Shift+2    move container to workspace $ws2;  workspace $ws2
bindsym $mod+Shift+3    move container to workspace $ws3;  workspace $ws3
bindsym $mod+Shift+4    move container to workspace $ws4;  workspace $ws4
bindsym $mod+Shift+5    move container to workspace $ws5;  workspace $ws5
bindsym $mod+Shift+6    move container to workspace $ws6;  workspace $ws6
bindsym $mod+Shift+7    move container to workspace $ws7;  workspace $ws7
bindsym $mod+Shift+8    move container to workspace $ws8;  workspace $ws8
bindsym $mod+Shift+9    move container to workspace $ws9;  workspace $ws9
bindsym $mod+Shift+0    move container to workspace $ws10; workspace $ws10
```

A few notes on the **Navigation** section:

- I like to keep the number of workspaces to 10 because the number row is easily accessible and there's less context switching involved.
- I also like to keep a higher number of workspaces on the main screen I work on as I can use `mod+Left` and `mod+Right` to switch focus on that screen only. This is usually to keep a reference opened on the other screen, like server logs or the [Todoist Linux](https://github.com/KryDos/todoist-linux) app.
- Those keybindings make it really easy to navigate between workspaces on one particular screen. Even though I like to work with a monitor being higher than the laptop located in front of it to avoid working in a twisted position at all times, this would work fantastically well in the horizontal direction too.
- If for whatever reason the main screen is disconnected (power outage or unplugged), I can still use the laptop screen without needing to modify the config file, although with a slightly more limited amount of workspaces. _Tip_: even if you don't see a workspace from a temporarily disconnected screen, you can still interact with it and bring windows back to workspaces that you can see without changing the config file.

### Layout

```{.bash}
# set default desktop layout (default is tiling), <stacking|tabbed>
workspace_layout    tabbed

# change container layout (stacked, tabbed, toggle split)
bindsym $mod+s    layout stacking
bindsym $mod+w    layout tabbed
bindsym $mod+e    layout toggle split

#start in opposite orientation from your monitor
default_orientation    vertical

#toggles split at each new window (Fibonnaci layout)
# for_window [class=".*"]    split toggle

# toggle the way a split happens in the focused window
bindsym $mod+t    split toggle

# toggle tiling / floating
# ⇒ this works on a container with any number of windows!
#   if you select multiple windows with `$mod+a` (see below)
#   to group them and then toggle them, the whole group will
#   either tile or float
bindsym $mod+Shift+space    floating toggle

# change focus between tiling / floating windows
# ⇒ If you leave a floating window on top of other tiled windows,
#   you can switch the focus from the one on top to the one(s) in
#   the background (useful with apps like Zoom or Google Meet that
#   you want to keep in the foreground)
bindsym $mod+space    focus mode_toggle

# Use Mouse+$mod to drag floating windows
floating_modifier    $mod

# toggle sticky
bindsym $mod+Shift+s    sticky toggle

# focus the surrounding containers
bindsym $mod+a    focus parent
bindsym $mod+c    focus child
```

A few notes on the **Layout** section:

- To maximize the size of applications, I prefer using the "tabbed" mode, which is more compact than the stacking mode. If I quickly want to split windows side-by-side, I just type `mod+e` to toggle split vertically by default and if I need a horizontal split, I just toggle again with `mod+e`.
- I don't use the "grouping" feature with `mod+a` and `mod+c` very often, but when I need to move a few windows to another workspace for instance, that's quite handy!
- A floating window in "sticky mode" will follow you on all your workspaces and remember that this mode is enabled even if you put in back in a tiling window and then to a floating   window again.

### Scratchpad

The scratchpad is sometimes so useful that it deserves its own section! When you send a window to the "scratchpad", it disappears. Then, with a keybinding, you can bring in back in floating mode on top of any other window on any active workspace you happen to be in. The same keybinding will toggle on/off the display of that scratchpad and if you happen to have sent multiple windows to the scratchpad, activating the same keybinding again will cycle through all the "scratchpads".

I often use that for an audio player I leave running in the background and instead of using a whole workspace to leave that window opened, I send it to the scratchpad, which means it doesn't take any space and I can quickly bring it back in focus whenever I want. I find that having more than two windows in the list of scratchpads becomes cumbersome as you cycle through them, so I keep the scratchpad for specific, infrequent uses for applications that require less attention.

If you want to convert a scratchpad back to a regular tiled container, it's as easy as triggering "toggle tiling / floating" (in this config file, it happens with `mod+Shift+space`).

```{.bash}
# Move the currently focused window to the scratchpad
bindsym $mod+minus    move scratchpad

# Show the next scratchpad window or hide the focused scratchpad window.
# If there are multiple scratchpad windows, this command cycles through them.
bindsym $mod+plus    scratchpad show, resize set 1900 1000, move position center
```
A note on the **Scratchpad** section:

- In my setup, I have two screens with the same resolution of 1920x1080, so the same "resize" command works on both screens. You might want to use two different keybindings if you want to bring a scratchpad back to a screen with a different resolution.

### Borders

```{.bash}
# Configure border style <normal|1pixel|pixel xx|none|pixel>
new_window pixel 3
new_float normal
default_floating_border pixel 3

# Hide borders
hide_edge_borders smart

# change borders
bindsym $mod+b    border none
bindsym $mod+y    border pixel 3
bindsym $mod+n    border normal
```

A few notes on the **Borders** section:

- I just **love** knowing which container is active, so I set thick, bright borders with a nice kind of "electric blue" color that's easy to spot on a light or dark background (colors are set below in the section **Colors & theming**).
- I also **love** saving space whenever possible to see more stuff on the screen, so I avoid gaps altogether (if you like them, have a look at [i3-gaps](https://github.com/Airblader/i3)). In that spirit, I also set the option `hide_edge_borders smart` so that borders don't show up when I have only one tiled container covering the whole space.
- This also shows that you can have a different border size for floating windows if you find the thickness distracting. Personally, I just find it helps me know which container is active when I toggle from foreground to background window with `mod+space`.

<figure>
    <a href="{static}/images/posts/0022_guided-tour-i3/demo_dark_light_background_thick_border.png"><img src="{static}/images/posts/0022_guided-tour-i3/demo_dark_light_background_thick_border.png" alt="demo_dark_light_background_thick_border_i3" class="max-size-img-post"></a>
    <figcaption>Bashtop on the left with a dark background, LibreOffice on the right with a light background, Neofetch floating window on top featuring a thick, blue border.</figcaption>
</figure>


### dmenu

`dmenu` is so useful that it also got its own section. By default, you usually launch applications with `mod+d`: I kept the same behavior here. I added a few custom launchers that I use all the time to open files based on a topic, using mnemonics that work (for me, at least). If you want to know more about setting these kinds of shortcuts, you may be interested in reading [Using dmenu to Optimize Common Tasks](https://www.sglavoie.com/posts/2019/11/10/using-dmenu-to-optimize-common-tasks/) ;).

```{.bash}
bindsym $mod+Mod1+c    exec --no-startup-id ~/Dropbox/.custom/dmenu/cheatsheets.sh
bindsym $mod+Mod1+d    exec --no-startup-id ~/Dropbox/.custom/dmenu/documents.sh
bindsym $mod+Mod1+e    exec --no-startup-id ~/Dropbox/.custom/dmenu/edit_scripts.sh
bindsym $mod+Mod1+f    exec --no-startup-id ~/Dropbox/.custom/dmenu/filepaths.sh
bindsym $mod+Mod1+q    exec --no-startup-id ~/Dropbox/.custom/dmenu/quotes.sh
bindsym $mod+Mod1+r    exec --no-startup-id ~/Dropbox/.custom/dmenu/reading.sh
bindsym $mod+Mod1+s    exec --no-startup-id ~/Dropbox/.custom/dmenu/scripts.sh
bindsym $mod+Mod1+u    exec --no-startup-id ~/Dropbox/.custom/dmenu/university.sh
bindsym $mod+Mod1+w    exec --no-startup-id ~/Dropbox/.custom/dmenu/work.sh
bindsym $mod+Shift+u   exec --no-startup-id ~/Dropbox/.custom/dmenu/university_launchers.sh
bindsym $mod+d         exec --no-startup-id ~/Dropbox/.custom/dmenu/software.sh
```

### Shortcuts

```{.bash}
bindsym $mod+control+r    exec --no-startup-id thunar ~/Desktop

# Simple calculator in terminal
bindsym $mod+masculine    exec alacritty -e bc

# Focus applications
bindsym $mod+q [class="Todoist"] focus

# Display multiple time zones around the world
bindsym $mod+Mod1+t    exec --no-startup-id ~/Dropbox/.custom/dmenu/times.sh
```

A few notes on the **Shortcuts** mini-section:

- In i3, you don't really make use of icons on the desktop. I like the absence of visual clutter it provides, but I sometimes like to access a specific folder in which I drop a few shortcuts/symlinks to access other files from there.
- `bc` is a nice minimalist calculator.
- Focusing applications is also a very cool use of shortcuts. In this case, I just leave Todoist running on a workspace and can quickly go back to it.
- _An idea for customization_: working remotely with many teammates from around the world is sometimes confusing timewise, so I have a simple script that outputs the current time in the places I'm interested in monitoring.

<figure>
    <a href="{static}/images/posts/0022_guided-tour-i3/timezones.png"><img src="{static}/images/posts/0022_guided-tour-i3/timezones.png" alt="timezones_dmenu" class="max-size-img-post"></a>
    <figcaption>Simple pop-up with a list of timezones.</figcaption>
</figure>

### Sound

```{.bash}
set $volumepath ~/.config/i3-volume/volume
set $statuscmd i3status

# Signal used to update the status line
set $statussig SIGUSR1

# Amount to increase/decrease volume as a percentage
set $volumestep 5

bindsym XF86AudioRaiseVolume    exec $volumepath -np -i $volumestep -t $statuscmd -u $statussig
bindsym XF86AudioLowerVolume    exec $volumepath -np -d $volumestep -t $statuscmd -u $statussig
bindsym XF86AudioMute           exec $volumepath -mn -t $statuscmd -u $statussig
bindsym XF86AudioMicMute        exec pactl set-source-mute alsa_input.pci-0000_03_00.6.analog-stereo toggle
```

This section will depend on the hardware being used, but it gives an idea of how to do things. I use [`i3-volume`](https://github.com/hastinbe/i3-volume) to get nice notifications when changing the volume and all the options being set here use `i3-volume`. Toggling the mic output was not super obvious at first, but it's obviously doable and it's good to know there's an `XF86Audio` property for that purpose!

### Brightness

```{.bash}
# Control brightness more precisely through software `light`
bindsym XF86MonBrightnessDown    exec "light -U 5"
bindsym XF86MonBrightnessUp      exec "light -A 5"

# Toggle laptop screen
bindsym $mod+Control+b    exec --no-startup-id ~/.local/bin/toggle_laptop_brightness
```

To control the screen brightness, I use [`light`](https://github.com/haikarainen/light). I also like to just toggle the brightness of my laptop at night when I read something on my external monitor, so I use a [`toggle_laptop_brightness`](https://github.com/sglavoie/dotfiles/blob/master/.local/bin/toggle_laptop_brightness) script that I found somewhere online and adapted slightly.

### Applications

This section will heavily depend on the software you use of course, but there's the gist of it. I like to have a shortcut for [bashtop](https://github.com/aristocratos/bashtop) to quickly monitor system resources ([glances](https://github.com/nicolargo/glances) is also quite nice). Besides that, I like to have applications automatically appear on specific workspaces and be switched to in some instances.

Controlling which application opens in floating mode is also useful as some just don't play that well with tiling. To find information about an application, you can open a new terminal window and launch `xprop`, click on the window you need information about and _voilà_, a couple of strings will be displayed like so (output truncated a bit):

```
	Icon (16 x 16):
	     ▒▓▓▓▓▒
	   ▒▓██████▓▒
	  ▒█▓▒░  ░▒▓█▒
	 ▒█▓░      ░▓█▒
	 ▓▓░  ░░░   ░▓▓
	▒█▒  ░███▓░  ▒█▒
	▓█░   ░░▓█▓  ░█▓
	▓█   ░▓▓██▓   █▓
	▓█   ▓█▒▓█▓   █▓
	▓█░  ▓█▓▓█▓  ░█▓
	▒█▒  ░▓▓▒▓▒  ▒█▒
	 ▓▓░        ░▓▓
	 ▒█▓░      ░▓█▒
	  ▒█▓▒░  ░▒▓█▒
	   ▒▓██████▓▒
	     ▒▓▓▓▓▒
WM_NORMAL_HINTS(WM_SIZE_HINTS):
		program specified location: 0, 0
		program specified minimum size: 627 by 279
		window gravity: NorthWest
WM_CLASS(STRING) = "audacious", "Audacious"
WM_ICON_NAME(STRING) = "47. David Bowie - Best Of Bowie - Heroes (3:36) - Audacious"
WM_NAME(STRING) = "47. David Bowie - Best Of Bowie - Heroes (3:36) - Audacious"
```

You may need to switch to tiling windows or make the terminal window that launches `xprop` a floating window to be able to click on the desired window. Here, we get an output for the Audacious music player. You usually need the second string from `WM_CLASS(STRING)` but if you don't want to mess with letter casing being upper vs lowercase, you can prefix with `(?i)` for "insensitive" as shown below and that will match any window containing that pattern. Sometimes, you're just after matching a "title" (like it's done with LibreOffice in the snippet of code below) and you can get that one by showing the container's border. With this config file, the `mod+n` keybinding will show the border you want at the top and `mod+y` will make it disappear again.

```{.bash}
# Start
bindsym $mod+BackSpace              exec alacritty -e bashtop
bindsym $mod+Print --release        exec --no-startup-id flameshot screen --path ~/Pictures/screenshots/
bindsym $mod+Shift+a                exec audacious
bindsym $mod+Shift+d --release      exec "killall dunst; exec notify-send 'restart dunst'"
bindsym $mod+Shift+g                exec gimp
bindsym $mod+Shift+i                exec inkscape
bindsym $mod+Shift+t                exec thunar
bindsym $mod+Shift+v                exec alacritty -e vifm
bindsym $mod+Shift+w                exec --no-startup-id google-chrome-stable
bindsym $mod+Shift+x --release      exec --no-startup-id xkill
bindsym Print --release             exec --no-startup-id flameshot gui --path ~/Pictures/screenshots/

# Open applications on specific workspaces
assign [class="(?i)code"]               $ws1
assign [class="(?i)brave-browser"]      $ws3
assign [class="(?i)firefox"]            $ws3
assign [class="(?i)google-chrome"]      $ws3
assign [class="(?i)scribus"]            $ws4
assign [class="Audacity"]               $ws4
assign [class="Gimp"]                   $ws4
assign [class="Inkscape"]               $ws4
assign [class="vlc"]                    $ws4
assign [class="(?i)org.gnome.Nautilus"] $ws5
assign [class="(?i)zathura"]            $ws6
assign [title="(?i)libreoffice"]        $ws7
assign [class="keepassxc"]              $ws8
assign [class="obs"]                    $ws8
assign [class="Transmission"]           $ws8

# Automatically switch to workspace when opening those
for_window [class="(?i)brave-browser"]      workspace $ws3
for_window [class="(?i)code"]               workspace $ws1
for_window [class="(?i)firefox"]            workspace $ws3
for_window [class="(?i)google-chrome"]      workspace $ws3
for_window [class="(?i)org.gnome.Nautilus"] workspace $ws5
for_window [class="(?i)scribus"]            workspace $ws4
for_window [class="(?i)zathura"]            workspace $ws6
for_window [class="Gimp"]                   workspace $ws4
for_window [class="Inkscape"]               workspace $ws4
for_window [class="Transmission"]           workspace $ws8
for_window [class="audacity"]               workspace $ws4
for_window [class="keepassxc"]              workspace $ws8
for_window [class="obs"]                    workspace $ws8
for_window [class="vlc"]                    workspace $ws4
for_window [title="(?i)libreoffice"]        workspace $ws7

# Open specific applications in floating mode
for_window [class="(?i)virtualbox"]   floating enable border pixel 2
for_window [class="GParted"]          floating enable border pixel 2
for_window [class="Lightdm-settings"] floating enable pixel 2
for_window [class="Lxappearance"]     floating enable sticky enable border pixel 2
for_window [class="Nitrogen"]         floating enable sticky enable border pixel 2
for_window [title="File Transfer*"]   floating enable border pixel 2
for_window [title="alsamixer"]        floating enable border pixel 2
for_window [class="(?i)zoom"]         floating enable border pixel 2

# Autostart applications
exec --no-startup-id    brightnessctl s 40%
exec --no-startup-id    google-chrome-stable
exec --no-startup-id    nitrogen --restore
exec --no-startup-id    nm-applet
exec --no-startup-id    pasystray
exec --no-startup-id    todoist
exec --no-startup-id    xfce4-clipman
exec --no-startup-id    unclutter --jitter 40 --ignore-scrolling &
exec --no-startup-id    compton -CG --config /dev/null
```
This last section on **Autostart applications** is the list of applications that launch when you open your X session with i3.

### Keyboard & mouse

```{.bash}
# Set compose key to Right Ctrl
exec_always --no-startup-id    setxkbmap -option "compose:rctrl"

# Delay, interval
exec_always --no-startup-id    xset r rate 250 60
```

I like to set those options in my config file as they can be modified on the fly if you reload i3. This is thanks to the `exec_always --no-startup-id` directive which will always run the invoked command when relaunching, not just when logging in to a session.

### Colors & theming

Of interest in this section, apart from the actual colors, is where you will set your i3bar on the screen (top vs bottom) and on which monitor your tray (the space with little icons to show the volume, WiFi connectivity and so on) will be displayed if you have more than one monitor. In this case, the bar displays at the top of the screen _à la Mac_ or GNOME with `position top` and reveals information about system resources with `i3status` (you can find how it can be configured in [my dotfiles](https://github.com/sglavoie/dotfiles/blob/master/.config/i3status/config) or on the [i3status repo](https://github.com/i3/i3status) on GitHub).

```{.bash}
# Start i3bar to display a workspace bar (plus the system information i3status if available)
bar {
    i3bar_command i3bar
    status_command i3status
    position top

## please set your primary output first. Example: 'xrandr --output eDP1 --primary'
    tray_output primary
    bindsym button4 nop
    bindsym button5 nop

    colors {
        background #222222
        statusline #dddddd
        separator #666666
#                         border  backgr. text
        focused_workspace #0088CC #0088CC #ffffff #cccccc
        active_workspace #333333 #333333 #ffffff #181715
        inactive_workspace #333333 #333333 #888888 #AAAAAA
        urgent_workspace #2f343a #900000 #ffffff #FFFFFF
    }
}

# Theme colors
# class          border  backgr. text    indic.  child_border
  client.focused #0088CC #00C8FF #ffffff #dddddd
  client.focused_inactive #333333 #333333 #888888 #292d2e
  client.unfocused #333333 #333333 #888888 #292d2e
  client.urgent #2f343a #900000 #ffffff #900000
  client.placeholder #F9FAF9 #061229 #FFFFFF #061229
  client.background #061229
```

Theming i3 can be tedious, but thankfully there are tools to automate the process! One such tool is [i3-style](https://github.com/altdesktop/i3-style), which allows you to quickly switch in place your theme without having to log out or modify manually your i3 `config` file. To go the manual route or to tweak an existing theme, you can always use a website like [HTML Color Codes](https://htmlcolorcodes.com) to find an exact hexadecimal value. You can also use [terminal.sexy](https://terminal.sexy) to come up with nice looking themes, which can be exported for other applications you may be using.

---

# Conclusion

You can find the [complete `config` file in my dotfiles on GitHub](https://github.com/sglavoie/dotfiles/blob/master/.config/i3/config). If you liked this article, you may also enjoy reading the following ones:

- [Suckless: Minimalist Tools That Work Great](https://www.sglavoie.com/posts/2019/05/12/suckless-minimalist-tools-that-work-great/)
- [Using dmenu to Optimize Common Tasks](https://www.sglavoie.com/posts/2019/11/10/using-dmenu-to-optimize-common-tasks/)
- [Using i3 as a Window Manager for Increased Productivity](https://www.sglavoie.com/posts/2019/01/08/using-i3-as-a-window-manager-for-increased-productivity/)

## More resources and references

- [Getting started with the i3 tiling window manager](https://fedoramagazine.org/getting-started-i3-window-manager/) — Fedora Magazine
- [Official i3 documentation](https://i3wm.org/docs/userguide.html) — i3wm.org
- [i3 page on the Arch Wiki](https://wiki.archlinux.org/index.php/i3) — Arch Wiki
