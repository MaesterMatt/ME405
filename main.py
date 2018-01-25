import pyb
import micropython
import time
import encoder_Ng_Kropp_Fitter as encode
import controller_Ng_Kropp_Fitter as controller
import motor_Ng_Kropp_Fitter as driver


self.ctr = controller.MotorController(1,4000)   ##Initializes controller with gain=1 and location = 50
self.motor = driver.MotorDriver()

while True:
    self.actuation = ctr.do_work()
    print("Actuation: " + self.actuation)
    print("Position: " + self.ctr.read())
    self.utime.sleep_ms(100)
