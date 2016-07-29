#include <CapacitiveSensor.h>


/* 
 *  Description:
 *  A program to function with a capacititive sensor as well as the CapSense C++/C/Arduino Library
 *  The program can sense the application and removal of post its on specified boards, and can be 
 *  easily modified for other uses as well
 *  
 *  Calibrated for a 1M Ohm sensor and Arduino Uno Board
 *  
 */

CapacitiveSensor   cs_4_6 = CapacitiveSensor(4,6);        // 10M resistor between pins 4 & 6, pin 6 is sensor pin, add a wire and or foil


// An average_arr array, will hold the last ten values of "noise" readings
// Will help with recalibration
int average_arr[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int counter = 0;

// Booleans to help with flow of program
int removed  = 0;
int posted = 0;  

void setup()                    
{
//   cs_4_6.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 2 - just as an example
   Serial.begin(9600);
}

// function that returns average of the global array 'average_arr'
double return_average(){
  int sum = 0;
  for (int i = 0; i < 10; ++i){
    sum += average_arr[i];
  }

  return sum / sizeof(average_arr);
}

// Function that recalibrates after each post it is removed/attached
// Future: Pass in a sensor ID
void recalibrate_sensor(){
    cs_4_6.reset_CS_AutoCal();
    for (int i = 0; i < 10; ++i){
      average_arr[i] = -1;
    }
    counter = 0;
}

void loop()                    
{
    // time and sensor readings
    long start = millis();
    long reading = 0;

    // gets an average of ten readings
    for (int i = 0; i < 10; ++i){
      reading += cs_4_6.capacitiveSensor(30);
    }
    reading /= 10;

    
    bool initializing = false;
    
    // populates average_arr array if not initialized, continues
    if (average_arr[counter] == -1){
      average_arr[counter] = reading;
      counter += 1;
      counter = counter % 10;
    }

    // gets average of average_arr
    int average = return_average();
    Serial.println(reading);
    
    if (average > 30){ //&& !initializing){
      recalibrate_sensor();
    }

    
    /* else if (!initializing){
      // arbitrary thresholds
      if (reading > 40){
        //Serial.print("Message");
        posted += 1;
        // reading away junk data
        long time_start = millis();
        while (reading > 40){
          reading = cs_4_6.capacitiveSensor(30);
        }

        // 5 second delay between next signal
        delay(6000);
        
        // recalibrate
        recalibrate_sensor();
      } */

     /* else if (reading > 150){
        Serial.println("Post it removed!");
        removed += 1;

        long time_start = millis();
        // half reading away junk data, 3 second timeout
        while (reading > 200){
          if (time_start - millis() > 3000) break;
          reading = cs_4_6.capacitiveSensor(30);
        }

        // second delay between next signal
        time_start = millis();
        while (millis() - time_start < 1000){
          // do nothing
        }

        // recalibrate
        recalibrate_sensor();
      }*/
  
      // delay to limit data to serial port
      delay(100);

      // update average_arr values & counter
      average_arr[counter] = reading;  
      counter += 1;
      counter = counter % 10;
    } 

                       

