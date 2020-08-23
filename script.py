from gpiozero import LED, DigitalInputDevice
from time import sleep

ledLight = LED(21)
igitionInput = DigitalInputDevice(20)
sleepTime = 3.5
ledOn = False

while True:
        if (ledOn):
            ledLight.off()
            ledOn = False
        else:
            ledLight.on()
            ledOn = True

        sleep(sleepTime)
