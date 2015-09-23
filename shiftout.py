import RPi.GPIO as GPIO
from time import sleep as sleep


'''
Defining class to handle shifing data out to shift  register 
OutPin = output pin
ClkPin = clock Pin 
Len = length of data in bytes (default 1 Byte)
Speed = delay between each bit (Default 0.01 sec)
'''

#  Keyword args, ie: def my_function(*args, **kwargs):
# my_instanace = ShiftOut(1,2,outpin=1,blah_blah=1)
# Retrieve with
# kwargs.get('name',default_value)

class ShiftOut():
  def __init__(self, OutPin, ClkPin, ClearPin, ByteLength=1, Speed=0.001):
    self.OutPin = OutPin
    self.ClkPin = ClkPin
    self.ClearPin = ClearPin
    self.ByteLength = ByteLength
    self.Speed = Speed
    self.setpins()
    self.DEBUG = 1
  def setpins(self):
    #Set pin number to BCM
    GPIO.setmode(GPIO.BCM)
    #Set required pins as output 
    GPIO.setup(self.OutPin, GPIO.OUT)
    GPIO.output(self.OutPin, GPIO.LOW)
    
    GPIO.setup(self.ClkPin, GPIO.OUT)
    GPIO.output(self.ClkPin, GPIO.LOW)
    
    GPIO.setup(self.ClearPin, GPIO.OUT)
    GPIO.output(self.ClearPin, GPIO.LOW)
    
  def sendbit(self, Bit):
  
    if(self.DEBUG == 1):
      print('Shiftout' ,Bit)
    #Load Bit to output pin 
    GPIO.output(self.OutPin, Bit)
    #toggle ClockPin

    GPIO.output(self.ClkPin, GPIO.HIGH)

    sleep(self.Speed)

    GPIO.output(self.ClkPin, GPIO.LOW)
    GPIO.output(self.OutPin,GPIO.LOW)

    sleep(self.Speed)
'''
ShiftOut::shiftout(data,length)
Description.....

#Shifts out Number LSB first

Usage....

data = inter 

'''    
  def shiftout(self, data, length = 0):
    bitmask = 0x00
    bytemask = 0x00
    #If Length is not defined then set to default 
    if (length == 0):
      length = self.ByteLength
      
    try:
      for ByteSelector in range(length):
        #select current byte
        bytemask = 0xFF << (ByteSelector * 8 )
        ByteToSend = bytemask & data
        ByteToSend =  ByteToSend >> (ByteSelector * 8)
        if(self.DEBUG == 1):
          print('Byte Mask = ' , bytemask , 'Current Byte = ' ,ByteToSend)

        #bit selector
        for BitSelector in range(8):
          bytemask = 1 << BitSelector
          BitToSend = bytemask & ByteToSend
          BitToSend = BitToSend/bytemask
          self.sendbit(BitToSend)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()


  def reset(self):
    GPIO.output(self.ClearPin, GPIO.HIGH)
    sleep(self.speed)
    GPIO.output(self.ClearPin, GPIO.LOW)
    sleep(self.speed)
    