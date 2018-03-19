#include <Servo.h>
#include <NewPing.h>

#define TRIG_PIN A0 
#define ECHO_PIN A1 
#define MAX_DISTANCE 10000 

// used as the delay between steps when the robot is moving forward or backward
const int wait = 150;
// used as the delay between steps when the robot is turning right or left
const int wait2 = 250;

NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE); 

// defines a variable that will be used to toggle the autonomy function for the robot
bool autoMove = false;

// Define the servos 
Servo frontrightBody;
Servo frontrightLeg;
Servo frontleftBody;
Servo frontleftLeg;
Servo rearleftBody;
Servo rearleftLeg;
Servo rearrightBody;
Servo rearrightLeg;

int servoPosition;
int distance = 0;
int waveCount = 0;
int waveCount2 = 0;
                  

void setup()
{
  // Attach the servos to their respective pins on the shield and initialize their position. The robot is set to lie down at this point
  frontrightBody.attach(6);
  frontrightBody.write(40);
  frontrightLeg.attach(7);
  frontrightLeg.write(90);
  frontleftBody.attach(8);
  frontleftBody.write(120);
  frontleftLeg.attach(9);
  frontleftLeg.write(90);
  rearleftBody.attach(10);
  rearleftBody.write(40);
  rearleftLeg.attach(11);
  rearleftLeg.write(90);
  rearrightBody.attach(4);
  rearrightBody.write(120);
  rearrightLeg.attach(5);
  rearrightLeg.write(90);

  Serial.begin(9600);
}

/*
 * The loop reads in characters from the serial monitor and performs the respective functions and also returns the distance 
 * read by the ultrasonic sensor
 */
void loop()
{
   distance = readPing();
   Serial.println(distance);
   if ( Serial.available()) 
   {
      char ch = Serial.read();
      if (ch == 'f')
      {
        forward ();
        Serial.println(distance);
      }

      if (ch == 'b')
      {
        back ();
        Serial.println(distance);
      }

      if (ch == 'r')
      {
        right ();
        Serial.println(distance);
      }

      if (ch == 'l')
      {
        left ();
        Serial.println(distance);
      }

      if (ch == 'w')
      {
        wave ();
        stand ();
        wave2 ();
        stand ();
        Serial.println(distance);
      }

      if (ch == 's')
      {
        sleep ();
        Serial.println(distance);
      }

      if (ch == 'u')
      {
        stand ();
        Serial.println(distance);
      }

      // Pressing a once causes the robot to begin moving autonomously, and pressing it again causes the robot to stop
      if (ch == 'a')
      {
          if (!autoMove)
          {
            waveCount2 = 0;
            autoMove = true;
          }
          else 
          {
            autoMove = false;
          }
       }
   }
          if (autoMove)
          {
              autonomy ();
              Serial.println(distance);
          }
          
}
  
