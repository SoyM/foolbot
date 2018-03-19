from __future__ import division
import time

import pca9685


# Uncomment to enable debug output.
import logging
logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = pca9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 52       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
#    pwm.set_pwm(0, 0, servo_min)
#    print("min")
#    time.sleep(1)
#    pwm.set_pwm(1, 0, servo_min)
#    time.sleep(1)
#    pwm.set_pwm(1, 0, servo_max)
#    time.sleep(1)
#    pwm.set_pwm(0, 0, servo_max)
#    time.sleep(1)
#    distance = readPing();
#    Serial.println(distance);
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