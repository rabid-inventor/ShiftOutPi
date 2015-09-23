# ShiftOutPi
Python Module for creating GPIO SerialIn/ParallelOut Shift Register instances on the Raspberry Pi and 74HC164 SR

# Usage:

#Import Module
import shiftout

#Create instace ( can be used several times to create multipule instances) 
MyShiftReg = shiftout(DataPin, ClockPin, ResetPin, DefaultByteLength, TimeBetweenClockPulses)

#Send data to shift Register
MyShiftReg.shiftout(Data, DataLength)

#Clear Shift Register
MyShiftReg.reset()

also check example.py for further usage 
