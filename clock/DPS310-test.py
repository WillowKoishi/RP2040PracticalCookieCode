from machine import I2C
from machine import Pin
import time,utime

time.sleep(0.5)
dps = I2C(1,scl=Pin(3),sda=Pin(2))
dps.scan()
def writeDPS(register,data):
    dps.writeto_mem(int(0x77),int(register),data)
def readDPS():
    return dps.readfrom_mem(int(0x77),int(0x00),6);
while True:
    mData = readDPS()
    mPSR = (mData[0]<<16) | (mData[0]<<8) | mData[0]
    print(mPSR)