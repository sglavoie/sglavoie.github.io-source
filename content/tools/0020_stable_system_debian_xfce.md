Title: Tip the Scales in Times of Instability With the Rock-Solid Debian Xfce
Date: 2020-04-05 12:14
Slug: tip-the-scales-in-times-of-instability-with-the-rock-solid-debian-xfce
Tags: debian, linux, stability, xfce
Authors: Sébastien Lavoie
Summary: Desperate times call for the best Linux experience possible... And in my experience so far, the [Debian](https://www.debian.org/) distribution with the [Xfce desktop environment](https://www.xfce.org/) makes for a very smooth ride.
Description: Desperate times call for the best Linux experience possible... And in my experience so far, the Debian distribution with the Xfce desktop environment makes for a very smooth ride.

# Introduction
I'm familiar with Linux distribution hopping, having tried out many options over the years, starting around the time Mandrake 9.2 was popular back in 2003, then switching to a few others including Ubuntu, KNOPPIX, Fedora, Xubuntu, openSUSE, Kubuntu, Mint, Manjaro, Mandriva... And of course Debian along the way, which undoubtedly used to be relatively harder to get started with.

My heart has also been stirred by different desktop environments and window managers, from more user-friendly/feature-rich solutions such as KDE, GNOME (along with Unity when it was still a thing), Xfce and Cinnamon to an arguably more obscure selection comprising Openbox, Fluxbox, Enlightenment, Awesome WM, dwm, i3 and bspwm.

I haven't tried everything that's out there (XMonad being one such _esoteric_ possibility), but I've come to realize that what matters most to me is a great balance of stability and usability, allowing to be more focused on any given task at end and therefore leading to increased productivity. For this reason, I recently turned back to a fantastic combo: Debian with Xfce.

---

## Why Debian Xfce?
### Stability and Reliability
Debian has always been to me the father figure of stability in the Linux world. Countless servers have run on Debian and continue to do so for good reason: it just works once it is properly set up. I have had some bad luck with other Debian-based distributions like Ubuntu and Linux Mint which strive to be easier to use but remain easier to break, being a bit more bleeding edge and sometimes bloated too with tons of software I don't really need. Fedora, although I like its philosophy and style very much, has always lead to hardware issues on my apparently less-than-ideal machines. Manjaro has been pleasant and easy to use, but Arch feels like the _right_ choice if one is to build a custom system from scratch. It does take a good amount of time to get things going on such a distribution and usually a good dose of maintenance too, which brought me to seek less time-consuming options. For stability and reliability, Debian is hard to beat in my experience.

### Marvelous Package Manager
I have always found the package manager on Debian (and derivatives) to be easier to use than alternatives like `yum`, `DNF` or `urpmi` for RPM packages. The `pacman` package manager available on Arch-based systems is truly excellent and powerful, but I simply find `apt` to be more intuitive after using it for a lot longer.

### It Just Won't Break
Sitting on the bleeding edge is fun and sometimes even rewarding when things finally work as expected, but I have seen that it doesn't stay that way forever. Big updates, sometimes relatively frequent ones, can leave the system in an unusable state. It's often a minor annoyance to fix, but that just doesn't happen on Debian, where packages are vetted mainly for their legendary stability before releasing them. They are indeed quite a bit older than what can be found on other distributions. It's the price to pay, but I came to the conclusion that it's worth it if you're looking to get things done in the long run.


<figure>
    <a href="{static}/images/posts/0020_stable_system_debian_xfce/debian_xfce.png"><img src="{static}/images/posts/0020_stable_system_debian_xfce/debian_xfce.png" alt="debian_xfce" class="max-size-img-post"></a>
    <figcaption>Debian Xfce in its glorious simplicity.</figcaption>
</figure>

### Xfce Is Minimalist Enough and Hassle-Free
It's also about the combination of **Debian + Xfce**: while Debian makes sure the system remains functional as a whole, Xfce is the solution for interacting with applications and windows without glitches. Debian itself keeps old packages around by choice and Xfce has a _very_ slow release cycle yet also provides stability out of the box. This means that installing Xfce on Debian **has** to work because bugs have been evened out over **years** of effort from both teams.

#### Xfce vs KDE
One of the main appeals of desktop environments like KDE and GNOME is that they have more features and add them more often. They do use more resources and even though they have gone through substantial optimizations over the years, they still feel less snappy on older systems compared to simpler window managers or even Xfce. Recently, KDE caught up with Xfce in terms of resources utilization, but there's one major reason I just can't rely on it on a production machine: in every single release I have tried (from KDE 2.x in the early 2000s to Plasma 5.x), I was confronted with numerous bugs within minutes of delving into it. I have always been faced with some minor troubles on GNOME too (versions 2 and 3), but it's never been as severe as with KDE. KDE has plenty of cool ideas and is fully customizable, but that's to a fault in my view.

#### Xfce vs GNOME
On the other hand, GNOME does consume at least twice as much RAM and CPU compared with Xfce even with no extensions enabled on GNOME and a couple of plugins activated on Xfce. I enjoy how GNOME deals with virtual desktops and think this can be a great productivity enhancement, but once I've configured Xfce to be mainly keyboard-driven, I prefer keeping it simpler with less transition effects and other nice visual additions. On the graphical side of things, GNOME with Wayland has never worked as well for me as with Xorg, so that's something else to watch for.

#### Xfce vs i3
Well, `i3` is a different beast in its own right and has taken a special place in my heart. It uses less memory and CPU than any desktop environment out there and can be used with minimalistic software, like the `st` terminal and the dynamic menu `dmenu` (read the article about [suckless tools](https://www.sglavoie.com/posts/2019/05/12/suckless-minimalist-tools-that-work-great/) if that resonates with your style!). But there are still a few things that I didn't like very much about it, such as the way windows are managed in fullscreen mode, the default lack of a convenient master/slave tiling layout (similar to `dwm` and `bspwm`) and the way one interacts with external monitor(s), where workspaces use the same numbering across multiple screens.

I find that maximizing windows works like what you would expect in Xfce, covering everything but the menu bar. There's also the fact that Xfce makes it very convenient to add and remove virtual desktops on the fly instead of having a bunch of those at all time. With minimal Bash scripting, windows in Xfce can be moved around from one monitor to the other, replicating a useful feature available in `i3`. Xfce, having only _floating_ windows, behaves better with applications like VirtualBox and GIMP by default. And there's also some common ground with the "pseudo tiling" available in Xfce which makes `i3` much less unique.

In the department of customization, `i3` is very good, but having to edit a configuration file manually each time a little change is desired can become tiresome. Xfce has a wonderful settings manager which makes it easy to adjust many system settings as well as those related only to the window manager. `i3` requires initially quite a bit more effort to work and will incur a few additional dependencies if one wants to make it look better. Xfce strikes a very good balance: it's highly customizable; pretty much bug-free in my experience and is usable right away without any surprise.

#### Xfce vs Other Window Managers
Now, there is an endless stream of other options to explore and I don't know enough about many of those to dare to comment. But from those I tried, I can certainly say that I preferred the ease of use of Xfce over other more minimalistic approaches like Openbox, Enlightenment and Fluxbox. Xfce offers all you need out of the box, but not much more, which is what I'm looking for at this moment. On the other hand, making `dwm` work in one precise way can be tricky and requires many tweaks before the configuration can remain untouched for a while. I do not like the necessity of recompiling the source code every single time a tiny change is made which led me to discard it as a convenient option in the long run. I like making small visual adjustments to my system from time to time and I want this to be as frictionless as possible.

Otherwise, `dwm` and `bspwm` might be some very decent options if one is inclined to be tweaking everything from scratch (it's not really a facultative step anyways!), but Xfce integrates everything one might need under very few different packages and has been extremely reliable for me from the beginning. On any kind of modern machine, the extra system resources used up by Xfce compared to those lighter alternatives really don't mean much in the end because it is compensated with the presence of useful applets and tools which definitely make one's life easier.

### It's Ideal for Developers
#### Resources Efficiency & Effectiveness
Debian with Xfce is resource-efficient and comes with much less software out of the box compared to the KDE or GNOME editions: instead, more resources are available for hungry applications like heavy IDEs. Installing applications specific to those desktop environments work flawlessly too. Not only does Debian consume less resources (especially while running Xfce on top), it does so extremely well and offers great performance.

<figure>
    <a href="{static}/images/posts/0020_stable_system_debian_xfce/resources_utilization.png"><img src="{static}/images/posts/0020_stable_system_debian_xfce/resources_utilization.png" alt="resources_utilization" class="max-size-img-post"></a>
    <figcaption>Debian Xfce mostly at rest.</figcaption>
</figure>


#### Rock-Solid Stability (Again, Big Selling Point!)
Since it's so stable, any release of Debian is currently supported for at least 3 years and up to 5 years for LTS (Long Term Support) releases, which means one doesn't have to worry about constantly upgrading the system. For a start, upgrading packages on the stable branch of Debian very rarely leads to a broken system, unlike on more bleeding edge distros like Fedora or Manjaro where downloading a few months old release almost guarantees some unexpected challenges.

#### Packages Availability
With currently close to 58,000 packages offered on Debian, there's a very good chance that anything one might need will be available. Working with up-to-date, proprietary applications like Google Chrome, Zoom or Slack is also pain-free: most companies, when they do consider Linux, opt for sharing a classic `deb` package, the format used on Debian and Debian-based systems. Some of those packages can also be found or added directly to the sources managed by the package manager, allowing for easy, automatic updates.

<figure>
    <a href="{static}/images/posts/0020_stable_system_debian_xfce/debian_packages.png"><img src="{static}/images/posts/0020_stable_system_debian_xfce/debian_packages.png" alt="debian_packages" class="max-size-img-post"></a>
    <figcaption>Synaptic, the legendary package manager.</figcaption>
</figure>


#### Large Community with Freedom in Mind
Because no company backs Debian directly, it relies on a community effort to keep going and it has done so for a long time, having now hundreds of distributions being based on it. This means that it's easy to find a ton of documentation and tutorials giving solutions taking into account Debian-based systems. One will be able to fix any issue cropping up thanks to the [Debian User Forums](http://forums.debian.net/) and of course thanks to the immense popularity of Ubuntu, which contributes tremendously to making answers available in [its forums](https://ubuntuforums.org/) and in the [Stack Exchange](https://askubuntu.com/) network.

---

## Resources to Get Started

- [Debian Documentation](https://www.debian.org/doc/)
- [Debian User Forums](http://forums.debian.net/)
- [Debian Wiki](https://wiki.debian.org/)
- Developer-oriented: [resources for contributing to Debian](https://www.debian.org/doc/manuals/developers-reference/resources.html)
- Cloud-oriented: [tutorials for Debian on Digital Ocean](https://www.digitalocean.com/community/tags/debian)

---

# Conclusion

After trying many different Linux distributions and desktop environments, I keep coming back to what satisfies me best in the end: stability and usability. Debian feels a bit old, but at the same time one knows it delivers on what it promises. The same can be said for Xfce. This is also what makes them such a good combo: despite not being cutting edge in the realm of features, there's no way it could break as easily as KDE or GNOME, particularly on less stable distributions. There are still a few rough edges when it comes to customizing Xfce in my opinion, but when looking for something that just works and will keep doing so, Debian Xfce edition is hard to beat.
