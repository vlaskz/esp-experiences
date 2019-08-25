

def led_blink(blinks):
    import machine
    import time
    led = machine.Pin(2, machine.Pin.OUT)
    i = 0
    while i < 2*blinks:
        led.value(not led.value())
        time.sleep(.1)
        i = i + 1
    return led


def connect():
    ESSID = input('ESSID: ')
    PSSWD = input('PSSWD: ')
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ESSID, PSSWD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    led_blink(4)
    return sta_if


def start_web_server():
    import socket
    html = open('index.html')
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(1)
    print('listening on ', addr)
    while True:
        cl, addr = s.accept()
        print('Client connected. Address:', addr)
        req = cl.recv(1024)
        req = str(req)
        print('Content = %s' % req)
        cl.send('HTTP/1.1 200 OK\n')
        cl.send('Content-Type: text/html\n')
        cl.send('Connection: close\n\n')
        cl.sendall(html)
        cl.close()
