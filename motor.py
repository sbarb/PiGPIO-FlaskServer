from RPIO import PWM

servo = PWM.Servo()

# Set servo on GPIO17 to 1200micros (1.2ms)
servo.set_servo(7, 1200)

# Set servo on GPIO17 to 2000mocros (2.0ms)
servo.set_servo(7, 2000)

# Clear servo on GPIO17
servo.stop_servo(7)
