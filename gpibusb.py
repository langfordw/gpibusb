import serial
from time import sleep

class GPIBUSB():

###################
#  INITIALIZATION #
###################
	def __init__(self, port):
		self._serialPort = port
		self._rawSerial = serial.Serial(self._serialPort, 9600, timeout=0)
		self.clearAutoAsk()

#################
# CONFIGURATION #
#################
	def clearAutoAsk(self):
		self.sendCommand("++auto 0")

	def setAutoAsk(self):
		self.sendCommand("++auto 1")

#############
# BASIC I/O #
#############
	def sendCommand(self, command):
		self._rawSerial.write(command+"\n")

	def askCommand(self, command):
		self._rawSerial.write(command+"\n")
		self._rawSerial.write("++read eoi\n")
		return self._readResponse()

	def _readResponse(self):
		buffer = []
		while len(buffer) <= 0:
			buffer = self._rawSerial.read(9999)
		return buffer.rstrip('\r'+'\n')
