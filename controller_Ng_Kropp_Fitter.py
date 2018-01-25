##
# Description: This class performs closed-loop proportional control for a motor


import pyb
import micropython
import time
import encoder_Ng_Kropp_Fitter as encode
import motor_Ng_Kropp_Fitter as driver

__author__= "Matthew Ng, Eugene Kropp, Yavisht Fitter"
__date__= "January 25,2018"

class MotorController:
    '''Motor Controller Class: Has a function to perform closed loop control by adjusting gain and initial setpoint.'''

    def __init__(self, gain, location):
        '''Creates a motor controller by initializing gain and setpoint. @param gain does something. @param setpoint sets the desired location'''
        self.enc = encode.MotorEncoder()
        self.motor = driver.MotorDriver()
        self.kp = gain    ## units are %/encoder unit
        self.setpoint = location
        self.error = self.setpoint - self.enc.read()
        self.actuation_signal = self.kp*self.error

    def set_setpoint(self, location):
        '''This function sets the setpoint'''
        self.setpoint = location

    def set_gain(self, gain):
        '''This function sets the control gain'''
        self.kp = gain

    def do_work(self):
        '''This function runs the control algorithm. Returns actuation signal.'''
        self.error = self.setpoint - self.enc.read()
        self.actuation_signal = self.kp*self.error    ##needs to be b/w 0-100
        if self.error < 100:
            self.actuation_signal = 0
        ##utime.sleep_ms(10)
        self.motor.set_duty_cycle(42)
        #self.motor.set_duty_cycle(self.actuation_signal)
        print(self.actuation_signal)
        return self.actuation_signal

