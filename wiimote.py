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

def determine(wm):
  if wm.state['buttons'] & cwiid.BTN_PLUS:
    #takeoff
    print "get lifted"
  if wm.state['buttons'] & cwiid.BTN_MINUS:
    #land
    print "landing"
  if wm.state['buttons'] & cwiid.BTN_HOME:
    #panic and stop
    print "kill everything"
  if wm.state['buttons'] & cwiid.BTN_B:
    #flip
	print "barrell roll"
  if wm.state['buttons'] & cwiid.BTN_UP:
	#foward
	print "movin on forward"
  if wm.state['buttons'] & cwiid.BTN_DOWN:
	#back
	print "back it up"
  if wm.state['buttons'] & cwiid.BTN_LEFT:
	#left
	print "to the left"
  if wm.state['buttons'] & cwiid.BTN_RIGHT:
	#right
	print "to the right now yall"
  if wm.state['buttons'] & cwiid.BTN_1:
	#elevate
	print "raise it"
  if wm.state['buttons'] & cwiid.BTN_2:
	#lower
	print "drop it low"
  time.sleep(0.1)

def main():
  wmote = makeConnection()
  while True:
    wmote.led = (wmote.state['led'] + 1) % 16
    determine(wmote)

if __name__ == "__main__":
  main()
