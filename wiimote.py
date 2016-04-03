#! /usr/bin/python

import cwiid
import time

def makeConnection():
  print "Press 1 + 2 on the wiimote yo"
  wm = cwiid.Wiimote()
  wm.led = 1
  wm.enable(cwiid.FLAG_MOTIONPLUS)
  wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_MOTIONPLUS
  print "you be connected"
  return wm

def determine(wmote):
  String command = ""
  if wmote.state['buttons'] & cwiid.BTN_PLUS:
    #takeoff
    command = "takeoff"
  if wmote.state['buttons'] & cwiid.BTN_MINUS:
    #land
    command = "land"
  if wmote.state['buttons'] & cwiid.BTN_HOME:
    #panic and stop
    command = "kill"
  if wmote.state['buttons'] & cwiid.BTN_B:
    #flip
	command = "flip"
  if wmote.state['buttons'] & cwiid.BTN_UP:
	#foward
	command = "forward"
  if wmote.state['buttons'] & cwiid.BTN_DOWN:
	#back
	command = "backward"
  if wmote.state['buttons'] & cwiid.BTN_LEFT:
	#left
	command = "left"
  if wmote.state['buttons'] & cwiid.BTN_RIGHT:
	#right
	command = "right"
  if wmote.state['buttons'] & cwiid.BTN_1:
	#elevate
	command = "up"
  if wmote.state['buttons'] & cwiid.BTN_2:
	#lower
	command = "down"
  time.sleep(0.1)
  return command


def main():
  wiimote = makeConnection()
  while True:
    wiimote.led = (wiimote.state['led'] + 1) % 16
    determine(wiimote)

if __name__ == "__main__":
  main()
