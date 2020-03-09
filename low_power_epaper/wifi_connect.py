import network
ssid='Jester'
pwrd='1281chas'
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    
    sta_if.active(True)
    sta_if.connect(ssid, pwrd)
    while not sta_if.isconnected():
        pass
    print('network config:', sta_if.ifconfig())


# def do_connect():
#     import network
#     sta_if = network.WLAN(network.STA_IF)
#     if not sta_if.isconnected():
#         print('connecting to network...')
#         sta_if.active(True)
#         sta_if.connect('<essid>', '<password>')
#         while not sta_if.isconnected():
#             pass
#     print('network config:', sta_if.ifconfig())