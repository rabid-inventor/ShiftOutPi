from shiftout import *
from time import sleep as sleep

sr1 = ShiftOut(17,27,4,2)

try:
  while 1:
    '''
    for i in range(0xFFFF):
      sr1.shiftout(i)
      sleep(0.01)
    '''
    sr1.shiftout(32768)
    sleep(0.5)
    sr1.reset()
	
except KeyboardInterrupt:
  exit()

