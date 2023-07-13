from machine import I2C
from machine import Pin
import time,utime
import random

machine.freq(240000000)

pinSER = Pin(11,Pin.OUT)
pinRCK = Pin(13,Pin.OUT)
pinSCK = Pin(15,Pin.OUT)
pinSER.off()
pinRCK.off()
pinSCK.off()
#vccP=Pin(6,Pin.OUT)
#vccP.on()
vccP=Pin(9,Pin.OUT)
vccP.on()
vccD=Pin(0,Pin.OUT)
vccD.on()
#不需要使用GPIO作为电源时请注释掉以上4行
toggleDate=Pin(25,Pin.IN,Pin.PULL_UP)
address = 0x68
register = 0x00
maohao1=Pin(22,Pin.OUT)
maohao1.toggle()
maohao2=Pin(23,Pin.OUT)
#sec min hour week day mout year
NowTime = b'\x20\x26\x13\x03\x15\x06\x22'
w  = ["周日","周一","周二","周三","周四","周五","周六"];
bus=I2C(1,scl=Pin(3),sda=Pin(2))
print(bus.scan())
print(bus)
def ds3231SetTime():
    bus.writeto_mem(int(address),int(register),NowTime)
def ds3231ReadTime():
    return bus.readfrom_mem(int(address),int(register),19);

#   0 1 2 3 4 5 6 7 8 9 sp ° C
bA=[1,0,1,1,0,1,1,1,1,1,0, 1,1]
bB=[1,1,1,1,1,0,0,1,1,1,0, 1,0]
bC=[1,1,0,1,1,1,1,1,1,1,0, 0,0]
bD=[1,0,1,1,0,1,1,0,1,1,0, 0,1]
bE=[1,0,1,0,0,0,1,0,1,0,0, 0,1]
bF=[1,0,0,0,1,1,1,0,1,1,0, 1,1]
bG=[0,0,1,1,1,1,1,0,1,1,0, 1,0]
def set595(s,c):
    s=(s<<12)|0X000000AAA
    for j in range(9):
        ms = (s & (0xF << (4*j))) >> 4*j
        pinSER.value((c>>j)&0b1)
        pinSCK.value(1)
        pinSCK.value(0)
        pinSER.value(bG[ms])
        pinSCK.value(1)
        pinSCK.value(0)
        pinSER.value(bF[ms])
        pinSCK.value(1)
        pinSCK.value(0)
        pinSER.value(bE[ms])
        pinSCK.value(1)
        pinSCK.value(0)
        pinSER.value(bD[ms])
        pinSCK.value(1)
        pinSCK.value(0)
        pinSER.value(bC[ms])
        pinSCK.value(1)
        pinSCK.value(0)
        pinSER.value(bB[ms])
        pinSCK.value(1)
        pinSCK.value(0)
        pinSER.value(bA[ms])
        pinSCK.value(1)
        pinSCK.value(0)
    pinRCK.value(1)
    pinRCK.value(0)
mDateMenu=0
def irqDateMenu(toggleDate):
    global mDateMenu
    if toggleDate.value() == 1:
        #time.sleep(0.1)
        mDateMenu = mDateMenu + 1
        if mDateMenu ==4:
            mDateMenu = 0
        print("irq1")
    print("irq2")
toggleDate.irq(irqDateMenu,Pin.IRQ_RISING)
def getDateTime(i):
    mt = ds3231ReadTime()
    if i == 0:
        return [(mt[2]<<16) | (mt[1]<<8) | mt[0],0]
    if i == 1:
        return [0xAA2000 | mt[6],0]
    if i == 2:
        return [0xA00A00 | ((mt[5]&0x1F)<<12) | (mt[4]&0x3F),0]
    if i == 3:
        mTemp = int((mt[17]+(mt[18]>>6)*0.25)*100)
        return [(b2d(mTemp)<<8)|0xBC,0x80]

def b2d(dec):
    return int(dec+int(dec/10)*6)

while 1:
    #mDate = getDateTime(mDateMenu)
    #set595(mDate[0],mDate[1])
    set595(((b2d(time.gmtime()[5])<<0) | (b2d(time.gmtime()[4])<<8) | (b2d(time.gmtime()[3]))<<16),0)
    maohao1.toggle()
    maohao2.toggle()
    time.sleep(0.05)