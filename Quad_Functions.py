/* 
 *  This sets the servos at positions that allow the robot to stand up
 */
void stand()
{
  frontrightBody.write(40);
  frontrightLeg.write(0);
  frontleftBody.write(120);
  frontleftLeg.write(0);
  rearleftBody.write(40);
  rearleftLeg.write(0);
  rearrightBody.write(120);
  rearrightLeg.write(0);

  delay (1000);
}

/*
 * First step when moving forward
 */
void forwardStep1 ()
{
  // lift the frontrightLeg, call delay, move the frontrightBody forward by 25 degrees, call delay, move the frontleftBody back by 15 degrees, lower the frontrightLeg
  frontrightLeg.write (35);
  delay (wait);
  frontrightBody.write (65);
  delay (wait);
  frontleftBody.write (135);
  frontrightLeg.write (0);
}

/*
 * Second step when moving forward
 */
void forwardStep2 ()
{
   // lift the rearrightLeg, call delay, move the rearrightBody forward by 35 degrees, call delay, move the rearleftBody back by 35 degrees, lower the rearrightLeg
  rearrightLeg.write (35);
  delay (wait);
  rearrightBody.write (155);
  delay (wait);
  rearleftBody.write (75);
  rearrightLeg.write (0);
}

/*
 * Third step when moving forward
 */
void forwardStep3 ()
{
  // lift the frontleftLeg, call delay, move the frontleftBody forward by 20 degrees, call delay, move the frontrightBody back by 40 degrees, lower the frontleftLeg
  frontleftLeg.write (35);
  delay (wait);
  frontleftBody.write (100);
  delay (wait);
  frontrightBody.write (25);
  frontleftLeg.write (0);
}

/*
 * Fourth step when moving forward
 */
void forwardStep4 ()
{
  // lift the rearleftLeg, call delay, move the rearleftBody forward by 50 degrees, call delay, move the rearrightBody back by 65 degrees, lower the rearleftLeg
  rearleftLeg.write (35);
  delay (wait);
  rearleftBody.write (25);
  delay (wait);
  rearrightBody.write (90);
  rearleftLeg.write (0);
}

/*
 * First step when moving backward
 */
void backStep1 ()
{
  // lift the rear right leg,call delay, move the rear right body back by 30 degrees,call delay, move the rear left body forward by 15 degrees, lower the rear right leg
  rearrightLeg.write (35);
  delay (wait);
  rearrightBody.write (90);
  delay (wait);
  rearleftBody.write (25);
  rearrightLeg.write (0);
}

/*
 * Second step when moving backward
 */
void backStep2 ()
{
  // lift the front left leg,call delay, move the front left body backward by 15 degrees,call delay, move the front right body forward by 25 degrees, lower the front left leg
  frontleftLeg.write (35);
  delay (wait);
  frontleftBody.write (135);
  delay (wait);
  frontrightBody.write (65);
  frontleftLeg.write (0);
}

/*
 * Third step when moving backward
 */
void backStep3 ()
{
  // lift the rear left leg, call delay, move the rear left body backward by 50 degrees, call delay, move the rear right body forward by 65 degrees, lower the rear left leg
  rearleftLeg.write (35);
  delay (wait);
  rearleftBody.write (75);
  delay (wait);
  rearrightBody.write (155);
  rearleftLeg.write (0);
}

/*
 * Fourth step when moving backward
 */
void backStep4 ()
{  
  // lift the front right leg, call delay, move the front right body backward by 40 degrees, call delay, move the front left body forward by 75 degrees, lower the front right leg
  frontrightLeg.write (35);
  delay (wait);
  frontrightBody.write (25);
  delay (wait);
  frontleftBody.write (100);
  frontrightLeg.write (0);
}

/*
 * First step when turning right
 */
void rightStep1 ()
{
  // lift the frontrightLeg, call delay, move the frontrightBody forward by 40 degrees, move the rearrightBody forward by 10 degrees, call delay, lower the frontrightLeg
  frontrightLeg.write (35);
  delay (wait2);
  frontrightBody.write (80);
  rearrightBody.write (130);
  delay (wait2);
  frontrightLeg.write (0);
}

/*
 * Second step when turning right
 */
void rightStep2 ()
{
  // move the frontrightBody back by 50 degrees, call delay, keep the rearleftLeg down as a pivot point
  frontrightBody.write (30);
  delay (wait2);
  rearleftLeg.write (0);
}

/*
 * Third step when turning right
 */
void rightStep3 ()
{
  // lift the frontleftLeg, call delay, move the frontleftBody back by 10 degrees, call delay, lower the frontleftLeg
  frontleftLeg.write (35);
  delay (wait2);
  frontleftBody.write (130);
  delay (wait2);
  frontleftLeg.write (0);
}

/*
 * Fourth step when turning right
 */
void rightStep4 ()
{  
  // lift the rearrightLeg, call delay, move the rearrightBody back by 50 degrees, move the fronleftBody forward by 10 degrees, call delay, lower the rearrightLeg
  rearrightLeg.write (35);
  delay (wait2);
  rearrightBody.write (80);
  frontleftBody.write (120);
  delay (wait2);
  rearrightLeg.write (0);
}

/*
 * First step when turning left
 */
void leftStep1 ()
{
  // lift the fronleftLeg, call delay, move the frontleftBody forward by 40 degrees, move the rearleftBody forward by 10 degrees, call delay, lower the frontleftLeg
  frontleftLeg.write (35);
  delay (wait2);
  frontleftBody.write (80);
  rearleftBody.write (30);
  delay (wait2);
  frontleftLeg.write (0);
}

/*
 * Second step when turning left
 */
void leftStep2 ()
{
  // move the frontleftBody back by 50 degrees, call delay, keep the rearrightLeg down as a pivot point 
  frontleftBody.write (130);
  delay (wait2);
  rearrightLeg.write (0);
}

/*
 * Third step when turning left
 */
void leftStep3 ()
{
  // lift the frontrightLeg, call delay, move the frontrightBody forward by 10 degrees, call delay, lower the frontrightLeg
  frontrightLeg.write (35);
  delay (wait2);
  frontrightBody.write (50);
  delay (wait2);
  frontrightLeg.write (0);
}

/*
 * Fourth step when turning left
 */
void leftStep4 ()
{  
  // lift the rearleftLeg, call delay, move the rearleftBody backward by 10 degrees, the frontrightBody backward by 20 degrees, call delay, lower the rearleftLeg
  rearleftLeg.write (35);
  delay (wait2);
  rearleftBody.write (90);
  frontrightBody.write (30);
  delay (wait2);
  rearleftLeg.write (0);
}

/*
 *This function causes the robot to move forward
 */
void forward()
{
  forwardStep1 ();
  forwardStep2 ();
  forwardStep3 ();
  forwardStep4 ();
}

/*
 *This function causes the robot to move back
 */
void back()
{
  backStep1 ();
  backStep2 ();
  backStep3 ();
  backStep4 ();
}

/*
 *This function turns the robot to the right 
 */
void right()
{
  rightStep1 ();
  rightStep2 ();
  rightStep3 ();
  rightStep4 ();
}

/*
 * This function turns the robot left
 */
void left ()
{
  leftStep1 ();
  leftStep2 ();
  leftStep3 ();
  leftStep4 ();
}

/*
 *This function causes the robot to wave at a nearby object using its front left leg
 */
void wave2 ()
{
  waveCount = 0;
  frontrightBody.write(90);
  frontrightLeg.write(0);
  frontleftBody.write(90);
  frontleftLeg.write(0);
  rearleftBody.write(90);
  rearleftLeg.write(0);
  rearrightBody.write(90);
  rearrightLeg.write(20);
  
  while (waveCount < 4)
  {
    for (servoPosition = 130; servoPosition <= 160; servoPosition++)
    {
      frontleftLeg.write(servoPosition);
      delay (10);
    }
    for (servoPosition = 160; servoPosition >= 130;servoPosition--)
    {
      frontleftLeg.write(servoPosition);
      delay (10);
    }
    waveCount++;
  }
}

/*
 *This function causes the robot to wave at a nearby object using its front right leg
 */
void wave ()
{
  waveCount = 0;
  frontrightBody.write(90);
  frontrightLeg.write(0);
  frontleftBody.write(90);
  frontleftLeg.write(0);
  rearleftBody.write(90);
  rearleftLeg.write(40);
  rearrightBody.write(90);
  rearrightLeg.write(0);
  
  while (waveCount < 4)
  {
    for (servoPosition = 130; servoPosition <= 160; servoPosition++)
    {
      frontrightLeg.write(servoPosition);
      delay (10);
    }
    for (servoPosition = 160; servoPosition >= 130;servoPosition--)
    {
      frontrightLeg.write(servoPosition);
      delay (10);
    }
    waveCount++;
  }
}

/*
 *This function causes the robot to wave at a nearby object in autonomous mode
 */
void waveAuto ()
{
  frontrightBody.write(90);
  frontrightLeg.write(0);
  frontleftBody.write(90);
  frontleftLeg.write(0);
  rearleftBody.write(90);
  rearleftLeg.write(60);
  rearrightBody.write(90);
  rearrightLeg.write(0);
  
  while (waveCount2 < 4)
  {
    for (servoPosition = 130; servoPosition <= 160; servoPosition++)
    {
      frontrightLeg.write(servoPosition);
      delay (10);
    }
    for (servoPosition = 160; servoPosition >= 130;servoPosition--)
    {
      frontrightLeg.write(servoPosition);
      delay (10);
    }
    waveCount2++;
  }
}

/*
 * This function causes the robot to lie down
 */
void sleep() 
{
  frontrightBody.write (90);
  frontleftBody.write (90);
  rearrightBody.write (90);
  rearleftBody.write (90);
  frontrightLeg.write (90);
  frontleftLeg.write (90);
  rearrightLeg.write (90);
  rearleftLeg.write (90);
}

/*
 * This function causes the robot to walk around autonomously, wave at the first object it sees and avoid that object and any others 
 */
void autonomy ()
{
   distance = readPing();
   if (distance > 50)
   {
     forward (); 
   }
   // waves at the first object it gets within 50cm of then turns right to avoid it and any others in its path
   else if (distance < 50)
   {
     stand ();
     delay (wait);
     waveAuto ();
     for (int i = 0; i < 3; i++)
     {
        right ();
     }
     if ((distance > 30)&&(distance < 50))
     {
       for (int i = 0; i < 3; i++)
       {
        right ();
       }
     }
     // moves backwards if it gets within 30cm of an object
     else if (distance < 30)
     {
       for (int i = 0; i < 3; i++)
       {
          back ();
       }
     }
   }
}

/* 
 *This function reads the ultrasonic sensor distance and converts it to cm
 */
int readPing() 
{ 
  delay(70);
  unsigned int uS = sonar.ping();
  int cm = uS/US_ROUNDTRIP_CM;
  return cm;
}

