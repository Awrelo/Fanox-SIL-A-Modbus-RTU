# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:47:46 2023

@author: efeba
"""

"""Monitoring the line currents of Fanox SIL-A Line Protection Relay - Modbus RTU"""
import minimalmodbus
import numpy as np
import time

instrument = minimalmodbus.Instrument('COM3',157)  # port name, slave address (in decimal)

instrument.serial.baudrate = 38400


instrument.serial.parity   = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 3         # seconds


pw_string = "5555"

instrument.write_string(168, pw_string) # Register 168'e şifre : 5555 yazıldı

"""Read line currents from relevant adresses"""
try:
    while True:
        A_current = instrument.read_float(300) 

        print("A phase current = " + str(A_current))

        B_current = instrument.read_float(302)

        print("B phase current = "+str(B_current))

        C_current = instrument.read_float(304)

        print("C phase current = "+str(C_current))

        I_max = instrument.read_float(308)

        print("Imax = "+str(I_max))
        
        time.sleep(1)

except Exception as e:
    print(e)

except KeyboardInterrupt:
    pass