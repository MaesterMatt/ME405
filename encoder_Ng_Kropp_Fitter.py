##
#    This file contains a motor encoder which initializes and measures how far the motor has gone

import pyb
import micropython
import time

__author__= "Matthew Ng, Eugene Kropp, Yavisht Fitter"
__date__= "January 18, 2018"

class MotorEncoder:
    ''' Motor Encoder Class: Has a function to read and reset motor position counter '''
    def __init__(self):
        '''Creates a motor encoder by initializing GPIO pins and setting position to zero'''
        self.pinB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN, pull=pyb.Pin.PULL_NONE, af=2)   
        self.pinB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN, pull=pyb.Pin.PULL_NONE, af=2)
        self.timEncoder = pyb.Timer(4, prescaler=0, period=0xffff)
        ch1 = self.timEncoder.channel(1, pyb.Timer.ENC_AB, pin=self.pinB6)
        ch2 = self.timEncoder.channel(2, pyb.Timer.ENC_AB, pin=self.pinB7)
        self.current_count = self.timEncoder.counter()
        self.delta_count = 0
        self.position = 0

    def cal_delta(self):
        '''This function calculates the change in motor rotations while preventing the count from overflowing'''  
        self.last_count = self.current_count
        self.current_count = self.timEncoder.counter()
        self.delta_count = self.current_count - self.last_count
        if abs(self.delta_count) > 32000:    ##encoder overflows at uint16 max, 65535
            self.delta_count -= 65535*self.delta_count/abs(self.delta_count)    ##adjusts overflow by uint16 max
        return int(self.delta_count)

    def zero(self):
        '''This function zeros the position of the motor'''
        self.position = 0   ##Resets the postion back to 0

    def read(self):
        '''This function calculates and returns the position of the motor'''
        self.position = self.position + self.cal_delta()
        return self.position    ##Returns the current postion of motor


        
