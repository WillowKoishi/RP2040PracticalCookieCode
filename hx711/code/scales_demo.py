#date:2021-04-16
#lcd1602 +hx711
#https://Github.com/devonschafer/Raspberry_Pi_Pico_I2C_1602_LCD_16x2
#https://Github.com/SergeyPiskunov/micropython-hx711
#It works

from hx711 import HX711
from utime import sleep_us,sleep
import machine, utime
from machine import I2C, Pin

machine.freq(280000000)
vcc = Pin(5,Pin.OUT)
vcc.on()
gnd = Pin(2,Pin.OUT)
gnd.off()
print("scales begin...")

    
class Scales(HX711):
    def __init__(self, d_out, pd_sck):
        super(Scales, self).__init__(d_out, pd_sck)
        self.offset = 0

    def reset(self):
        self.power_off()
        self.power_on()

    def tare(self):
        self.offset = self.read()

    def raw_value(self):
        return self.read() - self.offset

    def stable_value(self, reads=10, delay_us=500):
        values = []
        for _ in range(reads):
            values.append(self.raw_value())
            sleep_us(delay_us)
        return self._stabilizer(values)
    
    @staticmethod
    def _stabilizer(values, deviation=10):
        weights = []
        for prev in values:
            weights.append(sum([1 for current in values if abs(prev - current) / (prev / 100) <= deviation]))
        return sorted(zip(values, weights), key=lambda x: x[1]).pop()[0]

#scales init
scales = Scales(d_out=3, pd_sck=4)
scales.tare() #setoff

while True:
    val =int(scales.stable_value()*(0.000482462)*100)/100
    print(val)
    sleep(1)
