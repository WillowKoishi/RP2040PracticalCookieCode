# test of printing multiple fonts to the ILI9341 on an M5Stack using H/W SP
# MIT License; Copyright (c) 2017 Jeffrey N. Magee

from ili934xnew import ILI9341, color565
from machine import Pin, SPI
from machine import Pin, PWM
from utime import sleep_us, time
import time
import rp2
import m5stack
import glcdfont
import tt14
import tt24
import tt32

from machine import Pin
import time,utime

from neopixel import NeoPixel
machine.freq(133000000)
pin = Pin(11, Pin.OUT)
np = NeoPixel(pin,12)

pwm = PWM(Pin(21))
pwm.freq(20000)

PWM0 =(0)
pwm.duty_u16(PWM0)
time.sleep_ms(300)

fonts = [glcdfont,tt14,tt24,tt32]

text = 'POWERED BY FAIRING STUDIO \n FAIRING STUDIO.COM'

power = Pin(m5stack.TFT_LED_PIN, Pin.OUT)
power.value(1)

spi = SPI(
    0,
    baudrate=160000000,
    miso=Pin(4),
    mosi=Pin(7),
    sck=Pin(6))

display = ILI9341(
    spi,
    cs=Pin(5),
    dc=Pin(9),
    rst=Pin(8),
    w=320,
    h=240,
    r=3)

display.erase()
display.set_pos(0,0)
for ff in fonts:
    display.set_font(ff)
    display.print(text)
    
for i in range(12):
    np[i] = (255, 255, 255) 
np.write()

R = 0
G = 0
B = 0
m = 0
X = 0
C = 0
def HSV2RGB(H,S,V):
    global R,G,B,m,X,C
    if H<0:
        H = H+360
    if H>359.9:
        H = H-360
    H = (H/60)
    C = V*S
    i = int(H)
    X = C * (1-abs(H%2 - 1))
    m = V - C
    if i==0:
        R = C
        G = X
        B = 0
    if i==1:
        R = X
        G = C
        B = 0
    if i==2:
        R = 0
        G = C
        B = X
    if i==3:
        R = 0
        G = X
        B = C
    if i==4:
        R = X
        G = 0
        B = C
    if i==5:
        R = C
        G = 0
        B = X

    #R = int((R+m)*255)
    #G = int((G+m)*255)
    #B = int((B+m)*255)
    if R == 65025:
        R = 255
        B = 0
    if G == 36720:
        G = 0
    ##print("H:"+str(H*60)+"R:"+str((R+m)*255)+"G:"+str((G+m)*255)+"B:"+str((B+m)*255))
color =280
phase = 20
#H色度(0~360) S饱和度(0~1) V明度(0~1)
s = 1
v = 0.2
while True:
    PWM1 =(0)
    pwm.duty_u16(PWM1)
    time.sleep_ms(100)
    
    color = color-1
    if color==360:
        color=0
    if color==0:
        color=359
    print()
    HSV2RGB(color,s,v)
    np[0] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    np[9] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase,s,v)
    np[1] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*2,s,v)
    np[10] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*3,s,v)
    np[2] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*4,s,v)
    np[11] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*5,s,v)
    np[3] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*6,s,v)
    np[8] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    np[4] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*7,s,v)
    np[7] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*8,s,v)
    np[5] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*9,s,v)
    np[6] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    if ((R+m)*255>255)|((G+m)*255>255)|((B+m)*255>255):
#        print("overload")
        break
    time.sleep(0.1)
    np.write()
    
    PWM2 =(65535)
    pwm.duty_u16(PWM2)
    time.sleep_ms(100)