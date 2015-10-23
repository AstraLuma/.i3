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
* `feh`
* `xset`
* GNU `make`
* Font Awesome (Debian: `fonts-font-awesome`)
* [`j4-dmenu-desktop`](https://github.com/enkore/j4-dmenu-desktop)
* Gnome Keyring
* [`xss`](http://woozle.org/~neale/src/xss.html)

Setup
-----

1. Check out this repo into `~/.i3`
2. `cd` into it
3. Run `make` to generate config file
4. Start i3

Other recomendations (These are, in fact, totally optional):

* (Debian) Run `update-alternatives --config dmenu` and select `dmenu.xft` for better font support
* Run `make install` to symlink this xsession into your home directory
* Configure autologin in your DM (if you use my xsession)