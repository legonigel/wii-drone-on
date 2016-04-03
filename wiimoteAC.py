#! /usr/bin/python

import cwiid
import time
class InputWiimoteAC(Object):
    def makeConnection(self):
      print "Press 1 + 2 on the wiimote yo"
      wm = cwiid.Wiimote()
      wm.led = 1
      wm.enable(cwiid.FLAG_MOTIONPLUS)
      wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
      print "you be connected"
      self.wm = wm
      return wm

    def determine(self):
      #print "x: " + str(float((wm.state['acc'][0]-125))/30)
      #print "y: " + str(float((wm.state['acc'][1]-125))/30)
      directions = "LR " + str(float((self.wm.state['acc'][0]-125))/30) + " FB " + str(float((self.wm.state['acc'][1]-125))/30)
      time.sleep(0.1)
      return directions

def main():
  myInputAC = InputWiimoteAC()
  wiimote = myInputAC.makeConnection()
  while True:
    wiimote.led = (wiimote.state['led'] + 1) % 16
    print myInputAC.determine(wiimote)

if __name__ == "__main__":
  main()
