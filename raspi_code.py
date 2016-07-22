# Code to run purely on the raspberry pi
### 

from sems_api import register_connect_device, send_bluetooth, get_status_text
from time import sleep
import os
import subprocess
import bluetooth

# Changes directory to pi-blaster program, and initializes it
def run_piblaster():
	path = "/home/pi/3M_LED_Pi/pi-blaster"
	os.chdir( path )
	os.system("sudo ./pi-blaster")

# Sends commands to raspi that change its colors
def red():
	
	os.system('echo 17=1 > /dev/pi-blaster')
	os.system('echo 18=0 > /dev/pi-blaster')
	os.system('echo 22=0 > /dev/pi-blaster')

def blue():
	
	os.system('echo 17=0 > /dev/pi-blaster')
	os.system('echo 18=1 > /dev/pi-blaster')
	os.system('echo 22=0 > /dev/pi-blaster')


def green():
	
	os.system('echo 17=0 > /dev/pi-blaster')
	os.system('echo 18=0 > /dev/pi-blaster')
	os.system('echo 22=1 > /dev/pi-blaster')


# Scans for the Bluetooth device with the name listed inside the program
# TO DO: Make the name easier to change
def bluetooth_scan(bt_connected):
	bt_name = "3M"
	bt_addr = None

	nearby_devices = bluetooth.discover_devices()

	for addr in nearby_devices:
		if bt_name == bluetooth.lookup_name( addr ):
			bt_addr = addr
			break

	if bt_addr != None:
		#if not bt_connected:
			#print "found", bt_addr
			#port = 1
			#sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM)
			#sock.connect((bt_addr,port))			

		return True
	else:
		print "Not found!"
		return False
		

# runs on startup
def main():
        run_piblaster()
        
	# connects to the SEMS IoT platform
	headers = register_connect_device()
	bluetooth_status = ''
	
	# So the lights are constantly flickering when status is same 
	previous_status = '' 
	
	# tracks current status: In, Out, Busy
	current_status = ''
	bt_is_present = False
	while True:
		bt_is_present = bluetooth_scan(bt_is_present)
		print "bt_is, " , bt_is_present
		#can't find BT device specified
		if (bt_is_present == False):
			blue()
			bluetooth_status = 'Missing'
		# finds the bluetooth device specified
		else:
			bluetooth_status = 'Present'
			current_status = get_status_text(headers)
			# Only registers status changes, only works when BT present
			if (current_status == "Free" and previous_status != "Free"):
				green()
			elif (current_status == "Out" and previous_status != "Out"):
				blue()
			elif (current_status == "Busy" and previous_status != "Busy"):
				red()
			
		send_bluetooth(bluetooth_status, headers)
		previous_status = current_status
		
	# end while

if __name__ == "__main__": 
	main()


		
			
	
