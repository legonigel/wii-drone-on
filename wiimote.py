#! /usr/bin/python

import cwiid
import time
class InputWiimote(Object):
    def makeConnection(self):
      print "Press 1 + 2 on the wiimote yo"
      wm = cwiid.Wiimote()
      wm.led = 1
      wm.enable(cwiid.FLAG_MOTIONPLUS)
      wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_MOTIONPLUS
      print "you be connected"
      self.wm = wm
      return wm

    def determine(self):
      command = ""
      if self.wm.state['buttons'] & cwiid.BTN_PLUS:
        #takeoff
        command = "takeoff"
      if self.wm.state['buttons'] & cwiid.BTN_MINUS:
        #land
        command = "land"
      if self.wm.state['buttons'] & cwiid.BTN_HOME:
        #panic and stop
        command = "kill"
      if self.wm.state['buttons'] & cwiid.BTN_B:
        #flip
    	command = "flip"
      if self.wm.state['buttons'] & cwiid.BTN_UP:
    	#foward
    	command = "forward"
      if self.wm.state['buttons'] & cwiid.BTN_DOWN:
    	#back
    	command = "backward"
      if self.wm.state['buttons'] & cwiid.BTN_LEFT:
    	#left
    	command = "left"
      if self.wm.state['buttons'] & cwiid.BTN_RIGHT:
    	#right
    	command = "right"
      if self.wm.state['buttons'] & cwiid.BTN_1:
    	#elevate
    	command = "up"
      if self.wm.state['buttons'] & cwiid.BTN_2:
    	#lower
    	command = "down"
      time.sleep(0.1)
      return command


def main():
  myInput = InputWiimote()
  wiimote = myInput.makeConnection()
  while True:
    wiimote.led = (wiimote.state['led'] + 1) % 16
    print myInput.determine()

if __name__ == "__main__":
  main()
