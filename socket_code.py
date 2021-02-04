import socket
import time

s = socket.socket()
print("Socket successfully created")

port = 28965


s.bind(('192.168.0.131', port))
print("socket binded to %s" % (port))


s.listen(5)
print("socket is listening")

print(s)

while True:

    c, addr = s.accept()
    print(c)
    print('Got connection from', addr)


    output = 'Thank you for connecting'
    c.sendall(output.encode('utf-8'))

    x = 0
    for i in range(0,100):
        time.sleep(1)
        c.sendall(("Thanks again " + str(x) + '\n').encode('utf-8'))
        x = x + 1



