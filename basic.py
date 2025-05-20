import machine
import time

led= machine.Pin(2,machine.Pin.OUT)

while True:
    led.value(0)
    print("led is off")
    time.sleep_ms(1000)
    led.value(1)
    print("led is on")
    time.sleep_ms(1000)
    
    