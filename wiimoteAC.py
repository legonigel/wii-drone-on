#! /usr/bin/python

import cwiid
import time

def makeConnection():
  print "Press 1 + 2 on the wiimote yo"
  wm = cwiid.Wiimote()
  wm.led = 1
  wm.enable(cwiid.FLAG_MOTIONPLUS)
  wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
  print "you be connected"
  return wm

def accelerationDir(wmote):
  ax = 0
  ay = 0
  az = 0
  messages = wiimote.get_mesg()
  for mesg in messages:
    if mesg[0] == cwiid.MESG_ACC:
        ax = (((mesg[1][cwiid.X])-120)/2)
        ay = (((mesg[1][cwiid.Y])-120)/2)
        az = (((mesg[1][cwiid.Z])-120)/2)
        print "ax " + ax + "ay " + ay + "az " + az
  time.sleep(0.1)

def main():
  wiimote = makeConnection()
  while True:
    wiimote.led = (wiimote.state['led'] + 1) % 16
    accelerationDir(wiimote)

if __name__ == "__main__":
  main()
