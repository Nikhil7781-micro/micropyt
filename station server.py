import network

n= network.WLAN(network.STA_IF)
n.active(True)
n.connect("LAVA LXX504","00778100")
if not n.isconnected():
    print("network is connecting")
    
print("connected")
ip= n.ifconfig()
print(ip)