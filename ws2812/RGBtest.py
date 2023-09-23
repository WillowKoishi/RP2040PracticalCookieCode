from machine import Pin
import time,utime,random
from neopixel import NeoPixel
pin = Pin(16, Pin.OUT)
np = NeoPixel(pin,64)

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
    #print("H:"+str(H*60)+"R:"+str((R+m)*255)+"G:"+str((G+m)*255)+"B:"+str((B+m)*255))
color =280
phase = 8
#H色度(0~360) S饱和度(0~1) V明度(0~1)
s =1
v = 0.5
while 0:
    color = color-0.5
    if color>=360:
        color=0
    if color<=0:
        color=359
    HSV2RGB(color,s,v)
    np[9] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    np[0] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase,s,v)
    np[1] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*2,s,v)
    np[2] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*2.5,s,v)
    np[4] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*3,s,v)
    np[3] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*5,s,v)
    np[6] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*6,s,v)
    np[5] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    np[8] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    HSV2RGB(color+phase*7,s,v)
    np[7] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
    #time.sleep(0.02)
    np.write()
while 0:
    for i in range(64):
        HSV2RGB(random.randint(0,360),s,random.randint(0,50)/100)
        np[i] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
        time.sleep(0.00)
    np.write()
while 0:
    col2or = color-2
    if color>=360:
        color=0
    if color<=0:
        color=359
    HSV2RGB(color,s,v)
    for i in range(32):
        HSV2RGB(color+i*3,1,1)
        #np[i] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
        np[i] = (100, 0,60)
    for i in range(32):
        np[i+32] = (0, 60,150)
    np.write()
while 1:
    for i in range(64):
        HSV2RGB(0,0,1)
        np[i] = (int((R+m)*255), int((G+m)*255), int((B+m)*255))
        time.sleep(0.00)
    np.write()