import machine
import time
import urequests
import sys
import network

WIFI_SSID = "LAVA LXX504"
WIFI_PASS = "00778100"

WIFI_CONNECT_TIMEOUT = 5

def wifi_connect():
    wlan= network.WLAN(network.STA_IF)
    
    if wlan.isconnected():
        print("the device is already connected")
        print(wlan.ifconfig())
        return True
    
    print("connecting with wifi")
    wlan.active(True)
    wlan.connect(WIFI_SSID,WIFI_PASS)
    
    start_time=time.time()
    while not wlan.isconnected():
        if time.time()-start_time >= WIFI_CONNECT_TIMEOUT :
            wlan.disconnect()
            wlan.active(False)
            print("wifi connection timeout")
            return False
        print(".",end="")
        time.sleep(0.5)
    print("\nconnected with wifi")
    print(wlan.ifconfig())
    return True
if __name__== "__main__":
    if wifi_connect():
        print("station mode configure")
        req=urequests.get("https://example.com")
        print("request successful" if req.status_code==200 else "request failed")
        print(req.text)
        while True:
            time.sleep(20)
            if not network.WLAN(network.STA_IF).isconnected():
                print("the device lost the connection")
                if not wifi_connect():
                    print("reconnect the device")
                
            else:
                print("check the connection")

            
        
            
    