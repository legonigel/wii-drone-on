#! /usr/bin/python

import cwiid
from time import sleep

class InputBalanceBoard(Object):
    def makeConnection(self):
      print "Press sync on da board yo"
      wiiboard = cwiid.Wiimote()
      wiiboard.led = 1
      wiiboard.rpt_mode = cwiid.RPT_BALANCE | cwiid.RPT_BTN
      wiiboard.request_status()
      sleep(1)
      print wiiboard.state['ext_type']
      print "you be connected"
      self.wiiboard = wiiboard
      return wiiboard



    def determine(self):
      command = ""

      sleep(0.1)
      return command


def main():
  myBoard = InputBalanceBoard()
  board = myBoard.makeConnection()
  while True:
    board.led = (board.state['led'] + 1) % 2
    print myBoard.determine()

if __name__ == "__main__":
  main()
