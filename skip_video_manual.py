#!/usr/bin/python
# -*- coding: utf-8 -*-
# Manually executable file to trigger video skip from command line.

from evdev import uinput, ecodes as e
import time

	#simulate keystroke "o", which tells omxplayer to skip to the next video (easier than using dbus!)
	with uinput.UInput() as ui:
		ui.write(e.EV_KEY, e.KEY_O, 1)
		ui.syn()

	#disble button for 1 second
	time.sleep(1.0)
