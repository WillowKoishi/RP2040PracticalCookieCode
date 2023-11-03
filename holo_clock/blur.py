from machine import Pin
import time,utime,random,math
from neopixel import NeoPixel
from machine import Timer
pin = Pin(7, Pin.OUT)
np = NeoPixel(pin,60)
machine.freq(260000000)

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

    
rgb_seq=[]
for i in range(60):
    rgb_seq.append([0.01,0.01,0.01])
    #print(rgb_seq)

sec = 0+6
mim=07+6
hur=3
def seq_util(de):
    de = de*0.4
    return de
mtick=0
def mPrint():
    global mtick,sec,mim,hur
    #print("tick:"+str(mtick)+"  t:"+str(hur)+":"+str(mim)+":"+str(sec))
    mtick = 0
    sec=sec+1
    if sec>=60:
        sec=0
        mim=mim+1
    if mim>=60:
        mim=0
        hur=hur+1
    if hur>=12:
        hur=0
    rgb_seq[sec]=[0,200,200]
    rgb_seq[mim]=[200,0,200]
    rgb_seq[hur*5+6]=[191,140,100]
tim = Timer(period=1000,mode=Timer.PERIODIC,callback =lambda t:mPrint())
while 1:
    mtick = mtick +1
    for i in range(60):
        #m_rgb_seq=rgb_seq[i]
        #rgb_seq[i]=[seq_util(rgb_seq[i][0]),seq_util(rgb_seq[i][1]),seq_util(rgb_seq[i][2])]
        rgb_seq[i]=[rgb_seq[i][0]*0.99,rgb_seq[i][1]*0.99,rgb_seq[i][2]*0.99]
        #print((int(math.pow(rgb_seq[i][0]/255,1.4)*255),int(math.pow(rgb_seq[i][1]/255,1.4)*255),int(math.pow(rgb_seq[i][2]/255,1.4)*255)))
        np[i] = (int(math.pow(rgb_seq[i][0]/255,2)*255),int(math.pow(rgb_seq[i][1]/255,2)*255),int(math.pow(rgb_seq[i][2]/255,2)*255))
    time.sleep_us(2160)
    np.write()
    #print(mtick)
    

    
