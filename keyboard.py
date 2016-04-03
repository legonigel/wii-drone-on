import time
from pygame import *
import pygame
import threading

class InputKeyboard(threading.Thread):
	current_command = ""
	def __init__(self, nom = ''):
		threading.Thread.__init__(self)
		self._stopevent = threading.Event()

	def stop(self):
		self._stopevent.set()

	def run(self):
		pygame.init()
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode((640,360))

		running = True

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYUP:
					self.current_command = ""
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.current_command = "reset"
						running = False
						# takeoff / land
					elif event.key == pygame.K_RETURN:
						self.current_command = "takeoff"
					elif event.key == pygame.K_SPACE:
						self.current_command = "land"
						# emergency
					elif event.key == pygame.K_BACKSPACE:
						self.current_command = "reset"
						# forward / backward
					elif event.key == pygame.K_w:
						self.current_command = "forward"
					elif event.key == pygame.K_s:
						self.current_command = "back"
						# left / right
					elif event.key == pygame.K_a:
						self.current_command = "left"
					elif event.key == pygame.K_d:
						self.current_command = "right"
						# up / down
					elif event.key == pygame.K_UP:
						self.current_command = "up"
					elif event.key == pygame.K_DOWN:
						self.current_command = "down"
						# turn left / turn right
					elif event.key == pygame.K_LEFT:
						self.current_command = "turn_left"
					elif event.key == pygame.K_RIGHT:
						self.current_command = "turn_right"
						# speed
					elif event.key == pygame.K_1:
						self.current_command = "speed 0.1"
					elif event.key == pygame.K_2:
						self.current_command = "speed 0.2"
					elif event.key == pygame.K_3:
						self.current_command = "0.3"
					elif event.key == pygame.K_4:
						self.current_command = "0.4"
					elif event.key == pygame.K_5:
						self.current_command = "0.5"
					elif event.key == pygame.K_6:
						self.current_command = "0.6"
					elif event.key == pygame.K_7:
						self.current_command = "0.7"
					elif event.key == pygame.K_8:
						self.current_command = "0.8"
					elif event.key == pygame.K_9:
						self.current_command = "0.9"
					elif event.key == pygame.K_0:
						self.current_command = "1.0"
					print "cur_cmd: {}".format(self.current_command)
			clock.tick(1000)

	def makeConnection(self):
		self.start()

	def determine(self):
		return self.current_command

def main():
	myInput = InputKeyboard()
	myInput.makeConnection()
	while True:
		print myInput.determine()

if __name__ == '__main__':
	main()
