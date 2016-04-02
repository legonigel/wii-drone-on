#! /usr/bin/python

import cwiid
import time

def makeConnection():
  print "Press 1 + 2 on the wiimote yo"
  wm = cwiid.Wiimote()
  wm.led = 1
  wm.enable(cwiid.FLAG_MOTIONPLUS)
  wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_MOTIONPLUS | cwiid.RPT_ACC
  print "you be connected"
  return wm

def determine(wmote):
  #acceleration data
  ax = (((mesg[1][cwiid.X])-120)/2)
  ay = (((mesg[1][cwiid.Y])-120)/2)
  az = (((mesg[1][cwiid.Z])-120)/2)
  print "ax " + ax
  print "ay " + ay
  print "az " + az

  #button data
  if wmote.state['buttons'] & cwiid.BTN_PLUS:
    #takeoff
    print "get lifted"
  if wmote.state['buttons'] & cwiid.BTN_MINUS:
    #land
    print "landing"
  if wmote.state['buttons'] & cwiid.BTN_HOME:
    #panic and stop
    print "kill everything"
  if wmote.state['buttons'] & cwiid.BTN_B:
    #flip
	print "barrell roll"
  if wmote.state['buttons'] & cwiid.BTN_UP:
	#foward
	print "movin on forward"
  if wmote.state['buttons'] & cwiid.BTN_DOWN:
	#back
	print "back it up"
  if wmote.state['buttons'] & cwiid.BTN_LEFT:
	#left
	print "to the left"
  if wmote.state['buttons'] & cwiid.BTN_RIGHT:
	#right
	print "to the right now yall"
  if wmote.state['buttons'] & cwiid.BTN_1:
	#elevate
	print "raise it"
  if wmote.state['buttons'] & cwiid.BTN_2:
	#lower
	print "drop it low"

  time.sleep(0.1)

def main():
  wm2 = makeConnection()
  while True:
    wm.led = (wm.state['led'] + 1) % 16
    determine(wm2)

if __name__ == "__main__":
  main()
