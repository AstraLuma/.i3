#!/usr/bin/env python3
# From https://github.com/acrisci/i3ipc-python/raw/master/examples/disable-standby-fs.py

from argparse import ArgumentParser
from subprocess import call
import i3ipc

i3 = i3ipc.Connection()

parser = ArgumentParser(prog='disable-standby-fs',
        description='''
        Disable standby (dpms) and screensaver when a window becomes fullscreen
        or exits fullscreen-mode. Requires `xorg-xset`.
        ''')

args = parser.parse_args()

class StackManager(set):
    """
    Like a set, but:
    * Disables locking & power management has items
    * Enables them when empty
    """
    _oldlen = None

    def _update(self):
        if len(self) != self._oldlen:
            if len(self):
                print("Disabling screen features")
                call(['xset', 's', 'off'])
                call(['xset', '-dpms'])
                call(['xautolock', '-disable'])
            else:
                print("Enabling screen features")
                call(['xset', 's', 'on'])
                call(['xset', '+dpms'])
                call(['xautolock', '-enable'])
            self._oldlen = len(self)

    def add(self, item):
        super().add(item)
        self._update()

    def discard(self, item):
        super().discard(item)
        self._update()

fswstack = StackManager()

def on_fullscreen_mode(i3, e):
    # e.container.props.window or e.container.props.id
    wid = e.container.props.window
    if e.container.props.fullscreen_mode:
        fswstack.add(wid)
    else:
        fswstack.discard(wid)

def on_window_close(i3, e):
    wid = e.container.props.window
    fswstack.discard(wid)

i3.on('window::fullscreen_mode', on_fullscreen_mode)
i3.on('window::close', on_window_close)

i3.main()
