from machine import Pin
from machine import Timer
import utime

mos_ctrl = Pin(28,Pin.OUT)
mos_ctrl.off()
led = (16,Pin.OUT)
#led.off()
mos_in = Pin(27,Pin.IN,Pin.PULL_UP)
i=123
def erer():
    #print("t1")
    if mos_in.value()==0:
        print(i)

tim=Timer(period=1,mode=Timer.PERIODIC,callback = lambda t:erer())
utime.sleep_ms(1000)
mos_ctrl.on()
utime.sleep_ms(25)
mos_ctrl.off()
utime.sleep_ms(500)
print("START TEST")
mos_ctrl.on()
i=i+1
utime.sleep_ms(500)
mos_ctrl.off()
utime.sleep_ms(500)
mos_ctrl.on()
i=i+1
utime.sleep_ms(100)
mos_ctrl.off()
