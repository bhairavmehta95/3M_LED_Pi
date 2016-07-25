from time import sleep
from twilio.rest import TwilioRestClient
import serial

def send_text():
	client = TwilioRestClient('AC77bd11f11e791e4556c18124e4754f84','47f4da483a93fd9ddc6fa84092766340')
	 
	#client.messages.create(from_='+17326390755',
	#					   to='+15865302015',
	#					   body='Hey RJ, you are getting a message!')
						   
	client.messages.create(from_='+17326390755',
						   to='+17326874076',
						   body='Hey Bhairav, you are getting a message!')

def read_serial_arduino():
	ser = serial.Serial('/dev/ttyACM0', 9600)
	while True:
		value = ser.readline()
		print value
		try:
			val_int = int(value)
			if val_int > 30:
				send_text()
				
				while val_int > 30:
					value = ser.readline()
					try:
						val_int = int(value)
					except:
						pass
				print 'sleeping!'
				time.sleep(1)
				ser.flushInput()
				ser.flushOutput()
		except:
			print 'failed to convert', value
			pass


def main():
        read_serial_arduino()



if __name__ == "__main__": 
	main()
