#!/bin/sh

setxkbmap -option ctrl:nocaps
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus
i3lock -i ~/.i3/login.png
dbus-launch --exit-with-session i3
