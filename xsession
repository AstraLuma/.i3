#!/bin/sh

setxkbmap -option ctrl:nocaps
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus
export STEAM_RUNTIME=0
# dbus, ibus already in Xsession.d
gnome-keyring-daemon -d
i3lock -i ~/.i3/login.png
exec i3
