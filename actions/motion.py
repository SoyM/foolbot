import time

wait = 0.15
wait2 = 0.25


class Motion:
    def __init__(self, front_right_body, front_right_leg, front_left_body, front_left_leg, rear_left_body,
                 rear_left_leg,
                 rear_right_body, rear_right_leg):
        self.frontRightBody = front_right_body
        self.frontRightLeg = front_right_leg
        self.frontLeftBody = front_left_body
        self.frontLeftLeg = front_left_leg
        self.rearLeftBody = rear_left_body
        self.rearLeftLeg = rear_left_leg
        self.rearRightBody = rear_right_body
        self.rearRightLeg = rear_right_leg

    # This sets the servos at positions that allow the robot to stand up
    def stand(self):
        self.frontRightBody.write(40)
        self.frontRightLeg.write(0)
        self.frontLeftBody.write(120)
        self.frontLeftLeg.write(0)
        self.rearLeftBody.write(40)
        self.rearLeftLeg.write(0)
        self.rearRightBody.write(120)
        self.rearRightLeg.write(0)
        time.sleep(1)

    # First step when moving forward
    def forwardStep1(self):
        # lift the frontrightLeg, call delay, move the frontrightBody forward by 25 degrees, call delay,
        # move the frontleftBody back by 15 degrees, lower the frontrightLeg
        self.frontRightLeg.write(35)
        time.sleep(wait)
        self.frontRightBody.write(65)
        time.sleep(wait)
        self.frontLeftBody.write(135)
        self.frontRightLeg.write(0)

    # Second step when moving forward
    def forwardStep2(self):
        # lift the rearrightLeg, call delay, move the rearrightBody forward by 35 degrees, call delay,
        # move the rearleftBody back by 35 degrees, lower the rearrightLeg
        self.rearRightLeg.write(35)
        time.sleep(wait)
        self.rearRightBody.write(155)
        time.sleep(wait)
        self.rearLeftBody.write(75)
        self.rearRightLeg.write(0)

        # Third step when moving forward

    def forwardStep3(self):
        # lift the frontleftLeg, call delay, move the frontleftBody forward by 20 degrees, call delay,
        # move the frontrightBody back by 40 degrees, lower the frontleftLeg
        self.frontLeftLeg.write(35)
        time.sleep(wait)
        self.frontLeftBody.write(100)
        time.sleep(wait)
        self.frontRightBody.write(25)
        self.frontLeftLeg.write(0)

        # Fourth step when moving forward

    def forwardStep4(self):
        # lift the rearleftLeg, call delay, move the rearleftBody forward by 50 degrees, call delay,
        # move the rearrightBody back by 65 degrees, lower the rearleftLeg
        self.rearLeftLeg.write(35)
        time.sleep(wait)
        self.rearLeftBody.write(25)
        time.sleep(wait)
        self.rearRightBody.write(90)
        self.rearLeftLeg.write(0)

        # First step when moving backward

    def backStep1(self):
        # lift the rear right leg,call delay, move the rear right body back by 30 degrees,call delay,
        # move the rear left body forward by 15 degrees, lower the rear right leg
        self.rearRightLeg.write(35)
        time.sleep(wait)
        self.rearRightBody.write(90)
        time.sleep(wait)
        self.rearLeftBody.write(25)
        self.rearRightLeg.write(0)

        # Second step when moving backward

    def backStep2(self):
        # lift the front left leg,call delay, move the front left body backward by 15 degrees,call delay,
        #  move the front right body forward by 25 degrees, lower the front left leg
        self.frontLeftLeg.write(35)
        time.sleep(wait)
        self.frontLeftBody.write(135)
        time.sleep(wait)
        self.frontRightBody.write(65)
        self.frontLeftLeg.write(0)

    # Third step when moving backward

    def backStep3(self):
        #  lift the rear left leg, call delay, move the rear left body backward by 50 degrees, call delay,
        # move the rear right body forward by 65 degrees, lower the rear left leg
        self.rearLeftLeg.write(35)
        time.sleep(wait)
        self.rearLeftBody.write(75)
        time.sleep(wait)
        self.rearRightBody.write(155)
        self.rearLeftLeg.write(0)

    # Fourth step when moving backward

    def backStep4(self):
        # lift the front right leg, call delay, move the front right body backward by 40 degrees, call delay,
        # move the front left body forward by 75 degrees, lower the front right leg
        self.frontRightLeg.write(35)
        time.sleep(wait)
        self.frontRightBody.write(25)
        time.sleep(wait)
        self.frontLeftBody.write(100)
        self.frontRightLeg.write(0)

        # First step when turning right

    def rightStep1(self):
        # lift the frontrightLeg, call delay, move the frontrightBody forward by 40 degrees,
        # move the rearrightBody forward by 10 degrees, call delay, lower the frontrightLeg
        self.frontRightLeg.write(35)
        time.sleep(wait2)
        self.frontRightBody.write(80)
        self.rearRightBody.write(130)
        time.sleep(wait2)
        self.frontRightLeg.write(0)

        # Second step when turning right

    def rightStep2(self):
        # move the frontrightBody back by 50 degrees, call delay, keep the rearleftLeg down as a pivot point
        self.frontRightBody.write(30)
        time.sleep(wait2)
        self.rearLeftLeg.write(0)

        # Third step when turning right

    def rightStep3(self):
        # lift the frontleftLeg, call delay, move the frontleftBody back by 10 degrees, call delay,
        # lower the frontleftLeg
        self.frontLeftLeg.write(35)
        time.sleep(wait2)
        self.frontLeftBody.write(130)
        time.sleep(wait2)
        self.frontLeftLeg.write(0)

        # Fourth step when turning right

    def rightStep4(self):
        #  lift the rearrightLeg, call delay, move the rearrightBody back by 50 degrees,
        # move the fronleftBody forward by 10 degrees, call delay, lower the rearrightLeg
        self.rearRightLeg.write(35)
        time.sleep(wait2)
        self.rearRightBody.write(80)
        self.frontLeftBody.write(120)
        time.sleep(wait2)
        self.rearRightLeg.write(0)

        # First step when turning left

    def leftStep1(self):
        # lift the fronleftLeg, call delay, move the frontleftBody forward by 40 degrees,
        # move the rearleftBody forward by 10 degrees, call delay, lower the frontleftLeg
        self.frontLeftLeg.write(35)
        time.sleep(wait2)
        self.frontLeftBody.write(80)
        self.rearLeftBody.write(30)
        time.sleep(wait2)
        self.frontLeftLeg.write(0)

        # Second step when turning left

    def leftStep2(self):
        # move the frontleftBody back by 50 degrees, call delay, keep the rearrightLeg down as a pivot point
        self.frontLeftBody.write(130)
        time.sleep(wait2)
        self.rearRightLeg.write(0)

        # Third step when turning left

    def leftStep3(self):
        # lift the frontrightLeg, call delay, move the frontrightBody forward by 10 degrees, call delay,
        # lower the frontrightLeg
        self.frontRightLeg.write(35)
        time.sleep(wait2)
        self.frontRightBody.write(50)
        time.sleep(wait2)
        self.frontRightLeg.write(0)

        # Fourth step when turning left

    def leftStep4(self):
        # lift the rearleftLeg, call delay, move the rearleftBody backward by 10 degrees,
        # the frontrightBody backward by 20 degrees, call delay, lower the rearleftLeg
        self.rearLeftLeg.write(35)
        time.sleep(wait2)
        self.rearLeftBody.write(90)
        self.frontRightBody.write(30)
        time.sleep(wait2)
        self.rearLeftLeg.write(0)

    # This function causes the robot to move forward

    def forward(self):
        self.forwardStep1()
        self.forwardStep2()
        self.forwardStep3()
        self.forwardStep4()

    # This function causes the robot to move back

    def back(self):
        self.backStep1()
        self.backStep2()
        self.backStep3()
        self.backStep4()

    # This function turns the robot to the right

    def right(self):
        self.rightStep1()
        self.rightStep2()
        self.rightStep3()
        self.rightStep4()

        # This function turns the robot left

    def left(self):
        self.leftStep1()
        self.leftStep2()
        self.leftStep3()
        self.leftStep4()

    # This function causes the robot to wave at a nearby object using its front left leg
    def wave2(self):
        waveCount = 0
        self.frontRightBody.write(90)
        self.frontRightLeg.write(0)
        self.frontLeftBody.write(90)
        self.frontLeftLeg.write(0)
        self.rearLeftBody.write(90)
        self.rearLeftLeg.write(0)
        self.rearRightBody.write(90)
        self.rearRightLeg.write(20)

        while waveCount < 4:
            for servoPosition in range(130, 160):
                self.frontLeftLeg.write(servoPosition)
                time.sleep(10 / 1000)
            for servoPosition in range(160, 130, -1):
                self.frontLeftLeg.write(servoPosition)
                time.sleep(10 / 1000)
            waveCount += 1

    # This function causes the robot to wave at a nearby object using its front right leg

    def wave(self):
        waveCount = 0
        self.frontRightBody.write(90)
        self.frontRightLeg.write(0)
        self.frontLeftBody.write(90)
        self.frontLeftLeg.write(0)
        self.rearLeftBody.write(90)
        self.rearLeftLeg.write(40)
        self.rearRightBody.write(90)
        self.rearRightLeg.write(0)

        while waveCount < 4:
            for servoPosition in range(130, 160):
                self.frontRightLeg.write(servoPosition)
                time.sleep(10 / 1000)

            for servoPosition in range(160, 130, -1):
                self.frontRightLeg.write(servoPosition)
                time.sleep(10 / 1000)

            waveCount += 1

    # This function causes the robot to wave at a nearby object in autonomous mode
    def waveAuto(self):
        waveCount2 = 0

        self.frontRightBody.write(90)
        self.frontRightLeg.write(0)
        self.frontLeftBody.write(90)
        self.frontLeftLeg.write(0)
        self.rearLeftBody.write(90)
        self.rearLeftLeg.write(60)
        self.rearRightBody.write(90)
        self.rearRightLeg.write(0)

        while waveCount2 < 4:
            for servoPosition in range(130, 160):
                self.frontRightLeg.write(servoPosition)
                time.sleep(10 / 1000)
            for servoPosition in range(160, 130, -1):
                self.frontRightLeg.write(servoPosition)
                time.sleep(10 / 1000)

            waveCount2 += 1

        # This function causes the robot to lie down

    def sleep(self):
        self.frontRightBody.write(90)
        self.frontLeftBody.write(90)
        self.rearRightBody.write(90)
        self.rearLeftBody.write(90)
        self.frontRightLeg.write(90)
        self.frontLeftLeg.write(90)
        self.rearRightLeg.write(90)
        self.rearLeftLeg.write(90)

        # This function causes the robot to walk around autonomously,
        #  wave at the first object it sees and adef that object and any others

    def autonomy(self):
        distance = 0
        if distance > 50:
            self.forward()

        # waves at the first object it gets within 50cm of then turns right to adef it and any others in its path
        elif distance < 50:
            self.stand()
            time.sleep(wait)
            self.waveAuto()
            for i in range(0, 2):
                self.right()

            if distance > 30 & distance < 50:
                for i in range(0, 2):
                    self.right()

            # moves backwards if it gets within 30cm of an object
            elif distance < 30:
                for i in range(0, 2):
                    self.back()

    # This function reads the ultrasonic sensor distance and converts it to cm
    def readPing(self):
        return 1
