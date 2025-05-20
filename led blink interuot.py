import machine
import time

led_pin= 2
button_pin= 0

led= machine.Pin(led_pin,machine.Pin.OUT)

button= machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)

def button_handler(pin):
    global led_pin
    led.value(not led.value())
    if led.value():
        print("user given input, led is on")
        time.sleep_ms(100)
    else:
        print("led is off")
    

    
    
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
 


while True:
    pass