#! /usr/bin/env python

import libardrone
import threading

from time import sleep
import Queue
import signal
import sys

class DroneController(threading.Thread):
	"""Control class (to control the drone)"""

	is_flying = False
	speed = 0.1
	event_queue = Queue.Queue()

	previous_cmds = []

	prev_cmd_len = 50

	def __init__(self, nom = ''):
		threading.Thread.__init__(self)
		self._stopevent = threading.Event( )

	def stop(self):
		self._stopevent.set( )

	def run(self):
		"""Launch drone class"""
		self.drone = libardrone.ARDrone(True)

		print "running"

		move_forward = 0
		move_backward = 0
		move_left = 0
		move_right = 0
		turn = 0

		running = True
		while running:
			try:
				event, params = self.event_queue.get(True, 1)
				print "got event"
				event(*params)
			except Queue.Empty:
				self.drone.hover()
				sleep(0.001)

		print "Shutting down...",
		drone.reset()
		drone.halt()
		print "Ok."
		quit()

	def add_move(self, left=0, right=0, forward=0, back=0, up=0, down=0, t_left=0, t_right=0):
		if len(self.previous_cmds) == self.prev_cmd_len:
			self.previous_cmds.pop(0)
		self.previous_cmds.append({'left':left,'right':right,'forward':forward,'back':back,'up':up,'down':down,'t_left':t_left,'t_right':t_right})
		lr = 0
		lr_cnt = 0
		fb = 0
		fb_cnt = 0
		vv = 0
		vv_cnt = 0
		va = 0
		va_cnt = 0
		for cmd in self.previous_cmds:
			if cmd['right'] or cmd['left']:
				lr = cmd['right'] - cmd['left']
				lr_cnt += 1
			if cmd['back'] or cmd['forward']:
				fb = cmd['back'] - cmd['forward']
				fb_cnt += 1
			if cmd['up'] or cmd['down']:
				vv = cmd['up'] - cmd['down']
				vv_cnt += 1
			if cmd['t_right'] or cmd['t_left']:
				va = cmd['t_right'] - cmd['t_left']
				va_cnt += 1
		if lr_cnt:
			lr = lr * 1.0/ lr_cnt
		if fb_cnt:
			fb = fb * 1.0/ fb_cnt
		if vv_cnt:
			vv = vv * 1.0/ vv_cnt
		if va_cnt:
			va = va * 1.0/ va_cnt

		self.event_queue.put((self.drone.move_4d, (lr,fb,vv,va)))


	def do_command(self, command_string):
		"""
		makes the drone do something
		command_string is the string to execute
		such as turn_left, move_forward, possibly followed by a nubmer 0..1
		"""
		if any(s in command_string for s in ['kill','reset']):
			self.event_queue.put((self.drone.reset,()))
			self.is_flying = False
		elif any(s in command_string for s in ['halt']):
			self.event_queue.put((self.drone.halt,()))
			self.is_flying = False
		elif any(s in command_string for s in ['takeoff','tkoff']) and not self.is_flying:
			#takeoff
			self.event_queue.put((self.drone.takeoff, ()))
			self.is_flying = True
		elif any(s in command_string for s in ['land','lnd']):
			#land
			self.event_queue.put((self.drone.land, ()))
			self.is_flying = False

		if not self.is_flying:
			#cant do stuff when not flying
			return False

		if len(command_string.split(' ')) == 4 and 'lr' in command_string and 'fb' in command_string:
			splits = command_string.split(' ')
			lr = 0
			fb = 0
			for num, item in enumerate(splits):
				if item == 'lr':
					lr = float(splits[num + 1])
				elif item == 'fb':
					fb = float(splits[num + 1])
			self.add_move(forward = fb, left = lr)
			return True
		if len(command_string.split(' ')) > 3:
			print "Too many words in the command string!"
			return False

		number = self.speed
		if len(command_string.split(' ')) > 1:
			try:
				number = float(command_string.split(' ')[1])
			except Exception:
				print "You really fucked up the command, {} is not a number".format(command_string.split(' ')[1])
				return False


		print "speed is {}".format(number)
		print type(number)
		if any(s in command_string for s in ['forward','fwrd']):
			#move forward
			self.add_move(forward = number)
		elif any(s in command_string for s in ['backward','bckwd','back']):
			#move back
			print "doing back"
			self.add_move(back = number)
		elif 'turn' in command_string:
			#turn commands
			if any(s in command_string for s in ['left']):
				#move left
				self.add_move(t_left = number)
			elif any(s in command_string for s in ['right']):
				#move right
				self.add_move(t_right = number)
			else:
				print "Invalid Turn command"
				return False
		elif any(s in command_string for s in ['left']):
			#move left
			self.add_move(left = number)
		elif any(s in command_string for s in ['right']):
			#move right
			self.add_move(right = number)
		elif any(s in command_string for s in ['up']):
			#up
			self.add_move(up = number)
		elif any(s in command_string for s in ['down','dn']):
			#down
			self.add_move(down = number)
		elif any(s in command_string for s in ['speed']):
			#speed
			self.speed = number
		else:
			print "Bad drone command {}".format(command_string)
			return False
		return True
