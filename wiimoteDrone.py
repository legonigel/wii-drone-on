#! /usr/bin/python

import cwiid
import time

print "Press 1 + 2 on the wiimote yo"
wm = cwiid.Wiimote()
wm.led = 1
wm.enable(cwiid.FLAG_MOTIONPLUS)
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_MOTIONPLUS
print "you be connected"

def direction():
    dpadNum = wm.state['buttons']
    if(dpadNum != 0):
	print dpadNum
    time.sleep(0.1)

while True:
    wm.led = (wm.state['led'] + 1) % 16
    direction()

