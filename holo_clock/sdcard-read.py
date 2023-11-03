from machine import SPI,Pin
import os,sdcard
sdi = SPI(1, baudrate=8000000,  sck=Pin(14), mosi=Pin(15), miso=Pin(12))
sd = sdcard.SDCard(sdi, Pin(13))
sdfile=os.VfsFat(sd)
os.mount(sdfile,'/sd')