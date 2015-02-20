#!/usr/bin/env python3
"""
Migrates Chrome/Chromium password databases to pass

Chrome must be closed and not using the system secure storage (eg, not in Gnome
or KDE).

Passwords are stored in <site domain>/<user name> format. No additional
metadata is stored.
"""

import os
import re
import sqlite3
import subprocess

POSSIBLE_FILES = [
    "~/.config/google-chrome/Default/Login Data",
    "~/.config/chromium/Default/Login Data",
]
PASS_STORE = os.path.expanduser('~/.password-store')

FIND_DOMAIN = re.compile("^https?://([^/]+)/.*")


def pass_import_entry(path, data):
    """ Import new password entry to password-store using pass insert command """
    proc = subprocess.Popen(
        ['pass', 'insert', '--multiline', path],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.communicate(data.encode('utf8'))
    proc.wait()

for db in map(os.path.expanduser, POSSIBLE_FILES):
    if not os.path.exists(db):
        continue

    with sqlite3.connect(db) as conn:
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT blacklisted_by_user, signon_realm, username_value, password_value FROM logins")
        for row in iter(cursor.fetchone, None):
            if row[0]:
                continue
            _, url, user, rpasswd = row
            if not user:
                continue
            domain = FIND_DOMAIN.match(url).group(1)
            passwd = rpasswd.decode('utf-8')
            if not isinstance(passwd, (str)):
                print(row)
                print(type(passwd))
            print(domain, user)
            passname = '{}/{}'.format(domain, user)
            pass_import_entry(passname, passwd)
