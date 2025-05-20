import machine
import time


class toggle:
    
    def __init__(self,pin,off_time,on_time):
        self.pin= pin
        self.on_time= on_time
        self.off_time= off_time
        self.last_change= 0
        self.led_state= 0
        self.led= machine.Pin(self.pin,machine.Pin.OUT)
        
    def update(self):
        if (time.ticks_ms()-self.last_change>= self.off_time) and self.led_state == 0:
            self.last_change=time.ticks_ms()
            self.led_state=1
            self.led.value(1)
            print("led is on",self.pin)
        elif (time.ticks_ms()-self.last_change>= self.on_time) and self.led_state == 1:
            self.last_change=time.ticks_ms()
            self.led_state=0
            self.led.value(0) 
            print("led is off",self.pin)
                
led1= toggle(2,400,800)

while True:
    
    led1.update()
    