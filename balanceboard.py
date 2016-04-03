#! /usr/bin/python

import cwiid
import time

class InputBalanceBoard(Object):
    def makeConnection(self):
      print "Press sync on da board yo"
      wiiboard = cwiid.Wiimote()
      wiiboard.led = 1
      wiiboard.enable(cwiid.FLAG_MOTIONPLUS)
      wiimote.rpt_mode = cwiid.RPT_BALANCE | cwiid.RPT_BTN
      print "you be connected"
      self.wiimote = wiimote
      return wiimote

    def determine(self):
      command = ""
      if wiimote.state['ext_type'] != cwiid.EXT_BALANCE:
          print 'This program only supports the Wii Balance Board'
	      wiimote.close()
	      sys.exit(1)
	balance_calibration = wiimote.get_balance_cal()
	named_calibration = { 'right_top': balance_calibration[0],
                          'right_bottom': balance_calibration[1],
                          'left_top': balance_calibration[2],
                          'left_bottom': balance_calibration[3],
                        }
      time.sleep(0.1)
      return command


def main():
  myBoard = InputBalanceBoard()
  board = myBoard.makeConnection()
  while True:
    board.led = (board.state['led'] + 1) % 2
    print myBoard.determine()

if __name__ == "__main__":
  main()
