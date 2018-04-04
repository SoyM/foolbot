class Servo:
    def __init__(self, channel):
        self.channel = channel
        self.angle = 0
        # Initialise the PCA9685 using the default address (0x40).
        # Alternatively specify a different address and/or bus:
        # pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
        self.pwm = pca9685.PCA9685()

        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(50)

        self.servo_min = 150  # Min pulse length out of 4096
        self.servo_max = 600  # Max pulse length out of 4096

    def write(self, angle):
        self.angle = angle
        self.set_servo_angle(self.channel, self.angle)
        # print("channel:{0},angle:{1}".format(self.channel, self.angle))

    def set_servo_angle(self, channel, angle):
        pulse = angle * 5
        pulse //= 2
        pulse += 150
        self.pwm.set_pwm(channel, 0, pulse)
        # print(pulse)

    def move_extreme(self):
        self.write(self.servo_min)
        time.sleep(1)
        self.write(self.servo_max)
        time.sleep(1)

    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000  # 1,000,000 us per second
        pulse_length //= 52  # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096  # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm(channel, 0, pulse)