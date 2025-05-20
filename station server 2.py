import machine
import network
import time

def wifi_connect(ssid,pas,timeout):
    wlan= network.WLAN(network.STA_IF)
    wlan.active(True)
    t=0
    if not wlan.isconnected():
        print("connecting.....")
        while (not wlan.isconnected() and t<timeout):
            print(timeout-t)
            wlan.connect(ssid,pas)
            t+=1
            time.sleep(1)
        
    if wlan.isconnected():
        print("connected successfully")
    else:
        print("not connected")

wifi_connect("LAVA LXX504","00778100",4)


            