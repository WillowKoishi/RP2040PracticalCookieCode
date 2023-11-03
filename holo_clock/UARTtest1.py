from machine import UART,Pin
import utime

nrst = Pin(6,Pin.OUT)
nrst.on()

uart = UART(1,baudrate=115200,stop=1,tx=Pin(4),rx=Pin(5))


nrst.off()
utime.sleep_ms(100)
nrst.on()
utime.sleep_ms(500)
uart.write("ChinaNet-wMMk")                 # INPUT SSID to ESP8266
utime.sleep_ms(500)
uart.write("tvfqca5y")                  # INPUT PASSWORD to ESP8266
utime.sleep_ms(500)
null=uart.readline()
while True:
    print("START reception")               # WAITING DATA
    while uart.any() == False:
        print(".",end='\0')
        utime.sleep_ms(1000)

    utime.sleep_ms(10)
    print("\n WiFi connected!\nUnix is:")
    buf=uart.readline()                    # RECEPTION Unix DATA
    utime.sleep_ms(200)
    print(buf)
  
    
    utime.sleep_ms(1000)
    #machine.reset()