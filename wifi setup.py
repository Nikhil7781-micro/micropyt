import network

wlan= network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect("LAVA LXX504","00778100")

if wlan.isconnected():
    print("connected")
    
else:
    print("not connected")
    
