import machine
import time


on_time=1000
off_time=500
led_state=0
last_state=0


led= machine.Pin(2,machine.Pin.OUT)

while True:
    current_time= time.ticks_ms()
    if led_state==0:
        if time.ticks_diff(current_time,last_state)>= off_time:
            led.value(1)
            led_state=1
            print("led is on")
            last_state=current_time
    else:
        if time.ticks_diff(current_time,last_state)>= on_time:
            led.value(0)
            led_state=0
            print("led is off")
            last_state=current_time
            