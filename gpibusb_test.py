import gpibusb
from time import sleep
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# todo output data to table

# controling an Agilent E3633A DC Power Supply
# using prologix usb to gpib adaptor
dc_ps = gpibusb.GPIBUSB("/dev/tty.usbserial-PX8WHCO8")
dc_ps.sendCommand("apply 0.0, .1") # set current limit to 0.01A
dc_ps.sendCommand("voltage:step 0.1") # set step increment
dc_ps.sendCommand("voltage:protection:state 0") # turn off voltage protection
dc_ps.sendCommand("current:protection:state 0") # turn off curretn protection
dc_ps.sendCommand("output on") # turn on the output

v = 0
current = [];
voltage = [];
for i in range(20):
	dc_ps.sendCommand("voltage up")
	sleep(.5)
	c = dc_ps.askCommand("measure:current?")
	if (len(c)>1):
		print c
		current.append(float(c))
		v+=.1
		voltage.append(v)
	sleep(.5)

dc_ps.sendCommand("output off") # turn on the output

print voltage
print current

plt.figure()
plt.plot(voltage,current)
plt.show()