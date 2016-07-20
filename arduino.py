from time import sleep
from twilio.rest import TwilioRestClient
import serial

def send_text():
		 
	client = TwilioRestClient('AC77bd11f11e791e4556c18124e4754f84','47f4da483a93fd9ddc6fa84092766340')
	 
	client.messages.create(from_='+17326390755',
						   to='+15865302015',
						   body='Hey RJ, you are getting a message!')
						   
	client.messages.create(from_='+17326390755',
						   to='+17326874076',
						   body='Hey Bhairav, you are getting a message!')

# to do: FIX THIS TO MATCH EXACTLY!
def read_serial_arduino():
	ser = serial.Serial('/dev/tty.usbserial', 9600)
	while True:
		value = ser.readline()
		if value == "You're getting a message":
			send_text()
			


