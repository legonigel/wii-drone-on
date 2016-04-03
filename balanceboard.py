#! /usr/bin/python

import cwiid
from time import sleep

class InputBalanceBoard(object):
	def makeConnection(self):
		print "Press sync on da board yo"
		wiiboard = cwiid.Wiimote()
		wiiboard.led = 1
		wiiboard.rpt_mode = cwiid.RPT_BALANCE | cwiid.RPT_BTN
		wiiboard.request_status()
		sleep(1)
		print wiiboard.state['ext_type']
		ballance_calibration = wiiboard.get_balance_cal()
		self.named_cal = {'right_top':ballance_calibration[0],
					 'right_bottom':ballance_calibration[1],
					 'left_top':ballance_calibration[2],
					 'left_bottom':ballance_calibration[3]}
		self.calibrations = ballance_calibration
		print "you be connected"
		self.wiiboard = wiiboard
		return wiiboard

	def determine(self):
		command = ""
		self.wiiboard.request_status()

		readings = self.wiiboard.state['balance']

		weight = (calcweight(readings, self.named_cal)/100.0)

		x_bal, y_bal = get_balance(readings, self.named_cal)
		command = "lr " + str(x_bal) + " fb " + str(y_bal)
		return command

def get_balance(readings, calibrations):
	right_top = gsc(readings, 'right_top', calibrations)
	left_top  = gsc(readings, 'left_top' , calibrations)
	right_bottom = gsc(readings, 'right_bottom', calibrations)
	left_bottom  = gsc(readings, 'left_bottom' , calibrations)
	try:
		x_bal = (float(right_top + right_bottom)) / (float(left_top + left_bottom))
		if x_bal > 1:
			x_bal = ((float(left_top + left_bottom)) / (float(right_top + right_bottom)) * -1.0) + 1.0
		else:
			x_bal = x_bal - 1.0
		y_bal = (float(left_bottom + right_bottom)) / (float(left_top + right_top))
		if y_bal > 1:
			y_bal = ((float(left_top + right_top)) / (float(left_bottom + right_bottom)) * -1.0) + 1.0
		else:
			y_bal = y_bal - 1.0
	except:
		x_bal = 0
		y_bal = 0

	return (x_bal, y_bal)

def gsc(readings, pos, calibrations):
	reading = readings[pos]
	calibration = calibrations[pos]

	if reading < calibration[1]:
		weight = 1700 * (reading - calibration[0]) / (calibration[1] - calibration[0])
	else:
		weight = 1700 * (reading - calibration[0]) / (calibration[2] - calibration[1]) + 1700
	return weight


def calcweight(readings, calibrations):
	weight = 0
	for sensor in ('right_top','right_bottom','left_top','left_bottom'):
		weight += gsc(readings, sensor, calibrations)
	return weight


def main():
	myBoard = InputBalanceBoard()
	board = myBoard.makeConnection()
	while True:
		board.led = (board.state['led'] + 1) % 2
		print myBoard.determine()

if __name__ == "__main__":
	main()
