#! /usr/bin/python
# Python AR.Drone control
# Copyright (C) 2016 LegoNigel <legonigel@gmail.com>

import libardrone
from drone_control import DroneController
from video import Video
from wiimote import InputWiimote
from keyboard import InputKeyboard

import signal
import sys

def main():
	"""Main program"""
	controller = DroneController()
	controller.start()

	input_sources = []
	input_sources.append(InputWiimote())
	input_sources.append(InputKeyboar())

	for source in input_sources:
		if hasattr(source, "makeConnection"):
			source.makeConnection()
		else:
			print "This input source has not makeConnection method you dumb coder!"
			print source
		if not hasattr(source, "determine"):
			print "{} has not function determine, exiting".format(source)
			exit(1)

	running = True
	try:
		while running:
			for source in input_sources:
				command = source.determine()
				if command:
					controller.do_command(command)
			sleep(0.01) #sleep 10 ms


	except (KeyboardInterrupt, SystemExit):
		pass
	for source in input_sources:
		if hasattr(source, "stop"):
			source.stop()
	controller.do_command("reset")
	controller.do_command("halt")
	print "Done!"
	quit()


if __name__ == '__main__':
	try:
		#vid = Video('Thread Video')
		#vid.start()
		main()
	except Exception:
		#vid.stop()
		sys.exit()
