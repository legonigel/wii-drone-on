import time
from pygame import *
import pygame
import threading
from Queue import Queue

class InputKeyboard(threading.Thread):
	event_queue = Queue()
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

		current_command = ""

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYUP:
					current_command = ""
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						current_command = "reset"
						running = False
						# takeoff / land
					elif event.key == pygame.K_RETURN:
						current_command = "takeoff"
					elif event.key == pygame.K_SPACE:
						current_command = "land"
						# emergency
					elif event.key == pygame.K_BACKSPACE:
						current_command = "reset"
						# forward / backward
					elif event.key == pygame.K_w:
						current_command = "forward"
					elif event.key == pygame.K_s:
						current_command = "back"
						# left / right
					elif event.key == pygame.K_a:
						current_command = "left"
					elif event.key == pygame.K_d:
						current_command = "right"
						# up / down
					elif event.key == pygame.K_UP:
						current_command = "up"
					elif event.key == pygame.K_DOWN:
						current_command = "down"
						# turn left / turn right
					elif event.key == pygame.K_LEFT:
						current_command = "turn_left"
					elif event.key == pygame.K_RIGHT:
						current_command = "turn_right"
						# speed
					elif event.key == pygame.K_1:
						current_command = "speed 0.1"
					elif event.key == pygame.K_2:
						current_command = "speed 0.2"
					elif event.key == pygame.K_3:
						current_command = "0.3"
					elif event.key == pygame.K_4:
						current_command = "0.4"
					elif event.key == pygame.K_5:
						current_command = "0.5"
					elif event.key == pygame.K_6:
						current_command = "0.6"
					elif event.key == pygame.K_7:
						current_command = "0.7"
					elif event.key == pygame.K_8:
						current_command = "0.8"
					elif event.key == pygame.K_9:
						current_command = "0.9"
					elif event.key == pygame.K_0:
						current_command = "1.0"

	def makeConnection(self):
		pass

	def determine(self):
		return current_command

def main():
	myInput = InputKeyboar()
	myInput.makeConnection()
	while True:
		print myInput.determine()

if __name__ == '__main__':
	main()
