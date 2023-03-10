# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 18:15:54 2023

@author: efeba
"""

"""Controlling the output contacts of the Fanox SIL-A Line Protection Relay"""

#Imports
import minimalmodbus
import numpy as np
import time

fanox_relay = minimalmodbus.Instrument('COM3',157)  # port name, slave address (in decimal)

fanox_relay.serial.baudrate = 38400 # Baudrate 

#Serial comm.  parameters
fanox_relay.serial.parity   = minimalmodbus.serial.PARITY_NONE 
fanox_relay.serial.stopbits = 1
fanox_relay.serial.timeout  = 3         # seconds


pw_string = "5555" #Password to access the relay

fanox_relay.write_string(168, pw_string) # Password '5555' is written to register address 168

""" Command 'Open Breaker' is sent to the register address 182"""

fanox_relay.write_register(registeraddress = 182, value = 2, functioncode=16 ) 

""" Command 'Reset' is sent to the register address 182"""

fanox_relay.write_register(registeraddress = 182, value = 8, functioncode=16 ) 