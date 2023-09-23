from machine import Pin, ADC
from machine import Timer
import utime
import math

ADC0= ADC(Pin(26))
fan = Pin(18,Pin.OUT)#,Pin.OPEN_DRAIN)
heat = Pin(19,Pin.OUT)#,Pin.OPEN_DRAIN)

fan.off()
heat.on()
vTList = []
tVList = []
vt1 = open("v-t.csv","r")
tv1 = open("t-v.csv","r")

x_last = 0
p_last = 0
q = 0.01#系统噪音
r = 0.8#测量噪音
ADC_reference_voltage = 3  #ADC参考电压 V

def kf(z_measure,x_last=0,p_last=0,q=0.01,r=0.8):
    x_mid = x_last
    p_mid = p_last +q
    kg = p_mid/(p_mid+r)
    x_now = x_mid + kg*(z_measure-x_mid)
    p_now = (1-kg)*p_mid
    p_last = p_now
    x_last = x_now
    return x_now,p_last,x_last

dTime = 0
RTIndex = 0
def mTimer():
    global dTime,RTIndex,tVList
    dTime=dTime+1
    print("time:"+str(dTime))
    if dTime >= tVList[RTIndex][0]:
        RTIndex = RTIndex + 1
        print("togget temp:"+str(tVList[RTIndex][1]))





for i in range(270):
    mvt = vt1.readline()
    mvt = mvt.rstrip()
    mvt =mvt.replace("\ufeff", "")
    mvt =mvt.replace("\r\n", "")
    c = mvt.split(",")
    #print(mvt)
    vTList.append([float(c[0]),float(c[1])])
#print(vTList)
    

for i in range(81):
    mvt = tv1.readline()
    mvt = mvt.rstrip()
    mvt =mvt.replace("\ufeff", "")
    mvt =mvt.replace("\r\n", "")
    c = mvt.split(",")
    print(mvt)
    tVList.append([float(c[0]),float(c[1])])
print(tVList)
    
def v2t(voltage1):
    #print(voltage1)
    for i in range(270):
        if voltage1 >= float(vTList[i][1]):
            #print(vTList[i][0])
            return (vTList[i][0] - 8)
    return 270

for c in range(10):
    utime.sleep_ms(1000)
    print(str(10-c)+"秒后开始预热")
x_last = v2t(ADC0.read_u16()*ADC_reference_voltage/65535)
while True:
    mTemp=v2t(ADC0.read_u16()*ADC_reference_voltage/65535)
    post_dat,p_last,x_last = kf(mTemp,x_last,p_last,q,r)
    utime.sleep_ms(1000)
    if mTemp <= 40:
        heat.on()
    else:
        break
    print("pre-heating:"+str(post_dat))
for c in range(5):
    utime.sleep_ms(1000)
    print(str(5-c)+"秒后开始加热")

tim = Timer(period=1000,mode=Timer.PERIODIC,callback =lambda t:mTimer())
while True:
    #read_voltage0 = ADC0.read_u16()*ADC_reference_voltage/65535
    mTemp=v2t(ADC0.read_u16()*ADC_reference_voltage/65535)
    post_dat,p_last,x_last = kf(mTemp,x_last,p_last,q,r)
    #print("raw_temp:"+str(mTemp))
    print("filted_dat:"+str(post_dat))
    if mTemp <= tVList[RTIndex][1]:
        heat.on()
    else:
        heat.off()
    utime.sleep_ms(500)