#!/bin/sh

setxkbmap -option ctrl:nocaps
# dbus, ibus already in Xsession.d
gnome-keyring-daemon -d
i3lock -i ~/.i3/login.png
exec i3
