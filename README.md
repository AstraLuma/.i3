.i3
===
My [i3](http://i3wm.org/) configuration and scripts. My goal is to build up a fully-featured desktop environment based on i3.

* Screen locking for security
* Power management
* Basic desktop daemons: PulseAudio, NetworkManager, Bluetooth, Dropbox
* Wallpaper (from dropbox)

Requirements
------------
Most of these can be had from your package manager.

* i3 (obviously)
* Python 3
* i3ipc (from PyPI)
* ImageMagick
* `feh`
* `scrot`
* `xautolock`
* `xset`
* `gpg-agent`
* [`pass`](http://www.passwordstore.org/)
* `xdotool`
* GNU `make`
* [`j4-dmenu-desktop`](https://github.com/enkore/j4-dmenu-desktop)

Setup
-----

1. Check out this repo into `~/.i3`
2. `cd` into it
3. Run `make` to generate config file
4. Start i3
