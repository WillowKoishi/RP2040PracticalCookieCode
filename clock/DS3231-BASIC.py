#!/usr/bin/python
# -*- coding: utf-8 -*-
from machine import I2C
from machine import Pin
import time

address = 0x68
register = 0x00

#sec min hour week day mout year
NowTime = b'\x00\x49\x22\x04\x28\x09\x22'

w  = ["SUN","Mon","Tues","Wed","Thur","Fri","Sat"];


bus = I2C(0,sda=Pin(4),scl=Pin(5))

def ds3231SetTime():
    bus.writeto_mem(int(0x68),int(0x00),NowTime);

def ds3231ReadTime():
    return bus.readfrom_mem(int(address),int(register),19);

ds3231SetTime()
while 1:
    t = ds3231ReadTime()
    a = t[0]&0x7F  #sec
    b = t[1]&0x7F  #min
    c = t[2]&0x3F  #hour
    d = t[3]&0x07  #week
    e = t[4]&0x3F   #day
    f = t[5]&0x1F  #mouth
    print("20%x/%02x/%02x %02x:%02x:%02x %s" %(t[6],t[5],t[4],t[2],t[1],t[0],w[t[3]-1]))
    timeStr=(str(hex(e))+","+str(hex(c))+":"+str(hex(b))+":"+str(hex(a)))
    print(timeStr.replace("0x",""))
    #print(str(c)+":"+str(b)+""+str(a))
    time.sleep(1)