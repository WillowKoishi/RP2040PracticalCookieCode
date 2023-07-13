from utime import sleep_us, time
import time
from machine import Pin
machine.freq(280000000)
vcc = Pin(5,Pin.OUT)
vcc.on()
gnd = Pin(2,Pin.OUT)
gnd.off()
sck=Pin(4,Pin.OUT)
sda=Pin(3,Pin.IN)
time.sleep(2)
def read711():
    raw_data = 0
    while sda.value()==1:
        time.sleep(0)
    if 1:
        time.sleep(0.001)
        for i in range(24):
            sck.value(1)
            raw_data = (raw_data << 1 )| sda.value()
            sck.value(0)
        sck.value(1)
        sck.value(0)
    return raw_data ^ 0x800000
sumdata=0
for i in range(80):
    sumdata=sumdata+read711()
value0 = sumdata/80
while True:
    c=time.ticks_ms()
    sumdata=0
    for i in range(80):
        sumdata=sumdata+read711()
    print(str((sumdata/80-value0)*0.009342926824)+"克   delay:"+str((time.ticks_ms()-c)/1000))
    time.sleep(0)