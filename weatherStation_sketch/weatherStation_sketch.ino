/*
 * Weather Station Sketch by Drew Scholz
 * 
 * Samples the wind speed with an Interupt Service Routine
 * 
 */
 
#include <TimerOne.h>
#include <MyPrintf.h>

//#define PIEZOpin A0
#define TWO_MINUTES 120000000

int randNumber;

void setup() 
{
  Serial.begin(9600);

  //pinMode(PIEZOpin, INPUT);
  randomSeed(analogRead(0));
  
  Timer1.initialize(TWO_MINUTES);
  Timer1.attachInterrupt(sampleWeather);
}

void sampleWeather()
{
  //int piezoADC = analogRead(PIEZOpin);
  //double volts = piezoADC / 1023.0 * 5.0;
  randNumber = random(0,15);
  Printf(F("%i\n"), randNumber);
}

void loop()
{
  
}

