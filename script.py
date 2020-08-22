from gpiozero import LED, DigitalInputDevice
from time import sleep

ledLight = LED(21)
igitionInput = DigitalInputDevice(20)
sleepTime = 3.5

while True:
	igitionInput.wait_for_active()
	ledLight.on()
