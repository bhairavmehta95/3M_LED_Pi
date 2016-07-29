# 3M_LED_Pi
Code to run on Raspberry Pi that works with 3M_LEDIndicator


## Things You Will Need:

* Raspberry Pi (Bluetooth and Wifi Capabilities - either RPi 3 or RPi2 + Add In Transmitters)
* Breadboard
* Three transistors
* Wires
* RGB LED Strip
* Power to LEDs and Power to RPi

## Steps to Install - Hardware

* Build circuit (see below)

## Steps to Install - Software

* Run install.sh
* Configure user variables (i.e what Username to look for in DB -- See code for more details)

After configuring user variables, that is what the device will look for in the database. Be sure to use your 3M A-number in all capitals. An example is present in the code.

## To Run

The program should run automatically on startup (assuming install.sh ran with no problems), but after installation, if further work is required, run:

'''
python

python raspi_code.py

'''


## Circuit

** Note: The 'section' of the breadboard below will need to be reproduced for each R, G, and B channel. **
* Connect the power of the LED to the + terminal of the breadboard
* Connect the power source into the + and - terminals of the breadboard (_polarity is important_)
* Connect ground pin of RPi and connect it to the ground on the breadboard

Take a transitor (this tutorial is written using an N-Channel FQP MOSFET, so if using P-Channel, adjust G,D,S accordingly) 

For an N-Channel MOSFET, the Pins are arranged as Gate, Drain, and Source in that order when looking at the MOSFET from the front.

Gate - Connected to Pin that goes to Raspberry Pi -- The code is configured to use Pins 17, 18, and 22.

Drain - Connected to the R,G, or B wire of the LED

Source - Connected to ground

Power up your device and you will have a working LED Indicator!

## Troubleshooting

* Wifi not connected
  * 3MGuest should work, 3M GlobalSecure has problems authenticating the Raspberry Pi

* BT not connected
  * Be sure that the BT modules from install.sh were installed correctly

* Lights not changing
  * Check connections

* One color is always on
  * Check connections, particularly the one to ground


  
