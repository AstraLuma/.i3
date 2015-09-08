#!/bin/sh

echo "Hello!"
dbus-launch --sh-syntax | . /dev/stdin
gnome-keyring-daemon -d
i3lock -i ~/.i3/login.png
exec i3
