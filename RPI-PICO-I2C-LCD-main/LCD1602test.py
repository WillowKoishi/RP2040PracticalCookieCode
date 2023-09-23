import utime,time,os
import machine
from machine import I2C
from lcd_api import LcdApi
from machine import Pin
from pico_i2c_lcd import I2cLcd
machine.freq(280000000)
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
address = 0x68
register = 0x00
vcc = Pin(6,Pin.OUT)
vcc.on()
print("Running test_main")
i2c = I2C(1, sda=machine.Pin(2), scl=machine.Pin(3), freq=400000)
i2c2 = I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
lcd.putstr("BAD APPLE!!\nIN LCD1602")
time.sleep(1)
lcd.clear()
lcd.putstr("by\nWillowKoishi")
time.sleep(1)
ba = open("ba.txt","r")
os.listdir()
print(i2c.scan())
lcd.custom_char(0,[0x0B,0x1D,0x1E,0x0A,0x1F,0x1A,0x1F,0x00,0x00])
lcd.custom_char(1,[0x14,0x1f,0x4,0x1f,0x18,0x0d,0x1d,0x00,0x00])
lcd.custom_char(2,[0x1f,0x15,0x1f,0x06,0x0e,0x1f,0x04,0x00,0x00])
lcd.custom_char(3,[0b0,0x1f,0x04,0x04,0x04,0x04,0x1f,0x00,0x00])
lcd.custom_char(4,[0b01010,0b01011,0b10110,0b10011,0b10010,0b10011,0b10010,0,0])
lcd.custom_char(5,[0b00100,0b11111,0b11101,0b01010,0b11101,0b00100,0b11111,0,0])
lcd.custom_char(6,[0x02,0x0F,0x08,0x08,0x08,0x08,0x10,0x00])
lcd.custom_char(7,[0x1F,0x0A,0x1F,0x1B,0x1B,0x11,0x1F,0x00])
lcd.clear()
lcd.putchar(chr(3))
lcd.putchar(chr(2))
lcd.putchar(chr(1))
lcd.putchar(chr(0))
lcd.move_to(0,1)
lcd.putchar(chr(7))
lcd.putchar(chr(6))
lcd.putchar(chr(5))
lcd.putchar(chr(4))
def ds3231ReadTime():
    return i2c2.readfrom_mem(int(address),int(register),19);
while 1:
    my=""
    cu_chr0=[]
    cu_chr1=[]
    cu_chr2=[]
    cu_chr3=[]
    cu_chr4=[]
    cu_chr5=[]
    cu_chr6=[]
    cu_chr7=[]
    for i in range(8):
        mx=ba.readline(24)
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        c6=0
        c7=0
        c8=0
        for d in range(5):
            j=4-d
            if mx[j:j+1]=="1":
                c1=(c1<<1|0)
            else:
                c1=(c1<<1|1)
            if mx[j+6:j+7]=="1":
                c2=(c2<<1|0)
            else:
                c2=(c2<<1|1)
            if mx[j+12:j+13]=="1":
                c3=(c3<<1|0)
            else:
                c3=(c3<<1|1)
            if mx[j+18:j+19]=="1":
                c4=(c4<<1|0)
            else:
                c4=(c4<<1|1)
        cu_chr0.append(c1)
        cu_chr1.append(c2)
        cu_chr2.append(c3)
        cu_chr3.append(c4)
        #mx=mx[0:5]+"\n"
        my=my+mx
    for k in range(8):
        mx=ba.readline(24)
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        c6=0
        c7=0
        c8=0
        for d in range(5):
            j=4-d
            if mx[j:j+1]=="1":
                c1=(c1<<1|0)
            else:
                c1=(c1<<1|1)
            if mx[j+6:j+7]=="1":
                c2=(c2<<1|0)
            else:
                c2=(c2<<1|1)
            if mx[j+12:j+13]=="1":
                c3=(c3<<1|0)
            else:
                c3=(c3<<1|1)
            if mx[j+18:j+19]=="1":
                c4=(c4<<1|0)
            else:
                c4=(c4<<1|1)
        cu_chr4.append(c1)
        cu_chr5.append(c2)
        cu_chr6.append(c3)
        cu_chr7.append(c4)
    lcd.custom_char(0,cu_chr0)
    lcd.custom_char(1,cu_chr1)
    lcd.custom_char(2,cu_chr2)
    lcd.custom_char(3,cu_chr3)
    lcd.custom_char(4,cu_chr4)
    lcd.custom_char(5,cu_chr5)
    lcd.custom_char(6,cu_chr6)
    lcd.custom_char(7,cu_chr7)
    #time.sleep(0.3)