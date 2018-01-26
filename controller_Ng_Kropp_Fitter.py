##
# Description: This class performs closed-loop proportional control for a motor


import pyb
import micropython
import time
import utime

__author__= "Matthew Ng, Eugene Kropp, Yavisht Fitter"
__date__= "January 25,2018"

class MotorController:
    '''Motor Controller Class: Has a function to perform closed loop control by adjusting gain and initial setpoint.'''

    def __init__(self, gain, location):
        '''Creates a motor controller by initializing gain and setpoint. @param gain does something. @param setpoint sets the desired location'''
        self.kp = gain    ## units are %/encoder unit
        self.setpoint = location
        self.error = self.setpoint
        self.actuation_signal = self.kp*self.error
        self.data = []

    def set_setpoint(self, location):
        '''This function sets the setpoint'''
        self.data = []
        self.setpoint = location

    def set_gain(self, gain):
        '''This function sets the control gain'''
        self.kp = gain

    def err_calc(self, enc_read):
        self.error = self.setpoint - enc_read
        return self.error
    
    def do_work(self):
        '''This function runs the control algorithm. Returns actuation signal.'''
        self.actuation_signal = self.kp*self.error    ##needs to be b/w 0-100
        if abs(self.error) < 50:
            self.actuation_signal = 0
        
        self.write_data()
        return self.actuation_signal

    def write_data(self):
        self.data.append([utime.ticks_ms(), self.actuation_signal])

    def return_data(self):
        return self.data

