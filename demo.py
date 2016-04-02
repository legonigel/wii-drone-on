# Python AR.Drone 2.0
#
# Copyright (C) 2013 Quadeare <lacrampe.florian@gmail.com>
# Twitter : @quadeare

from pygame import *
import pygame
import libardrone
import threading
import time
from subprocess import call

import signal
import sys



class video(threading.Thread):
    """Video class to launch media flux"""
    def __init__(self, nom = ''):
        threading.Thread.__init__(self)
        self.process = None
    def run(self):
        print "Video"
        call(["ffplay", "http://192.168.1.1:5555/"])
    def stop(self):
        call(["killall", "ffplay"])
        if self.process is not None:
            self.process.terminate()
            self.process = None

class controle(threading.Thread):
    """Control class (to control the drone)"""

    def __init__(self, nom = ''):
        threading.Thread.__init__(self)
        self._stopevent = threading.Event( )
    def stop(self):
        self._stopevent.set( )

    def run(self):
        """We call pygame (to use controler)"""
        pygame.init()

        """Launch drone class"""
        drone = libardrone.ARDrone(True)
        clock = pygame.time.Clock()
        running = True

        screen = pygame.display.set_mode((640, 400))

        """Set up and init joystick"""
        #j=joystick.Joystick(0)
        #j.init()

        print "running"

        move_forward = 0
        move_backward = 0
        move_left = 0
        move_right = 0
        turn = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYUP:
                    drone.hover()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        drone.reset()
                        running = False
                        # takeoff / land
                    elif event.key == pygame.K_RETURN:
                        drone.takeoff()
                    elif event.key == pygame.K_SPACE:
                        drone.land()
                        # emergency
                    elif event.key == pygame.K_BACKSPACE:
                        drone.reset()
                        # forward / backward
                    elif event.key == pygame.K_w:
                        drone.move_forward()
                    elif event.key == pygame.K_s:
                        drone.move_backward()
                        # left / right
                    elif event.key == pygame.K_a:
                        drone.move_left()
                    elif event.key == pygame.K_d:
                        drone.move_right()
                        # up / down
                    elif event.key == pygame.K_UP:
                        drone.move_up()
                    elif event.key == pygame.K_DOWN:
                        drone.move_down()
                        # turn left / turn right
                    elif event.key == pygame.K_LEFT:
                        drone.turn_left()
                    elif event.key == pygame.K_RIGHT:
                        drone.turn_right()
                        # speed
                    elif event.key == pygame.K_1:
                        drone.speed = 0.1
                    elif event.key == pygame.K_2:
                        drone.speed = 0.2
                    elif event.key == pygame.K_3:
                        drone.speed = 0.3
                    elif event.key == pygame.K_4:
                        drone.speed = 0.4
                    elif event.key == pygame.K_5:
                        drone.speed = 0.5
                    elif event.key == pygame.K_6:
                        drone.speed = 0.6
                    elif event.key == pygame.K_7:
                        drone.speed = 0.7
                    elif event.key == pygame.K_8:
                        drone.speed = 0.8
                    elif event.key == pygame.K_9:
                        drone.speed = 0.9
                    elif event.key == pygame.K_0:
                        drone.speed = 1.0
            clock.tick(1000)

        print "Shutting down...",
        drone.reset()
        drone.halt()
        #video.stop()
        print "Ok."
        quit()


if __name__ == '__main__':
    try:
        # Controle
        controle = controle('Thread Controle')
        controle.start()
        time.sleep(5)
        # Video
        #video = video('Thread Video')
        #video.start()
    except (KeyboardInterrupt, SystemExit):
        controle.stop()
        #cleanup_stop_thread();
        sys.exit()
