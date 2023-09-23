import time
import random
from machine import Pin, PWM
vcc=Pin(0,Pin.OUT)
vcc.value(1)
REG_SEC=0
REG_MIN=1
REG_HOUR=2
REG_DATE=3
REG_MON=4
REG_DOW=5
REG_YEAR=6
REG_WP=7
REG_TCR=8