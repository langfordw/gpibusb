# gpibusb
Code to interface with GPIB equipment using a USB to GPIB adaptor (prologix)

usage:

```python
import gpibusb
dc_ps = gpibusb.GPIBUSB("/dev/tty.usbserial-PX8WHCO8")
dc_ps.sendCommand("apply 5.0, 0.1") # set current limit to 0.1A, voltage to 5V
dc_ps.sendCommand("output on") # turn on the output
```
