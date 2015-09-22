import RPi.GPIO as GPIO
import time

#  1  2  4  8  16 32 64 128 BINARY DIGIT
#  23 18 15 14 26 19 6  13  CORRESPONDING PIN


#set BCM mode
GPIO.setmode(GPIO.BCM)

#set the buttons on pin 17 and 27
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#set the LED's 
GPIO.setup(13,GPIO.OUT)   #128
GPIO.setup(6,GPIO.OUT)   #64
GPIO.setup(19,GPIO.OUT)  #32
GPIO.setup(26,GPIO.OUT)  #16
GPIO.setup(24,GPIO.OUT)  #8
GPIO.setup(15,GPIO.OUT)  #4
GPIO.setup(18,GPIO.OUT)  #2
GPIO.setup(23,GPIO.OUT)  #1

#we set everything on low at start
GPIO.output(13,GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)

counter = 0

def buttonHandler():
	global counter
	if (GPIO.input(27) == 1 and counter != 255):
		counter += 1
		print bin(counter)[2:].zfill(8)
		time.sleep(.2)
	if (GPIO.input(27) == 1 and counter == 255):
		counter = 0
		print bin(counter)[2:].zfill(8)
		time.sleep(.2)
	if (GPIO.input(17) == 1 and counter != 0): #stop decrement inputs if 0
		counter -= 1
		print bin(counter)[2:].zfill(8)
		time.sleep(.2)
	if (GPIO.input(17) == 1 and counter == 0):
		counter = 255
		print bin(counter)[2:].zfill(8)
		time.sleep(.2)
	return
	
def ledLogic(c):
	binaryString = bin(c)[2:].zfill(8)
	for index, value in enumerate(binaryString):
		if (value == '1'):
			ledOn(index)
		else:
			ledOff(index)
	return
	
def ledOn(pin):
	if (pin == 0):
		GPIO.output(13,GPIO.HIGH)
	if (pin == 1):
		GPIO.output(6,GPIO.HIGH)
	if (pin == 2):
		GPIO.output(19,GPIO.HIGH)
	if (pin == 3):
		GPIO.output(26,GPIO.HIGH)
	if (pin == 4):
		GPIO.output(24,GPIO.HIGH)
	if (pin == 5):
		GPIO.output(15,GPIO.HIGH)
	if (pin == 6):
		GPIO.output(18,GPIO.HIGH)
	if (pin == 7):
		GPIO.output(23,GPIO.HIGH)
	
	return
def ledOff(pin):
	if (pin == 0):
		GPIO.output(13,GPIO.LOW)
	if (pin == 1):
		GPIO.output(6,GPIO.LOW)
	if (pin == 2):
		GPIO.output(19,GPIO.LOW)
	if (pin == 3):
		GPIO.output(26,GPIO.LOW)
	if (pin == 4):
		GPIO.output(24,GPIO.LOW)
	if (pin == 5):
		GPIO.output(15,GPIO.LOW)
	if (pin == 6):
		GPIO.output(18,GPIO.LOW)
	if (pin == 7):
		GPIO.output(23,GPIO.LOW)
	return
	
try: 
	while True:
		buttonHandler()
		ledLogic(counter)
except KeyboardInterrupt:
	GPIO.cleanup()
		
