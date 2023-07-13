from machine import Pin
import time,utime

pinSER = Pin(3,Pin.OUT)
pinRCK = Pin(1,Pin.OUT)
pinSCK = Pin(2,Pin.OUT)
pinSER.off()
pinRCK.off()
pinSCK.off()

toggleDate=Pin(25,Pin.IN,Pin.PULL_UP)
time1 = utime.localtime()

#   0 1 2 3 4 5 6 7 8 9 sp ° C
bA=[1,0,1,1,0,1,1,1,1,1,0, 1,1]
bB=[1,1,1,1,1,0,0,1,1,1,0, 1,0]
bC=[1,1,0,1,1,1,1,1,1,1,0, 0,0]
bD=[1,0,1,1,0,1,1,0,1,1,0, 0,1]
bE=[1,0,1,0,0,0,1,0,1,0,0, 0,1]
bF=[1,0,0,0,1,1,1,0,1,1,0, 1,1] 
bG=[0,0,1,1,1,1,1,0,1,1,0, 1,0]
def set595(s,c):
    s=(s<<12)|0X000000aaa
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
dot = 0b010100000
def DEC2BCD(dec):
    return int(dec+int(dec/10)*6)
while True:
    time1 = utime.localtime()
    print("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}".format(
year=time1[0], month=time1[1], day=time1[2],
HH=time1[3], MM=time1[4], SS=time1[5]))
    print(hex(DEC2BCD(time1[5])))
    set595((DEC2BCD(time1[3])<<16)|(DEC2BCD(time1[4])<<8)|DEC2BCD(time1[5]),dot)
    if dot ==0b010100000:
        dot = 0
    else:
        dot = 0b010100000
    time.sleep(0.5)