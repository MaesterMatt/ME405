import pyb
import micropython
import utime
import time
import controller_Ng_Kropp_Fitter as controller


ctr = controller.MotorController(1,4000)   ##Initializes controller with gain=1 and location = 50

while True:
    actuation = ctr.do_work()
    utime.sleep_ms(100)
