import gpibusb
from time import sleep

# controling an Agilent E3633A DC Power Supply
# using prologix usb to gpib adaptor
dc_ps = gpibusb.GPIBUSB("/dev/tty.usbserial-PX8WHCO8")
dc_ps.sendCommand("apply 0.0, 0.1") # set current limit to 0.01A
dc_ps.sendCommand("voltage:step 0.1") # set step increment
dc_ps.sendCommand("voltage:protection:state 0") # turn off voltage protection
dc_ps.sendCommand("current:protection:state 0") # turn off curretn protection
dc_ps.sendCommand("output on") # turn on the output

v = 0
current = [];
voltage = [];
for i in range(20):
	dc_ps.sendCommand("voltage up")
	v+=.1
	voltage.append(v)
	sleep(.05)
	c = dc_ps.askCommand("measure:current?")
	print float(c)
	current.append(float(c))
	sleep(.05)

dc_ps.sendCommand("output off") # turn on the output

print current