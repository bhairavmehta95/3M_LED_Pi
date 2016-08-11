# 3M_LED_Pi
Code to run on Raspberry Pi that works with 3M_LEDIndicator

**Note: This IoT-enabled device works best if after setup, the _device is constantly powered on_**.

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

[Check out the wiki page on setup here] (https://github.com/bhairavmehta95/3M_LED_Pi/wiki/Step-by-Step-Set-Up).

* Open up terminal, and type:
``` git clone https://github.com/bhairavmehta95/3M_LED_Pi ```
* When prompted, login with a user who is permitted to clone that repository
* In the same terminal (when the clone is finished), type:
``` cd 3M_LED_Pi ```
* Configure the _raspi_code.py_ file with the correct device-id and Bluetooth name of your phone
* Run install.sh
* Connect to the internet
* Run (if not already running)
``` python raspi_code.py```

After configuring device variables, that is what the device will look for in the database. 

**Note**: There are still some things that need to be fixed per user:

* Twillio needs to be configured with that user's phone number
* If the user has an iOS device, BT is unlikely to be reliable.


## To Run

The program should run automatically (assuming install.sh ran with no problems), but after installation, if further work is required, run:

```
python raspi_code.py
```

You will also need to run this command if at any time the Raspberry Pi turns off, as you will need to reconnect to 3MGuest and start the script again.

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
  
* Pi turned off, and now it doesn't work
  * You have to restart the code on the Raspberry Pi. Please contact SEMS.


  
