import utime,time,os
import machine
from machine import Pin
from neopixel import NeoPixel
pin = Pin(6, Pin.OUT)
np = NeoPixel(pin,64)
ba = open("ba.txt","r")
os.listdir()
ON = [10,10,10]
OFF = [0,0,0]
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
    R = int((R+m)*255)
    G = int((G+m)*255)
    B = int((B+m)*255)
    if R == 65025:
        R = 255
        B = 0
    if G == 36720:
        G = 0
    #print("H:"+str(H*60)+"R:"+str((R+m)*255)+"G:"+str((G+m)*255)+"B:"+str((B+m)*255))
color =280
phase = 8
#H色度(0~360) S饱和度(0~1) V明度(0~1)
s =1
v = 1
while True:
    color = color-5
    if color>=360:
        color=0
    if color<=0:
        color=359
    color = color + 1
    HSV2RGB(color,s,v)
    ON = [R,G,B]
    HSV2RGB(color+180,s,v)
    OFF = [R,G,B]
    t1 = time.ticks_ms()
    for i in range(8):
        mx=ba.readline(24)
        mx=ba.readline(24)
        for ix in range(8):
            if i%2==0:
                if mx[int(ix*2.8):int(ix*2.8)+1] == "1":
                    np[ix+i*8]=ON
                else:
                    np[ix+i*8]=OFF
            else:
                if mx[int(ix*2.8):int(ix*2.8)+1] == "1":
                    np[-ix+i*8+7]=ON
                else:
                    np[-ix+i*8+7]=OFF
    time.sleep_ms(10)
    np.write()
    print(time.ticks_ms()-t1)